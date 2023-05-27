import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set the width and height of the display window
width = 800
height = 600

# Set the size of each snake segment and the speed of the snake
segment_size = 20
segment_speed = 20

# Set the font for the game over message
font_style = pygame.font.SysFont(None, 50)

# Initialize the display window
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Define a function to display the score on the screen
def show_score(score):
    score_text = font_style.render('Score: ' + str(score), True, black)
    display.blit(score_text, [10, 10])

# Define the snake function
def snake(segment_size, snake_list):
    for segment in snake_list:
        pygame.draw.rect(display, green, [segment[0], segment[1], segment_size, segment_size])

# Define the game loop
def game_loop():
    game_over = False
    game_end = False

    # Initial position of the snake
    x1 = width / 2
    y1 = height / 2

    # Initial movement direction
    x1_change = 0
    y1_change = 0

    # Create the snake list and length
    snake_list = []
    snake_length = 1

    # Generate the initial position of the food
    foodx = round(random.randrange(0, width - segment_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - segment_size) / 20.0) * 20.0

    while not game_over:

        while game_end == True:
            display.fill(white)
            game_over_message = font_style.render('Game Over! Press Q-Quit or C-Play Again', True, black)
            display.blit(game_over_message, [width / 6, height / 3])
            show_score(snake_length - 1)
            pygame.display.update()

            # Handle game over events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_end = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -segment_speed
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = segment_speed
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -segment_speed
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = segment_speed
                    x1_change = 0

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        display.fill(white)
        pygame.draw.rect(display, red, [foodx, foody, segment_size, segment_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_end = True

        # Check for collision with boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_end = True

        # Draw the snake
        snake(segment_size, snake_list)

        # Update the display
        show_score(snake_length - 1)
        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - segment_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - segment_size) / 20.0) * 20.0
            snake_length += 1

        # Set the game speed
        clock.tick(15)

    pygame.quit()
    quit()

# Start the game
game_loop()
