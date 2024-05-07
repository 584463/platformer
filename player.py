import pygame.sprite

class Player(pygame.sprite.Sprite):
    """A class to manage the player sprite"""

    def __init__(self, game) -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = "Blue"
        self.rect = pygame.Rect(0,0,10,30)
        self.fall_count = 0
        self.falling = True
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        #Change to blit if you want to use an image

    def update(self):
        self.rect.y += self.fall_count
        self.rect.x = 10
        if self.falling: 
            self.fall_count += .01 

        