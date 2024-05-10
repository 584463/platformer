import pygame.sprite

class Player(pygame.sprite.Sprite):
    """A class to manage the player sprite"""

    def __init__(self, game) -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = "Red"
        self.rect = pygame.Rect(0,0,10,30)
        self.y_acceleration = 0
        self.falling = True
        self.moving_left = self.moving_right = False
        self.jump_count = 0
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        #Change to blit if you want to use an image

    def update(self):
        
        self.rect.y += self.y_acceleration * 1
        if self.falling: 
            self.y_acceleration += 1
        
        


    def landed(self):
        self.falling = False
        self.y_acceleration = 0
        self.jump_count=0
        

    def move(self, map):

        if self.moving_right and not self.collide("right", map.map_objects):
            self.rect.x += self.settings.player_speed
        if self.moving_left and not self.collide("left", map.map_objects) and self.rect.left > 0:
            self.rect.x -= self.settings.player_speed

 
    def jump(self):
        if self.jump_count <= 1:
            self.jump_count += 1
            self.y_acceleration = -20 #Testing
            self.falling = True

    def collide(self, direction, objects):
        if direction == "right":
            vel = self.settings.player_speed
            print(direction)
        elif direction == "left":
            vel = -self.settings.player_speed

        self.rect.x += vel
        
        collided_object = None
        for obj in objects:
            if pygame.sprite.spritecollideany(self, objects):
                collided_object = obj
                
                break
        self.rect.x -= vel
        
        return collided_object