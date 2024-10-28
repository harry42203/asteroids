import pygame
from circleshape import *
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen, color):
            pygame.draw.circle(screen, color, (self.position), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt