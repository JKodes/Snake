import pygame

pygame.init()


window_width = 800
window_height = 800

game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('SNAKE')




playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False



pygame.display.update()
pygame.quit()


