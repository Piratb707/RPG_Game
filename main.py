import pygame


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600, 350))
pygame.display.set_caption("RPG_Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.jpg')

walk_left = [
    pygame.image.load('Animation\Player\StaySteelL.png'),
    pygame.image.load('Animation\Player\PreWalkL.png'),
    pygame.image.load('Animation\Player\WalkL.png'),
    pygame.image.load('Animation\Player\StaySteelL.png')
]

walk_right = [
    pygame.image.load('Animation\Player\StaySteel.png'),
    pygame.image.load('Animation\Player\PreWalkR.png'),
    pygame.image.load('Animation\Player\WalkR.png'),
    pygame.image.load('Animation\Player\StaySteel.png')
]

player_anim_count = 0
bg_x = 0

bg_sound = pygame.mixer.Sound("music/Walk.mp3")
bg_sound.play()

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 600, 0))
    screen.blit(walk_right[player_anim_count], (300, 170))

    if player_anim_count == 3:
        player_anim_count =0
    else:
        player_anim_count += 1

    bg_x -= 2
    if bg_x == - 618:
         bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(13)