class Settings:
    def __init__(self):
        #屏幕设置
        self.screen_width = 1300
        self.screen_height = 800
        

        #子弹
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250,250,250)

        #雨滴
        self.rain_width =  4
        self.rain_height = 15
        self.rain_color = (255,215,0)
        self.rain_speed = 10.5
        self.rain_points = 1000

        

        #外星人
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
        self.ab_color = (0,250,154)
        
        #飞船
        self.ship_speed = 20.5
        self.ship_limit = 3

        #版本
        self.v = '1.3.3'
        
        #加快游戏节奏
        self.speedup_scale = 1.3
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.bullet_speed = 7.5
        self.alien_speed = 20.5
        self.ship_speed = 20.5
        self.fleet_direction = 1
        self.alien_points = 50
        self.ship_full_blood = 100
        self.ship_blood = self.ship_full_blood
        

    def increase_speed(self):
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.ship_full_blood *= self.speedup_scale
        self.ship_blood *= self.speedup_scale
        

        self.alien_points = int(self.alien_points * self.speedup_scale)
