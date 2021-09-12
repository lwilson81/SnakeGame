import pygame
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((1500, 1000))
screen_rect=screen.get_rect()
player=pygame.Rect(300, 300, 50, 50)
#background_img = pygame.image.load('resources/images/space.jpg').convert()
run=True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]: player.move_ip(0, -1)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: player.move_ip(-1, 0)
    if keys[pygame.K_DOWN] or keys[pygame.K_d]: player.move_ip(0, 1)
    if keys[pygame.K_RIGHT] or keys[pygame.K_s]: player.move_ip(1, 0)
    player.clamp_ip(screen_rect) # ensure player is inside screen
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,0,200), player)
    pygame.draw.circle(screen,(200,0,0),(500,900),30)
    #screen.blit(background_img,[0,0])
    pygame.display.flip()