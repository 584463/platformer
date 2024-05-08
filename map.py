import pygame
import pygame.sprite

class Object(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width=100, height=100):
        super().__init__()
        self.screen = game.screen
        self.rect = pygame.Rect(x,y, width, height)
        self.color = "#89CFF0"

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Map:
    def __init__(self):
        self.map_objects = pygame.sprite.Group()

    def load_level(self, level, game):
        if level == 1:
            floor1 = Object(game, 0, 700, 400, 10)
            floor2 = Object(game, 500, 600, 400, 10)
            block1 = Object(game, 900, 400, height=500)
            self.map_objects.add(floor1)
            self.map_objects.add(floor2)
            self.map_objects.add(block1)

    def draw(self):
        for object in self.map_objects:
            object.draw()