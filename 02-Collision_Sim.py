import pygame
import numpy as np

#Define Variables
position1 = np.array([40.0,80.0])    #Initial position1
radius1 = 70                         #radius1
velocity1 = np.array([400.0,50.0])    #initial velocity1
position2 = np.array([900.0,80.0])   #Initial position2
radius2 = 70                         #radius2
velocity2 = np.array([500.0,0.0])    #initial velocity2
acceleration = np.array([0.0,2000.0]) #acceleration
coefficient_of_restitution = 0.9
FPS = 60
timesteps=2                           #the dt in x += v.dt
rounded_pos1 = position1.astype(int)  #you can't use floats as inputs for pygame.draw
rounded_pos2 = position2.astype(int)  #you can't use floats as inputs for pygame.draw


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("02-Collision_Sim")
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
    pygame.draw.circle(screen, "red", rounded_pos1, radius1)
    pygame.draw.circle(screen, "red", rounded_pos2, radius2)
    for x in range(timesteps):
        #Ball1
        position1 += velocity1 * (1/(FPS*timesteps))
        velocity1 += acceleration * (1/(FPS*timesteps))
            #Boundary Conditions
        if position1[0]>(screen.get_width()-radius1):
            position1[0]=(screen.get_width()-radius1)
            velocity1[0] *= -coefficient_of_restitution
        if position1[0]<radius1:
            position1[0]=radius1
            velocity1[0] *= -coefficient_of_restitution
        if position1[1]>(screen.get_height()-radius1):
            position1[1]=(screen.get_height()-radius1)
            velocity1[1] *= -coefficient_of_restitution
        if position1[1]<radius1:
            position1[1]=radius1
            velocity1[1] *= -coefficient_of_restitution
        #Ball2
        position2 += velocity2 * (1/(FPS*timesteps))
        velocity2 += acceleration * (1/(FPS*timesteps))
            #Boundary Conditions
        if position2[0]>(screen.get_width()-radius2):
            position2[0]=(screen.get_width()-radius2)
            velocity2[0] *= -coefficient_of_restitution
        if position2[0]<radius2:
            position2[0]=radius2
            velocity2[0] *= -coefficient_of_restitution
        if position2[1]>(screen.get_height()-radius2):
            position2[1]=(screen.get_height()-radius2)
            velocity2[1] *= -coefficient_of_restitution
        if position2[1]<radius2:
            position2[1]=radius2
            velocity2[1] *= -coefficient_of_restitution
        #Collsion Handling
        Distance = np.linalg.norm(position2-position1)  #   np.linalg.norm(v) gives the length of v
        overlap = (radius1 + radius2) - Distance         
        if overlap>0:
            direction = (position2-position1)/Distance
            tangent1 = np.dot(direction, velocity1) * direction
            tangent2 = np.dot(direction, velocity2) * direction
            normal1 = velocity1 - tangent1
            velocity1 = normal1 + tangent2 * coefficient_of_restitution
            normal2 = velocity2 - tangent2
            velocity2 = normal2 + tangent1 * coefficient_of_restitution
            position1 -= direction*(overlap/2)
            position2 += direction*(overlap/2)
    rounded_pos1 = position1.astype(int)
    rounded_pos2 = position2.astype(int)

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(FPS)  # limits FPS

pygame.quit()