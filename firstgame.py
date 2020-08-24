import pygame
import moveable
pygame.init()
screen = pygame.display.set_mode([1900, 1050])

bg = pygame.image.load("Mushroom_Forest_Corona.jpg").convert_alpha()
screen.blit(bg, (0,0))
# bg.convert()
df = pygame.image.load("df3.png").convert_alpha()
running = True

dragonfly = moveable.Movable(screen, df, 250,250)

game_objects = [dragonfly]

while running: 
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dragonfly.set_delta(-1, 0)
    if keys[pygame.K_RIGHT] :
        dragonfly.set_delta(1, 0)
    if keys[pygame.K_UP]:
        dragonfly.set_delta(0,-1)
    if keys[pygame.K_DOWN]:
        dragonfly.set_delta(0, 1)
    if keys[pygame.K_SPACE]:
        dragonfly.clear_delta()

    screen.blit(bg, (0,0))

    # redraw background
    for obj in game_objects:
        obj.do_it()
        # pass
    pygame.display.flip()

