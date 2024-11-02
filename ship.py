import pygame

from settings import Settings
from pygame.sprite import Sprite

class Ship(Sprite):
    """管理飞船的类"""
    def __init__(self,ai_game):
        super().__init__()
        """初始化飞船并设置其初始位置"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #每艘新飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        #移动标志（飞船一开始不移动）
        self.moving_right = False
        self.moving_left = False

        

    def update(self):
        """根据移动标志调准飞船位置"""
        if self.moving_right and self.rect.right + self.settings.ship_speed < self.screen_rect.right:
            if self.ai_game.isfullscreen:
                self.rect.x += self.settings.ship_speed
            else:
                if self.moving_right and self.rect.right + self.settings.ship_speed < 1300:
                    self.rect.x += self.settings.ship_speed

        
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        if self.rect.left < 0:
            self.rect.x = 0

        self.x = self.rect.x 
            
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen.get_rect.midbottom
        self.x = float(self.rect.x)
