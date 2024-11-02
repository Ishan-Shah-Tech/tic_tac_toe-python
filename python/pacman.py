import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))

# define color
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)

# game speed
clock = pygame.time.Clock()

# packman and food position
pacman_position = [320, 240]
food_position = [random.randrange(1, 63)*10, random.randrange(1, 47)*10]
score = 0

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman_position[1] -= 10
            if event.key == pygame.K_DOWN:
                pacman_position[1] += 10
            if event.key == pygame.K_LEFT:
                pacman_position[0] -= 10
            if event.key == pygame.K_RIGHT:
                pacman_position[0] += 10

    # detect collision with food
    if pacman_position == food_position:
        score += 1
        food_position = [random.randrange(1, 63)*10, random.randrange(1, 47)*10]

    # draw packman and food
    pygame.draw.circle(screen, white, pacman_position, 5)
    pygame.draw.circle(screen, red, food_position, 5)

    # draw score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: %s" % score, True, white)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(30)