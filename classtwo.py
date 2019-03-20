import pygame
 
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Oi, sou o PyGame")
done = False
 
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
         
        pygame.display.flip()

pygame.quit()