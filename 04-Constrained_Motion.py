import pygame
import numpy as np
import math

#Define Variables
Radius_Big = 250                        #Initial position (Radius)
Angle = 90                              #Initial position (angle)
radius_smol = 50                        #Radius
velocity = np.array([700.0,0.0])        #initial velocity
acceleration = np.array([0.0,2000.0])   #acceleration
FPS = 48
timesteps=5                             #the dt in x += v.dt

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("04-Constrained_Motion")
clock = pygame.time.Clock()
running = True

center = np.array([screen.get_width()/2 , screen.get_height()/2])

position = np.array([center[0] + Radius_Big * math.cos(Angle),center[1] + Radius_Big * math.sin(Angle)])
rounded_pos = position.astype(int)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "gray", center, Radius_Big + 1)
    pygame.draw.circle(screen, "black", center, Radius_Big - 1)
    pygame.draw.circle(screen, "red", rounded_pos, radius_smol)
    for x in range(timesteps):
        prev_pos = np.array(position)
        
        velocity += acceleration * (1/(FPS*timesteps))
        position += velocity * (1/(FPS*timesteps))
        rounded_pos = position.astype(int)
        #Constraint
        relative_position = position - center
        
        
        if(np.linalg.norm(relative_position) != Radius_Big):
            position = center + relative_position * (Radius_Big/np.linalg.norm(relative_position))
        velocity = (position - prev_pos) * FPS * timesteps

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 25

pygame.quit()