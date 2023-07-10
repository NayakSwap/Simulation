import pygame
import numpy as np
import random

#Store Ball Variables
class Ball:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.colour = pygame.Color(0)
        self.colour.hsva = (random.randint(0, 255),random.randint(0, 100),100, 100)
    
    def Physics_Update(self, dt):
        self.position += self.velocity * dt
        self.velocity += self.acceleration * dt
    
    def Override(self, position, velocity):
        self.position = position
        self.velocity = velocity
    
    def give_x(self):
        return self.position
    
    def give_v(self):
        return self.velocity
    
    def color(self):
        return self.colour

#Declare Custom Variables

number_of_balls = 25
radius = 25
FPS = 48
timesteps = 2
acceleration = np.array([0,0])
coefficient_of_restitution = 1

Balls = []
for x in range(number_of_balls):
    Balls.append(Ball(np.random.randint(900, size=2).astype(float), np.random.randint(900, size=2).astype(float), acceleration))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("03-Particle_Simulation")
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
    for x in range(number_of_balls):
        pygame.draw.circle(screen, Balls[x].color(), Balls[x].give_x().astype(int), radius)
        for y in range(timesteps):
            Balls[x].Physics_Update(1/(FPS*timesteps))
            #Check Boundary Condition
            if Balls[x].give_x()[0]>(screen.get_width()-radius): Balls[x].Override(np.array([(screen.get_width()-radius), Balls[x].give_x()[1]]), np.array([ Balls[x].give_v()[0] * -coefficient_of_restitution , Balls[x].give_v()[1] ]))
            if Balls[x].give_x()[0]<radius: Balls[x].Override(np.array([radius, Balls[x].give_x()[1]]), np.array([ Balls[x].give_v()[0] * -coefficient_of_restitution , Balls[x].give_v()[1] ]))
            if Balls[x].give_x()[1]>(screen.get_height()-radius): Balls[x].Override(np.array([Balls[x].give_x()[0], screen.get_height()-radius]), np.array([ Balls[x].give_v()[0] , Balls[x].give_v()[1] * -coefficient_of_restitution ]))
            if Balls[x].give_x()[1]<radius: Balls[x].Override(np.array([Balls[x].give_x()[0],radius]), np.array([ Balls[x].give_v()[0] , Balls[x].give_v()[1] * -coefficient_of_restitution ]))
            #Collision Handling
            for z in range(x+1,number_of_balls):
                Distance = np.linalg.norm(Balls[z].give_x() - Balls[x].give_x())
                overlap = (2 * radius) - Distance
                if overlap>0:
                    direction = (Balls[z].give_x() - Balls[x].give_x())/Distance
                    tangent1 = np.dot(direction, Balls[x].give_v()) * direction
                    tangent2 = np.dot(direction, Balls[z].give_v()) * direction
                    normal1 = Balls[x].give_v() - tangent1
                    normal2 = Balls[z].give_v() - tangent2
                    Balls[x].Override( Balls[x].give_x() - direction*overlap/2 , normal1 + tangent2 * coefficient_of_restitution )
                    Balls[z].Override( Balls[z].give_x() + direction*overlap/2 , normal2 + tangent1 * coefficient_of_restitution )
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(FPS)  # limits FPS

pygame.quit()