from circleshape import *
from constants import *
from shot import *
from main import *
PLAYER_SHOT_COOLDOWN = 0.3
class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__( x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.timer = 0

    def triangle(self):
        """
        defines player position :
        returns list of a, b, c
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
       self.rotation += (PLAYER_TURN_SPEED * dt) 

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
                self.timer = PLAYER_SHOT_COOLDOWN

        self.timer -= dt
        if self.timer < 0:
            self.timer = 0
    
    def shoot(self):
        velocity = pygame.Vector2(0,1).rotate(self.rotation)
        velocity = velocity * PLAYER_SHOOT_SPEED
        new_shot = Shot(self.position.x, self.position.y, velocity)
        self.shots_group.add(new_shot)
    
