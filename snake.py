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
purple = (106, 13, 173) #random back splash


#Fonts
font = pygame.font.SysFont('Helvetica', 40)


#Display Text

#Intro Title OF The Game Name
game_title_text = font.render('Snake', True, white, purple)
title_rect = game_title_text.get_rect()
title_rect.center = (window_width//2, window_height//2)

#Score Display For Left Hand Top Corner
score_display_text = font.render('Score: ' + str(score), True, white, purple )
score_rect = score_display_text.get_rect()
score_rect.topleft = (25, 25)

#Character's for the game






#Play Again Text Display
play_again_text = font.render("Play Again Hit Any Key", True, white, purple )
play_again_text_rect = play_again_text.get_rect()
play_again_text_rect.center = (window_width//2, window_height//2)

#Main game loop
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False



pygame.display.update()
pygame.quit()


