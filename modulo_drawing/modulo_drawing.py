import pygame
import math
from sys import argv


def calculate_next_x(radius, angle):
    return radius * math.sin(math.radians(angle)) + circle_x

def calculate_next_y(radius, angle):
    return radius * math.cos(math.radians(angle)) + circle_y

def coordinates_points():
    points = [{'x': 0, 'y': 0} for i in range(nb_points)]
    degree_between_points = 360 / nb_points
    for i in range(nb_points):
        points[i]['x'] = calculate_next_x(circle_r, degree_between_points * i)
        points[i]['y'] = calculate_next_y(circle_r, degree_between_points * i)
    return points


nb_points = int(argv[1])
factor = int(argv[2])

# PyGame setup
pygame.init()

size = [800, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Modulo drawing")

WHITE = (255, 255, 255)
GREY = (84, 84, 84)

circle_x = 400
circle_y = 400
circle_r = 300

done = False
while not done:
    # Check if the user closed the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clean the screen
    screen.fill(WHITE)

    # Draw the main circle
    pygame.draw.circle(screen, GREY, [circle_x, circle_y], circle_r, 1)

    # Draw the chords
    points = coordinates_points()
    for i in range(nb_points):
        a = (points[i]['x'], points[i]['y'])
        b = (   points[i * factor % nb_points]['x'],
                points[i * factor % nb_points]['y'])
        pygame.draw.line(screen, GREY, a, b)

    # Update the screen
    pygame.display.flip()

pygame.quit()
