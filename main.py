import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroid, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group)
    asteroid_field = AsteroidField()




    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)
        for asteroid_obj in asteroid:
            if player.check_collision(asteroid_obj):
                print("Game over!")
                import sys
                sys.exit()
        for asteroid_obj in asteroid:
            for shot_obj in shots_group:
                if asteroid_obj.check_collision(shot_obj):
                    asteroid_obj.split()
                    shot_obj.kill()
    
            
        screen.fill("black")
        for item in drawable:
            item.draw(screen)

        for shot in shots_group:
            shot.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

   

    
if __name__ == "__main__":
    main()