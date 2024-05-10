import pygame
from settings import Settings
from map import Map
from player import Player

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1500,1000))
        pygame.display.set_caption("Platformer")
        self.map = Map()
        self._load_level()
        self.player = Player(self)
        self.running = True

    def run(self):
        while self.running:

            #Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.moving_right = True

                            
                            
                    if event.key == pygame.K_LEFT:
                        self.player.moving_left = True


                    if event.key == pygame.K_SPACE:
                        self.player.jump()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.player.moving_right = False
                    if event.key == pygame.K_LEFT:
                        self.player.moving_left = False

            #Update
            
            self.player.move(self.map)
            self.player.update()
            self._check_collisions()
            self.scroll()


            #Draw Screen
            self.screen.fill(self.settings.bg_color)
            self.map.draw()
            self.player.draw()
            pygame.display.flip()
            self.clock.tick(60)

    def _load_level(self):
        self.map.load_level(1, self)

        
    def _check_collisions(self):
        collisions = pygame.sprite.spritecollideany(self.player, self.map.map_objects)
        
        if collisions:
            if self.player.y_acceleration > 0 and self.player.falling: #aka moving down
                self.player.rect.bottom = collisions.rect.top  
                self.player.landed()

            elif self.player.y_acceleration < 0 and self.player.falling: #Hit our head
                self.player.rect.top = collisions.rect.bottom
                self.player.y_acceleration = 0


            
        else:
            self.player.falling = True


    def scroll(self):
        if (self.player.rect.x >= self.screen.get_rect().right - self.settings.scroll_offset)\
        and self.player.moving_right:
            self.player.rect.x -=self.settings.player_speed
            for object in self.map.map_objects:
                object.rect.x -= self.settings.player_speed
            

game = Game()
game.run()