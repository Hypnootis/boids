import math

import pygame

WIDTH = 800
HEIGHT = 600
FPS = 60

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boids")
clock = pygame.time.Clock()

# Takes a tuple of vertices, then returns the coordinates of the centre
def polygon_centre(vertices):
    x_list = [vertex[0] for vertex in vertices]
    y_list = [vertex[1] for vertex in vertices]
    list_length = len(vertices)
    x_centre = sum(x_list) / list_length
    y_centre = sum(y_list) / list_length

    return (x_centre, y_centre)   # Return a tuple with the centre coordinates


def get_distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


class Boid():
    def __init__(self, position):
        self.position = position
        self.velocity = 0

    def nearest_neighbor(self, neighbors):
        shortest_distance = 0
        for i in neighbors:
            distances = []
            distance = get_distance(self.position, i.position)
            distances.append(distance)
            for j in distances:
                x = 10000
                if j < x:
                    x = j
                    shortest_distance = x
                else:
                    pass
        return shortest_distance

    def update(self, position, velocity, deltatime):
        self.velocity += velocity * deltatime
        self.position += position * deltatime


# Game loop
running = True
while running:

    # Process input/events
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Update

    # Render
    screen.fill(pygame.color.Color("cornflowerblue"))

    pygame.display.flip()

pygame.quit()
