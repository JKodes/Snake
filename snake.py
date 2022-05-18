import pygame, random

#Initializer
pygame.init()

#Line 6-10 is window display settings 
window_width = 800
window_height = 800
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('SNAKE')

#Speed of the game
frame_per_second = 25
clock = pygame.time.Clock()

#Main game elements
snake_mass = 40


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
apple = (300, 300, snake_mass, snake_mass)
apple_rect = pygame.draw.rect(game_window, blue, apple)
head = (snake_head_x, snake_head_y, snake_mass, snake_mass)
head_rect = pygame.draw.rect(game_window, yellow, head)
snake_body =[]


#Play Again Text Display
play_again_text = font.render("Play Again Hit Spacebar  Key", True, white, purple )
play_again_text_rect = play_again_text.get_rect()
play_again_text_rect.center = (window_width//2, window_height//2)



#Main game loop
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_direction_x = -1*snake_mass
                snake_direction_y =0
            if event.key == pygame.K_RIGHT:
                 snake_direction_x = snake_mass
                 snake_direction_y =0
            if event.key == pygame.K_UP:
                 snake_direction_x =0
                 snake_direction_y =-1*snake_mass
            if event.key == pygame.K_DOWN:
                 snake_direction_x =0
                 snake_direction_y =snake_mass

    snake_body.insert(0, head)
    snake_body.pop()

    snake_head_x += snake_direction_x
    snake_head_y += snake_direction_y
    head = (snake_head_x, snake_head_y, snake_mass, snake_mass)

    #Snake hit wall collision
    if head_rect.left < 0 or  head_rect.right > window_width or head_rect.top < 0 or head_rect.bottom > window_height:
        game_window.blit(play_again_text, play_again_text_rect)
        pygame.display.update()

        reset_game = True
        while reset_game:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score =0
                        snake_head_x = window_width // 2
                        snake_head_y = window_height //2 + 200

                        head = (snake_head_x, snake_head_y, snake_mass, snake_mass)

                        snake_body =[]
                        snake_direction_x =0
                        snake_direction_y =0

                        reset_game = False
                        if event.type == pygame.QUIT:
                            reset_game = False
                            playing = False

                

               



 #Snake collision with apple causes score to update by one 
    if head_rect.colliderect(apple_rect):
        score += 1

        apple_pos_x = random.randint(0, window_width - snake_mass)
        apple_pos_y = random.randint(0, window_height - snake_mass)
        apple = (apple_pos_x, apple_pos_y, snake_mass, snake_mass)

        snake_body.append(head)

    score_display_text = font.render('Score: ' + str(score), True, white, purple )

    game_window.fill(green)
    game_window.blit(game_title_text, title_rect)
    game_window.blit(score_display_text,score_rect)

    for stomach in snake_body:
        pygame.draw.rect(game_window, blue, stomach)

    head_rect = pygame.draw.rect(game_window, yellow, head)
    apple_rect = pygame.draw.rect(game_window, blue, apple)

    pygame.display.update()
    clock.tick(frame_per_second)


pygame.display.update()
pygame.quit()


