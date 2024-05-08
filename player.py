import pygame.sprite

class Player(pygame.sprite.Sprite):
    """A class to manage the player sprite"""

    def __init__(self, game) -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = "Blue"
        self.rect = pygame.Rect(0,0,10,30)
        self.y_acc = 0
        self.falling = True
        self.jump_count = 0
        self.moving_left = self.moving_right = self.moving_up = False
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        #Change to blit if you want to use an image

    def update(self):
        self.rect.y += self.y_acc * .01
        if self.falling: 
            self.y_acc += 1


        self.move()


    def landed(self):
        self.falling = False
        self.y_acc = 0
        self.jump_count = 0


    def move(self):
        if self.moving_right:
            self.rect.x += self.settings.player_speed
        if self.moving_left:
            self.rect.x -= self.settings.player_speed
        if self.moving_up:
            self.rect.y -= self.settings.player_up

    def jump(self):
        if self.jump_count == 0:
            self.jump_count += 1
            self.y_acc = -200
        self.falling = True
