from random import uniform
from ship import Ship
class Shield(Ship):
    def init(self,ai_game):
        super().__init__()
        self.image = pygame.image.load('images/shield.bmp')
    def update(self):
        self.x = uniform(0,ai_game.settings.screen_width)
