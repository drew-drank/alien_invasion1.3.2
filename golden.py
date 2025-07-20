import pygame
from pygame.sprite import Sprite
from random import randint

class Rain(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.rain_color
        self.screen_rect = ai_game.screen.get_rect()

        self.rect = pygame.Rect(0,0, self.settings.rain_width,self.settings.rain_height)
        self.rect.midtop = self.screen_rect.midtop
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    def update(self):
        self.y += self.settings.rain_speed
        self.rect.y = self.y

    def x_update(self):
        self.x = randint(1,1920)
        self.rect.x = self.x

    def draw_rain(self):
        pygame.draw.rect(self.screen, self.color, self.rect)        
