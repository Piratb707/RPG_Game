import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300)) #flags=pygame.NOFRAME)
pygame.display.set_caption("RPG_Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

running = True
while running:

    #screen.fill((114,157,224))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((70, 44, 133))