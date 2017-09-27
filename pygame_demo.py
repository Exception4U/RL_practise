import pygame
pygame.init()
pygame.display.set_mode()
events = pygame.event.get()
while(1):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print ("LEFT")
            if event.key == pygame.K_RIGHT:
                print ("RIGHT")
