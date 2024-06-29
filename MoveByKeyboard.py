import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((500, 500),0, 32)
sprite1 = pygame.image.load('Images/butterfly.png')
sprite1 = pygame.transform.scale(sprite1, (50, 50))  #resize of the butterfly
spriteWidth = sprite1.get_width()
spriteHeight = sprite1.get_height()
pygame.display.set_caption('Hello Keyboard')
screen.fill((0, 0, 0))
game_over = False

#set up butterfly to be 0,0
x,y = (0,0)
#main loop
clock = pygame.time.Clock()
while not game_over:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    #set up control by keyboard
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
       y -= 0.5 * dt
    if pressed_keys[K_DOWN]:
       y += 0.5 * dt
    if pressed_keys[K_RIGHT]:
       x += 0.5 * dt
    if pressed_keys[K_LEFT]:
       x -= 0.5 * dt
    if pressed_keys[K_SPACE]:
       x,y = (0,0)

  # Restricting Movement fram screen
    if x > (screen.get_width() - spriteWidth):
        x = screen.get_width() - spriteWidth;

    if y > (screen.get_height() - spriteHeight):
        y = screen.get_height() - spriteHeight;
    if x < 0:
        x = 0
    if y < 0:
        y = 0

    screen.fill((0, 0, 0)) #clear sceen
    screen.blit(sprite1, (x,y))
    pygame.display.update()
pygame.quit()
