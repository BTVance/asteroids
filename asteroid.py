from circleshape import *
from constants import *
import random
import pygame 


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, "white", (self.position.x, self.position.y), self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            angle = random.uniform(20,50)
            A1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS ))
            A2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS ))
            A1.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
            A2.velocity = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2






