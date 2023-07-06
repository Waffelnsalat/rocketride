import sys
import pygame
import random


def game_over_screen(scor):
    # Initialize the font
    fontscore = pygame.font.Font(None, 36)
    # Create the game over text
    game_over_text = fontscore.render("Game Over", True, (255, 255, 255))
    scoretext = fontscore.render("Your score is: " + str(scor), True, (255, 255, 255))
    global high_score
    if scor > high_score:
        high_score = scor
    high_score_text = fontscore.render("High" + "score: " + str(high_score), True, (255, 255, 255))
    # Get the size of the game over text
    text_rect = game_over_text.get_rect()
    score_rect = scoretext.get_rect()
    high_score_rect = high_score_text.get_rect()
    # Center the text on the screen
    text_rect.center = (window_size[0] // 2, window_size[1] // 2)
    score_rect.center = (window_size[0] // 2, window_size[1] // 2 + 50)
    high_score_rect.center = (window_size[0] // 2, window_size[1] // 2 + 100)
    waiting = True
    while waiting:
        # Clear the screen
        screen.fill((0, 0, 0))
        # Draw the game over text
        screen.blit(game_over_text, text_rect)
        screen.blit(scoretext, score_rect)
        screen.blit(high_score_text, high_score_rect)
        # Update the display
        pygame.display.update()
        # Check for events
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif events.type == pygame.KEYDOWN:
                waiting = False


# Initialize the score
score = 0

# Define High score
high_score = 0

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (800, 800)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Rocket Ride')

# Load the main character image
character_image = pygame.image.load('character.png')

# Set the position of the character
character_pos = (window_size[0] / 2, window_size[1] - character_image.get_height() - 5)

# Set the default speed of the character
default_speed = 1
default_speed_y = 1

# Set the current speed of the character
character_speed = default_speed
character_speed_y = default_speed_y

# Set the direction of the character
character_direction = 'stay'
character_direction_y = 'stay'

# Set the running state of the game
running = True

# Create a list to hold obstacle positions and speeds
obstacles = []

# Load the obstacle image
obstacle_image = pygame.image.load('obstacle.png')

# Set the number of obstacles to be generated
num_obstacles = 6

# Create initial positions and speeds for the obstacles
for i in range(num_obstacles):
    obstacle_pos = (random.randint(30, window_size[0] - obstacle_image.get_width()), random.randint(-600, -100))
    obstacle_speed = random.uniform(0.1, 0.7)
    obstacles.append([obstacle_image, obstacle_pos, obstacle_speed])

# Set the clock and the delay for the obstacle
clock = pygame.time.Clock()

# Create a font to display the score
font = pygame.font.Font(None, 36)

# Keep track of the time when the score was last incremented
last_increment_time = pygame.time.get_ticks()

# Create a counter to keep track of the time passed
counter = 0
# Set the speed increment for each second
speed_increment = 0.001

# Load the background image
bg_image = pygame.image.load('bg.png')
bg_image2 = pygame.image.load('bg.png')

# Set the transparency of the background image to 50%
bg_image.set_alpha(200)
bg_image2.set_alpha(200)

# Set the initial position of the background
bg_pos = [0, -300]
bg_pos2 = [0, -bg_image.get_height() - 300]
# Set the speed of the background
bg_speed = 0.3


def start_screen():
    # Initialize the font
    font_for_start = pygame.font.Font(None, 36)
    # Create the start text
    start_text = font_for_start.render("Press any key to start", True, (255, 255, 255))
    # Get the size of the start text
    text_rect = start_text.get_rect()
    # Center the text on the screen
    text_rect.center = (window_size[0] // 2, window_size[1] // 2)

    waiting = True
    while waiting:
        # Clear the screen
        screen.fill((0, 0, 0))
        # Draw the start text
        screen.blit(start_text, text_rect)
        # Update the display
        pygame.display.update()
        # Check for events
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif events.type == pygame.KEYDOWN:
                waiting = False
                # reset obstacles
                global obstacles
                obstacles.clear()
                obstacles = []
                # Create initial positions and speeds for the obstacles
                for obstacle_num in range(num_obstacles):
                    obstacle_position = (random.randint(30, window_size[0] - obstacle_image.get_width()),
                                         random.randint(-600, -100))
                    obstacle_speed2 = random.uniform(0.2, 0.6)
                    obstacles.append([obstacle_image, obstacle_position, obstacle_speed2])
                # Reset the background
                global bg_pos
                bg_pos = [0, -300]
                global bg_pos2
                bg_pos2 = [0, -bg_image.get_height() - 300]
                # reset character position
                global character_pos
                character_pos = (window_size[0] / 2, window_size[1] - character_image.get_height() - 5)
                # reset character speed
                global character_speed
                global character_speed_y
                global character_direction
                global character_direction_y
                global bg_speed
                character_speed = default_speed
                character_speed_y = default_speed_y
                character_direction = 'stay'
                character_direction_y = 'stay'
                bg_speed = 0.3


# Create a new list to hold laser beam positions and speeds
laser_beams = []

# Load the laser beam image
laser_beam_image = pygame.image.load('laser_beam.png')

# Set the speed of the laser beams
laser_beam_speed = 7

# Show start screen
start_screen()

# Main game loop
while running:
    # Clear the screen
    screen.fill((0, 0, 0))

    # Limit the frame rate to 120 FPS
    clock.tick(120)

    # Check if the counter has reached the time interval
    if counter % 30 == 0 and not score == 0:
        # Increase the speed of the obstacles
        for obstacle in obstacles:
            obstacle[2] += speed_increment
        character_speed += speed_increment
        character_speed_y += speed_increment
        bg_speed += speed_increment

    # Check for events
    for event in pygame.event.get():
        # Quit the game if the user closes the window
        if event.type == pygame.QUIT:
            running = False
        # Update the direction of the character based on the arrow keys
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                character_direction = 'left'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                character_direction = 'right'
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                character_direction_y = 'up'
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                character_direction_y = 'down'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Append a new laser beam to the list with the current character position
                    laser_beams.append(
                        [laser_beam_image, (character_pos[0] + character_image.get_width() / 2, character_pos[1]),
                         laser_beam_speed])
                    if character_speed > 0:
                        character_speed -= (100 * speed_increment)
                        character_speed_y -= (100 * speed_increment)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if character_direction != 'right':
                    character_direction = 'stay'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if character_direction != 'left':
                    character_direction = 'stay'
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                if character_direction_y != 'down':
                    character_direction_y = 'stay'
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if character_direction_y != 'up':
                    character_direction_y = 'stay'
        # Move the character based on the direction
    if character_direction == 'right':
        # Calculate the new position of the character
        new_pos = (character_pos[0] + character_speed, character_pos[1])
        # Check if the new position is within the boundaries of the screen
        if new_pos[0] + character_image.get_width() < window_size[0]:
            character_pos = new_pos
    elif character_direction == 'left':
        # Calculate the new position of the character
        new_pos = (character_pos[0] - character_speed, character_pos[1])
        # Check if the new position is within the boundaries of the screen
        if new_pos[0] > 0:
            character_pos = new_pos
    elif character_direction_y == 'up':
        # Calculate the new position of the character
        new_pos = (character_pos[0], character_pos[1] - character_speed_y)
        # Check if the new position is within the boundaries of the screen
        if new_pos[1] > 0:
            character_pos = new_pos
    elif character_direction_y == 'down':
        # Calculate the new position of the character
        new_pos = (character_pos[0], character_pos[1] + character_speed_y)
        # Check if the new position is within the boundaries of the screen
        if new_pos[1] + character_image.get_height() < window_size[1]:
            character_pos = new_pos

    # Move the obstacle down
    for obstacle in obstacles:
        obstacle[1] = (obstacle[1][0], obstacle[1][1] + obstacle[2])

        # Check if the obstacle has reached the bottom of the screen
        if obstacle[1][1] > window_size[1]:
            # Reset the position of the obstacle
            obstacle[1] = (random.randint(30, window_size[0] - obstacle_image.get_width()), 0)

        # Create rectangles for character and obstacle
        character_rect = pygame.Rect(character_pos[0], character_pos[1], character_image.get_width() - 5,
                                     character_image.get_height() - 5)
        obstacle_rect = pygame.Rect(obstacle[1][0], obstacle[1][1], obstacle_image.get_width() - 5,
                                    obstacle_image.get_height() - 5)

        if character_rect.colliderect(obstacle_rect):
            # Game over Screen by Collision
            game_over_screen(score)
            # Reset the score
            score = 0
            # Show the start screen
            start_screen()
            print("collision detected!")
            print("Your Score was: " + str(score))
            break

    # Update the position of the laser beams
    for laser_beam in laser_beams:
        x, y = laser_beam[1]
        y -= laser_beam[2]
        laser_beam[1] = (x, y)

    # Add collision detection for laser beams and obstacles
    for obstacle in obstacles:
        for laser_beam in laser_beams:
            if laser_beam[1][0] < obstacle[1][0] + obstacle_image.get_width() and \
                    laser_beam[1][0] + laser_beam_image.get_width() > obstacle[1][0] and \
                    laser_beam[1][1] < obstacle[1][1] + obstacle_image.get_height() and \
                    laser_beam[1][1] + laser_beam_image.get_height() > obstacle[1][1]:
                # Remove the obstacle and increase the score
                obstacle[1] = (random.randint(30, window_size[0] - obstacle_image.get_width()), 0)
                score += 10
                character_speed += (110 * speed_increment)
                character_speed_y += (110 * speed_increment)
                laser_beams.remove(laser_beam)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Move the backgrounds
    bg_pos[1] += bg_speed
    bg_pos2[1] += bg_speed

    # Check if the main background image has gone off the screen
    if bg_pos[1] > bg_image.get_height():
        # Move the main background image back to the top
        bg_pos[1] = -bg_image.get_height()
    # Check if the copy of the background image has gone off the screen
    if bg_pos2[1] > bg_image.get_height():
        # Move the copy of the background image back to the top
        bg_pos2[1] = -bg_image.get_height()

    # Render the background images
    screen.blit(bg_image, bg_pos)
    screen.blit(bg_image2, bg_pos2)
    # Draw the character
    screen.blit(character_image, character_pos)

    # Draw the laser beams on the screen
    for laser_beam in laser_beams:
        screen.blit(laser_beam[0], laser_beam[1])

    # Draw the obstacles

    for obstacle in obstacles:
        screen.blit(obstacle[0], obstacle[1])

    # Increment the score every 100 milliseconds
    current_time = pygame.time.get_ticks()
    if current_time - last_increment_time >= 100:
        score += 1
        last_increment_time = current_time

    # Render the score
    score_text = font.render("Score: " + str(score), True, (0, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
