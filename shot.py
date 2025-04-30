from circleshape import *
from constants import *
import pygame 
SHOT_RADIUS = 5
class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
    def draw(self, surface):
        pygame.draw.circle(surface, "white", (self.position.x, self.position.y), self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt

