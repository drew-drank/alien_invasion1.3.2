import pygame.font
from pygame.sprite import Group

from ship import Ship
class Scoreboard:

    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (250,250,250)
        self.font = pygame.font.SysFont("SimHei",30)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.prep_blood()
        
    def prep_score(self):
        rounded_score = round(self.stats.score,-1)
        score_str = f"得分:{rounded_score:,}"
        self.score_image = self.font.render(score_str,True,self.text_color,None)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        high_score = round(int(self.stats.high_score),-1)
        high_score_str = f"最高分:{high_score:,}"
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,None)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        level_str = f"等级:{str(self.stats.level)}"
        self.level_image = self.font.render(level_str,True,self.text_color,None)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right 
        self.level_rect.top = self.score_rect.bottom + 10
    def prep_blood(self):
        rounded_blood = int(self.ai_game.settings.ship_blood)
        rounded_full_blood = int(self.ai_game.settings.ship_full_blood)
        blood_str = f"剩余血量:{str(rounded_blood)}/{str(rounded_full_blood)}"
        self.blood_image = self.font.render(blood_str,True,self.text_color,None)

        self.blood_rect = self.level_image.get_rect()
        self.blood_rect.left = self.screen_rect.left 
        self.blood_rect.top = self.score_rect.bottom + 10
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
            
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.screen.blit(self.blood_image,self.blood_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
