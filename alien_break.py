import pygame
from pygame.sprite import Sprite
from random import randint
class AlienBreak(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.ab_color

        self.rect = pygame.Rect(0,0, self.settings.bullet_width,self.settings.bullet_height)
        
        for alien in ai_game.aliens.sprites():
            self.rect.top = alien.rect.top
            
            
            
        self.y = float(self.rect.y)

        self.x = float(self.rect.x) 

    def update(self):
        self.y += self.settings.bullet_speed
        self.rect.y = self.y

    def x_update(self):
        self.x = randint(1,1200)
        self.rect.x = self.x
    

    def draw_ab(self):
        pygame.draw.rect(self.screen, self.color, self.rect)        

