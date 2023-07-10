import pygame
import numpy as np

#Define Variables
spring_len = 100
radius = 10
acceleration = np.array([0.0,2000.0])
FPS = 48
stiffness = 2000
bottom_pos = np.array([640.0,50.0])
bottom_vel = np.array([0.0,0.0])
top_vel = np.array([0.0,0.0])
top_pos = np.array([640.0,50.0 + spring_len])
acceleration = np.array([0.0,1500.0])
timesteps = 500

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("07-08-Vertical_Coupled_Spring_Mass_System")
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
    pygame.draw.circle(screen, "red", bottom_pos.astype(int), radius)
    pygame.draw.circle(screen, "red", top_pos.astype(int), radius)

    for x in range(timesteps):
        center_of_mass = np.array((bottom_pos + top_pos) / 2)
        bottom_vel += acceleration * (1/(FPS*timesteps))
        bottom_prev_pos = np.array(bottom_pos)
        bottom_pos += bottom_vel * (1/(FPS*timesteps))
        bottom_pos += (bottom_pos - [center_of_mass[0],center_of_mass[1] - spring_len/2]) * -1 * (stiffness/(stiffness+((FPS*timesteps)**2)))   #Soft Constraint
        bottom_vel = np.array((bottom_pos - bottom_prev_pos) * (FPS*timesteps))
        top_vel += acceleration * (1/(FPS*timesteps))
        top_prev_pos = np.array(top_pos)
        top_pos += top_vel * (1/(FPS*timesteps))
        top_pos += (top_pos - [center_of_mass[0],center_of_mass[1] + spring_len/2]) * -1 * (stiffness/(stiffness+((FPS*timesteps)**2)))         #Soft Constraint
        top_vel = np.array((top_pos - top_prev_pos) * (FPS*timesteps))
        if top_pos[1] > 710:                    #Ground Collision
            top_pos[1] = 710
            top_vel *= -1

    pygame.display.flip()
    clock.tick(FPS)  # limits FPS

pygame.quit()