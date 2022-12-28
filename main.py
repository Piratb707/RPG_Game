import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600, 350))
pygame.display.set_caption("RPG_Game")
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)

#Player
bg = pygame.image.load('images/bg.jpg').convert_alpha()
walk_left = [
    pygame.image.load('Animation\Player\StaySteelL.png').convert_alpha(),
    pygame.image.load('Animation\Player\PreWalkL.png').convert_alpha(),
    pygame.image.load('Animation\Player\WalkL.png').convert_alpha(),
    pygame.image.load('Animation\Player\StaySteelL.png').convert_alpha()
]
walk_right = [
    pygame.image.load('Animation\Player\StaySteel.png').convert_alpha(),
    pygame.image.load('Animation\Player\PreWalkR.png').convert_alpha(),
    pygame.image.load('Animation\Player\WalkR.png').convert_alpha(),
    pygame.image.load('Animation\Player\StaySteel.png').convert_alpha()
]


#Enemy Devil
devil = pygame.image.load('images/devil.png').convert_alpha()
devil_list_in_game = []

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 170

is_jump = False
jump_count = 10 

bg_sound = pygame.mixer.Sound("music/Walk.mp3")
bg_sound.play()
bg_sound.set_volume(0.1)

devil_timer = pygame.USEREVENT + 1
pygame.time.set_timer(devil_timer, 2500)

label = pygame.font.Font('fonts/RubikBubbles-Regular.ttf', 40)
lose_label = label.render("You Lose!", False, (193, 196, 199))
res_label = label.render("Try Again", False, (113, 126, 19))
res_label_rect = res_label.get_rect(topleft=(180, 200))

#Стрельба
bullets_left = 5
bullet = pygame.image.load("images/bullet.png")
bullets = []

gameplay = True

#Running
running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 600, 0))

    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        
        #Enemy Collide
        if devil_list_in_game:
            for (i, el) in enumerate(devil_list_in_game):
                screen.blit(devil, el)
                el.x -= 10

                if el.x < -25:
                    devil_list_in_game.pop(i) #Удаление врагов с карты

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()
        
        #Key Left & Right
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > -20:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 500:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True

        #Jump
        else:
            if jump_count >= -10:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10

        #Animation
        if player_anim_count == 3:
            player_anim_count =0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == - 618:
            bg_x = 0

        #Стрельба
        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 4


                if el.x > 630:
                    bullets.pop(i)
                
                if devil_list_in_game:
                    for (index, devil_el) in enumerate(devil_list_in_game):
                        if el.colliderect(devil_el):
                            devil_list_in_game.pop(index)
                            bullets.pop(i)

    else:
        screen.fill((56, 11, 98))
        screen.blit(lose_label, (180, 100))
        screen.blit(res_label, (res_label_rect))

        mouse = pygame.mouse.get_pos()
        if res_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            devil_list_in_game.clear()
            bullets.clear()

    pygame.display.update()

    #Game running event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == devil_timer:
            devil_list_in_game.append(devil.get_rect(topleft=(620, 115)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 30 , player_y + 10)))
            bullets_left -= 1

    clock.tick(15)