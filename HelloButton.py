import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Hello Button')
text_color = (255, 255, 255)
button_color = (0, 0, 170)
button_over_color = (255, 50, 50)
button_width = 100
button_height = 50
button_rect = [screen.get_width() / 2 - button_width / 2,
               screen.get_height() / 2 - button_height / 2,
               button_width, button_height]
button_font = pygame.font.SysFont('Arial', 20)
button_text = button_font.render('Quit', True, text_color)
screen.fill((100, 100, 100))
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if(button_rect[0] <= x <= button_rect[0] + button_rect[2] and
               button_rect[1] <= y <= button_rect[1] + button_rect[3]):
                game_over = True

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if (button_rect[0] <= mouse_x <= button_rect[0] + button_rect[2] and
            button_rect[1] <= mouse_y <= button_rect[1] + button_rect[3]):
        current_button_color = button_over_color
    else:
        current_button_color = button_color

    screen.fill((100, 100, 100))  # Clear the screen


    pygame.draw.rect(screen, current_button_color, button_rect)
    screen.blit(button_text, (button_rect[0] + (button_width - button_text.get_width()) / 2,
                              button_rect[1] + (button_height / 2 - button_text.get_height() / 2)))

    pygame.display.update()

pygame.quit()
