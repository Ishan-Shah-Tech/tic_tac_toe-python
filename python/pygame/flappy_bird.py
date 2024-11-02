import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# Set up character
character_width, character_height = 250, 250
character_x, character_y = (width - character_width) // 2, (height - character_height) // 2
character_speed = 5
jump_strength = 15

# Set up gravity
gravity = 1
fall_speed = 0

# Load character texture
character_texture = pygame.image.load(r"C:\Users\Kunal\OneDrive\Documents\Librasprite Drawings\Image form\Bird.png")
character_texture = pygame.transform.scale(character_texture, (character_width, character_height))

# Main game loop
clock = pygame.time.Clock()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Jump when the space key is pressed
            fall_speed = -jump_strength
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Jump when the screen is clicked
            fall_speed = -jump_strength

    # Get key states
    keys = pygame.key.get_pressed()

    # Update character position based on key states
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and character_x > 0:
        character_x -= character_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and character_x < width - character_width:
        character_x += character_speed

    # Apply gravity
    fall_speed += gravity
    character_y += fall_speed

    # Check if the character is on the ground
    if character_y > height - character_height:
        character_y = height - character_height
        fall_speed = 0  # Stop falling when on the ground

    # Draw background
    screen.fill((255, 255, 255))

    # Draw character with texture
    screen.blit(character_texture, (character_x, character_y))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
