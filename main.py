import pygame
from settings import Settings
from map import Map
from player import Player

class Game:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1500,1000))
        pygame.display.set_caption("Platformer")
        self.map = Map()
        self._load_level()
        self.player = Player(self)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.player.moving_right = True
                    if event.key == pygame.K_a:
                        self.player.moving_left = True
                    if event.key == pygame.K_SPACE:
                     self.player.jump()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.player.moving_right = False
                    if event.key == pygame.K_a:
                        self.player.moving_left = False
                

            #Update
            self.player.update()


            #Draw Screen
            self.screen.fill(self.settings.bg_color)
            self.map.draw()
            self.player.draw()
            self._check_collisions()
            pygame.display.flip()

    def _load_level(self):
        self.map.load_level(1, self)

    def _check_collisions(self):
        collisions = pygame.sprite.spritecollideany(self.player, self.map.map_objects)
        if collisions:
            if self.player.y_acc > 0     and self.player.falling:
                self.player.rect.bottom = collisions.rect.top
                self.player.landed()
            elif self.player.y_acc < 0 and self.player.falling:
                self.player.rect.top = collisions.rect.bottom
                self.player.y_acc = 0

        else:
            self.player.falling = True

game = Game()
game.run()