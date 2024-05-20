import pygame.sprite

class Player(pygame.sprite.Sprite):
    """A class to manage the player sprite"""

    def __init__(self, game) -> None:
        super().__init__()
        self.respawn_x = 0
        self.respawn_y = 0
        self.screen = game.screen
        self.settings = game.settings
        self.color = "White"
        self.rect = pygame.Rect(0,0,self.settings.player_width,30)
        self.rect.topleft = (0, 500)
        self.y_acceleration = 0
        self.falling = True
        self.moving_left = self.moving_right = False
        self.jump_count = 0
        self.speed = self.settings.player_speed
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        #Change to blit if you want to use an image

    def update(self, map):
        
        if self.falling:
            self.rect.y += self.y_acceleration

            self.y_acceleration += 1
        self._check_collisions(map)
        
        


    def landed(self):
        self.falling = False
        self.y_acceleration = 0
        self.jump_count=0
        

    def move(self, map):

        if self.moving_right and not self.collide("right", map.map_objects):
            self.rect.x += self.speed
        if self.moving_left and not self.collide("left", map.map_objects) and self.rect.left > 0:
            self.rect.x -= self.speed

 
    def jump(self):
        if self.jump_count < self.settings.jump_limit:
            self.jump_count += 1
            self.y_acceleration = -20 #Testing
            self.falling = True

    def collide(self, direction, objects):
        if direction == "right":
            vel = self.speed

        elif direction == "left":
            vel = -self.speed

        self.rect.x += vel
        
        collided_object = None
        for obj in objects:
            if pygame.sprite.spritecollideany(self, objects):
                collided_object = obj
                
                break
        self.rect.x -= vel
        
        return collided_object
    
    def respawn(self, game):
        self.rect.topleft = (self.respawn_x, self.respawn_y)
        self.y_acceleration = 0
        self.jump_count = 0
        game.vertical_tracker = 0


    def _check_collisions(self, map):
        collisions = pygame.sprite.spritecollideany(self, map.map_objects)
        print(collisions)
        if collisions:
            if self.y_acceleration > 0 and self.falling: #aka moving down
                self.rect.bottom = collisions.rect.top  
                self.landed()          

            elif self.y_acceleration < 0 and self.falling: #Hit our head
                self.rect.top = collisions.rect.bottom
                self.y_acceleration = 0
            
        else:
            self.falling = True