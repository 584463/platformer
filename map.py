import pygame
import pygame.sprite
from enemy import Enemy

class Object(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width=30, height=30):
        super().__init__()
        self.screen = game.screen
        self.rect = pygame.Rect(x,y, width, height)
        self.color = "Red"

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Map:
    def __init__(self, game):
        self.map_objects = pygame.sprite.Group()
        self.check_point_x = 0
        self.settings = game.settings

    def load_level(self, level, game, offset=0):
        self.map_objects.empty()
        if level == 1:

            self.map_objects.add(Object(game, 0, 700, 400, 10))
            self.map_objects.add(Object(game, 1000, 600, 400, 10))
            self.map_objects.add(Object(game, 2000, 300, width= 100 ,height= 500))
            self.map_objects.add(Object(game, 2700, 600, 400, 10))
            self.map_objects.add(Object(game, 3000, 300, height= 500))
            self.map_objects.add(Object(game, 3800, 200, 400, 10))
            self.map_objects.add(Object(game, 4500, 300, height= 500))
            self.map_objects.add(Object(game, 5000, 200, 400, 10))
            self.map_objects.add(Object(game, 5700, 200, 400, 10))
            self.map_objects.add(Object(game, 6400, 400, height= 400))
            self.map_objects.add(Object(game, 6900, 600, 400, 10))

            enemy = Enemy(game, 200, 300)
            game.enemies.add(enemy)
            

            for object in self.map_objects.sprites():
                object.rect.x += offset
            
            


    def draw(self):
        for object in self.map_objects:
            object.draw()