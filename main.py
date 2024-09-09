import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
bg_color = pygame.Color(255,255,255)
pygame.display.set_caption("Window")
screen.fill(bg_color)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    clock.tick(60)

pygame.quit()
exit()