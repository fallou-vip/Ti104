import pygame
pygame.init()
pygame.display.set_mode((800,600))
pygame.display.set_caption("rpgFallou")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit(0)