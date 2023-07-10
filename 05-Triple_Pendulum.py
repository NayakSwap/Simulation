import pygame
import numpy as np

radius = 15
pen_len = 100.0
acceleration = np.array([0.0,2000.0])
FPS = 48
timesteps = 50

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("05-Triple_Pendulum")
clock = pygame.time.Clock()
running = True

pivot_pos = np.array([screen.get_width()/2, (screen.get_height()/2 - 50)])
position1 = pivot_pos + np.array([pen_len,0.0])
position2 = position1 - np.array([0.0,pen_len])
position3 = position2 - np.array([0.0,pen_len])
velocity1 = np.array([0.0, 0.0])
velocity2 = np.array([0.0, 0.0])
velocity3 = np.array([0.0, 0.0])

position11 = pivot_pos + np.array([pen_len,0.1])
position21 = position11 - np.array([0.0,pen_len])
position31 = position21 - np.array([0.0,pen_len])
velocity11 = np.array([0.0, 0.0])
velocity21 = np.array([0.0, 0.0])
velocity31 = np.array([0.0, 0.0])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.line(screen, 'grey', pivot_pos, position1, 5)
    pygame.draw.line(screen, 'grey', position1, position2, 5)
    pygame.draw.line(screen, 'grey', position2, position3, 5)
    pygame.draw.circle(screen, "red", position1.astype(int), radius)
    pygame.draw.circle(screen, "red", position2.astype(int), radius)
    pygame.draw.circle(screen, "red", position3.astype(int), radius)

    pygame.draw.line(screen, 'grey', pivot_pos, position11, 5)
    pygame.draw.line(screen, 'grey', position11, position21, 5)
    pygame.draw.line(screen, 'grey', position21, position31, 5)
    pygame.draw.circle(screen, "blue", position11.astype(int), radius)
    pygame.draw.circle(screen, "blue", position21.astype(int), radius)
    pygame.draw.circle(screen, "blue", position31.astype(int), radius)
    

    #Timesteps Loop
    for n_dt in range(timesteps):
        #Simulate Ball1
        prev_pos1 = np.array(position1)
        velocity1 += acceleration * (1/(FPS*timesteps))
        position1 += velocity1 * (1/(FPS*timesteps))
        #Simulate Ball2
        prev_pos2 = np.array(position2)
        velocity2 += acceleration * (1/(FPS*timesteps))
        position2 += velocity2 * (1/(FPS*timesteps))
        #Simulate Ball3
        prev_pos3 = np.array(position3)
        velocity3 += acceleration * (1/(FPS*timesteps))
        position3 += velocity3 * (1/(FPS*timesteps))

        #Constraint1
        relative_position1 = position1 - pivot_pos
        if(np.linalg.norm(relative_position1) != pen_len): position1 = pivot_pos + relative_position1 * (pen_len/np.linalg.norm(relative_position1))
        #Contraint2
        relative_position2 = position2 - position1
        if(np.linalg.norm(relative_position2) != pen_len):
            position2 = (position1 + position2)/2 + relative_position2 * (pen_len/np.linalg.norm(relative_position2)) * 0.5
            position1 = (position1 + position2)/2 - relative_position2 * (pen_len/np.linalg.norm(relative_position2)) * 0.5
        #Contraint3
        relative_position3 = position3 - position2
        if(np.linalg.norm(relative_position3) != pen_len):
            position3 = (position2 + position3)/2 + relative_position3 * (pen_len/np.linalg.norm(relative_position3)) * 0.5
            position2 = (position2 + position3)/2 - relative_position3 * (pen_len/np.linalg.norm(relative_position3)) * 0.5
        #Update Velocities
        velocity1 = (position1 - prev_pos1) * FPS * timesteps
        velocity2 = (position2 - prev_pos2) * FPS * timesteps
        velocity3 = (position3 - prev_pos3) * FPS * timesteps

        #Simulate Ball1
        prev_pos11 = np.array(position11)
        velocity11 += acceleration * (1/(FPS*timesteps))
        position11 += velocity11 * (1/(FPS*timesteps))
        #Simulate Ball2
        prev_pos21 = np.array(position21)
        velocity21 += acceleration * (1/(FPS*timesteps))
        position21 += velocity21 * (1/(FPS*timesteps))
        #Simulate Ball3
        prev_pos31 = np.array(position31)
        velocity31 += acceleration * (1/(FPS*timesteps))
        position31 += velocity31 * (1/(FPS*timesteps))

        #Constraint1
        relative_position11 = position11 - pivot_pos
        if(np.linalg.norm(relative_position11) != pen_len): position11 = pivot_pos + relative_position11 * (pen_len/np.linalg.norm(relative_position11))
        #Contraint2
        relative_position21 = position21 - position11
        if(np.linalg.norm(relative_position21) != pen_len):
            position21 = (position11 + position21)/2 + relative_position21 * (pen_len/np.linalg.norm(relative_position21)) * 0.5
            position11 = (position11 + position21)/2 - relative_position21 * (pen_len/np.linalg.norm(relative_position21)) * 0.5
        #Contraint3
        relative_position31 = position31 - position21
        if(np.linalg.norm(relative_position31) != pen_len):
            position31 = (position21 + position31)/2 + relative_position31 * (pen_len/np.linalg.norm(relative_position31)) * 0.5
            position21 = (position21 + position31)/2 - relative_position31 * (pen_len/np.linalg.norm(relative_position31)) * 0.5
        #Update Velocities
        velocity11 = (position11 - prev_pos11) * FPS * timesteps
        velocity21 = (position21 - prev_pos21) * FPS * timesteps
        velocity31 = (position31 - prev_pos31) * FPS * timesteps
    
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 25

pygame.quit()