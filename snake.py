import pygame

#Initializer
pygame.init()

#Line 6-10 is window display settings 
window_width = 800
window_height = 800
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('SNAKE')

#Speed of the game
frame_per_second = 60
clock = pygame.time.Clock()

#Main game elements
snake_body = 40


snake_head_x = window_width // 2
snake_head_y = window_height //2 + 200

snake_direction_x = 0
snake_direction_y = 0

score = 0

#Colors
blue = (0, 102, 204) #apple color
yellow = (255, 255, 51) #snake color 
green  = (0, 153, 0) #grass color
white = (255, 255, 255) #font color


#Fonts


#Display Text


#Main game loop
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False



pygame.display.update()
pygame.quit()


