import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
            pygame.draw.circle(screen, (255,255,255), (self.position), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill() 
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            radius = self.radius - ASTEROID_MIN_RADIUS
            velocity1 = self.velocity.rotate(angle)  # rotate one way
            velocity2 = self.velocity.rotate(-angle) # rotate other way     
            new1 = Asteroid(self.position.x, self.position.y, radius)
            new1.velocity = velocity1 * 1.2
            new2 = Asteroid(self.position.x, self.position.y, radius)
            new2.velocity = velocity2 * 1.2

