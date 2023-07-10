#Example file showing a basic pygame "game loop"
import pygame
import numpy as np

#Define Variables
position = np.array([40.0,40.0])    #Initial position
radius = 10                         #Radius
velocity = np.array([150.0,20.0])    #initial velocity
acceleration = np.array([0.0,2000.0]) #acceleration
coefficient_of_restitution = 1
FPS = 48
timesteps=5                         #the dt in x += v.dt
rounded_pos = position.astype(int)  #you can't use floats as inputs for pygame.draw

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("01-Moving_Ball_uniform_velocity")
clock = pygame.time.Clock()
running = True

#MainLoop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "red", rounded_pos, radius)
    for x in range(timesteps):
        velocity += acceleration * (1/(FPS*timesteps))
        prev_pos = np.array(position)
        position += velocity * (1/(FPS*timesteps))
        velocity = (position - prev_pos) * FPS * timesteps
        if (position[0]>(screen.get_width()-radius) and velocity[0]>0) or (position[0]<radius and velocity[0]<0): velocity[0] *= -coefficient_of_restitution
        if (position[1]>(screen.get_height()-radius) and velocity[1]>0) or (position[1]<radius and velocity[1]<0): velocity[1] *= -coefficient_of_restitution
    rounded_pos = position.astype(int)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 25

pygame.quit()