import pygame
import pygame.sprite

class Object(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width=100, height=100):
        super().__init__()
        self.screen = game.screen
        self.rect = pygame.Rect(x,y, width, height)
        self.color = "Red"

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Map:
    def __init__(self):
        self.map_objects = pygame.sprite.Group()

    def load_level(self, level, game):
        self.map_objects.empty()
        if level == 1:

            self.map_objects.add(Object(game, 0, 700, 400, 10))
            self.map_objects.add(Object(game, 500, 600, 400, 10))
            self.map_objects.add(Object(game, 900, 300, height= 500))
            self.map_objects.add(Object(game, 1200, 600, 400, 10))
            self.map_objects.add(Object(game, 2000, 300, height= 500))
            self.map_objects.add(Object(game, 2300, 200, 400, 10))
            self.map_objects.add(Object(game, 3000, 300, height= 500))
            self.map_objects.add(Object(game, 3200, 200, 400, 10))
            self.map_objects.add(Object(game, 3400, 200, 400, 10))
            self.map_objects.add(Object(game, 3800, 400, height= 500))

    def draw(self):
        for object in self.map_objects:
            object.draw()