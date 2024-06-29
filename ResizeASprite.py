import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500),0, 32)
sprite1 = pygame.image.load('Images/butterfly.png')
sprite1 = pygame.transform.scale(sprite1, (50, 50))  #resize of the butterfly
spriteWidth = sprite1.get_width()
spriteHeight = sprite1.get_height()
pygame.display.set_caption('Hello Reize')
screen.fill((0, 0, 0))
game_over = False
#main loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
     #  screen.blit(sprite1, (350-128, 350-128)) ===>> 128 is half of size image butterfly //350 is half of size 700x700
     #  Easy way for code is below
    screen.blit(sprite1, (screen.get_width()/2 - spriteWidth/2, screen.get_height()/2 - spriteHeight/2))
    pygame.display.update()
pygame.quit()


