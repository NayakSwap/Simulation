import pygame
import numpy as np

#Define Variables
radius = 50                             #Radius
velocity1 = np.array([0.0,0.0])         #initial velocity
velocity2 = np.array([0.0,0.0])
acceleration = np.array([0.0,0.0])      #intial acceleration
FPS = 48
timesteps=50                             #the dt in x += v.dt
Amplitude = 500
Intercept = 200
position1 = np.array([float(640 - Amplitude),float(360 + Intercept)])
position2 = np.array([float(640 - Amplitude),float(360 - Intercept)])
stiffness = 4


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("07-Soft_Constraints_spring_mass_system")
clock = pygame.time.Clock()
running = True

#MainLoop
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "red", position1.astype(int), radius)
    pygame.draw.circle(screen, "red", position2.astype(int), radius)
    for x in range(timesteps):
        #Ball1
        velocity1 += acceleration * (1/(FPS*timesteps))
        position1 += velocity1 * (1/(FPS*timesteps))
        acceleration = (position1 - np.array([640.0,float(360 + Intercept)])) * -1 * stiffness      #Using Hooke's law
        prev_pos2 = np.array(position2)
        position2 += velocity2 * (1/(FPS*timesteps))
        position2 += (position2 - np.array([640.0,float(360 - Intercept)])) * -1 * (stiffness/(stiffness+((FPS*timesteps)**2)))     #Soft Constraint
        velocity2 = (position2 - prev_pos2) * FPS * timesteps
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(FPS)  # limits FPS

pygame.quit()