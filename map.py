import pygame
import pygame.sprite
from enemy import Enemy

class Object(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width=30, height=30, color="Red"):
        super().__init__()
        self.screen = game.screen
        self.rect = pygame.Rect(x,y, width, height)
        self.color = color

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

            self.map_objects.add(Object(game, 0, 700, 400, 12))
            
            self.map_objects.add( Object(game, 500, 600, 300, 12))
            
            self.map_objects.add(Object(game, 1300, 300, 400, 12))
            
            self.map_objects.add(Object(game, 1700, 600, 500, 12)) 
           
            self.map_objects.add(Object(game, 3000, 200, 300, 12))
            
            self.map_objects.add(Object(game, 4900, 400, 300, 12))
            
            self.map_objects.add(Object(game, 6600, 400, 300, 12))

            self.map_objects.add(Object(game, 6000, 700, 400, 12))
            
            self.map_objects.add( Object(game,6700, 600, 300, 12))
            
            self.map_objects.add(Object(game, 7300, 300, 400, 12))
            
            self.map_objects.add(Object(game, 7700, 600, 500, 12)) 
           
            self.map_objects.add(Object(game, 8900, 600, 300, 12))
            
            self.map_objects.add(Object(game, 9500, 600, 300, 12))
            
            self.map_objects.add(Object(game, 10100, 800, 300, 12))
            
            self.map_objects.add( Object(game, 1000, 300,width=50 ,height= 310, color= pygame.Color("#ffffff")))

            self.map_objects.add(Object(game, 5700, 200,width=50 ,height= 500, color= pygame.Color("#ffffff")))

            self.map_objects.add(Object(game, 2700, 300,width=50 ,height= 490, color= pygame.Color("#ffffff")))

            self.map_objects.add(Object(game, 4000, 200,width=50 ,height= 500, color= pygame.Color("#ffffff")))

            self.map_objects.add( Object(game, 6700, 300,width=50 ,height= 310, color= pygame.Color("#ffffff")))

            self.map_objects.add(Object(game, 6000, 200,width=50 ,height= 500, color= pygame.Color("#ffffff")))

            self.map_objects.add(Object(game, 9000, 300,width=50 ,height= 490, color= pygame.Color("#ffffff")))

            self.map_objects.add(Object(game, 10000, 10,width=50 ,height= 730, color= pygame.Color("#ffffff")))

            enemy = Enemy(game, 200, 300)
            game.enemies.add(enemy)
            

            for object in self.map_objects.sprites():
                object.rect.x += offset
            
            


    def draw(self):
        for object in self.map_objects:
            object.draw()