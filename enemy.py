from player import Player

class Enemy(Player):
    def __init__(self,game, x, y):
        super().__init__(game)

        self.x = x
        self.y = y
        self.color = "Red"
        self.rect.topleft = (x, y)
        self.moving_left = True
        self.speed = 1
        

    