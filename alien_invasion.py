from settings import Settings
v = Settings().v
print(f"坤星人入侵 v{v} on ",end='')

import sys
from time import sleep

import pygame


from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard
from golden import Rain
from alien_break import AlienBreak
from pathlib import Path
from music import Music


class AllenInvasion:
    def __init__(self):
        pygame.init()  
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        
        pygame.display.set_caption(f"坤星人入侵 v{self.settings.v}")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.music = Music()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.rain = pygame.sprite.Group()
        self.ab = pygame.sprite.Group()
        
        self._create_fleet()

        

        self.game_active = False
        self.play_button = Button(self,"开始")

        self.sb = Scoreboard(self)
        self.m = 0
        
        self.background=pygame.image.load(r"images\b.jpg")
        
        self.screen.blit(self.background,(0,0))
        
        
        
        self.music._check_background_music()
    def run_game(self):
          
            
        while True:
            self._check_events()
            
            
            if self.game_active:
                self.ship.update()
                self._update_ab()
                self._update_bullets()
                self._update_rain()
                self._update_aliens()
                self.cab()
                self.cr()
                self._check_blood()
                
                
            self._update_screen()
            self.clock.tick(60)
         

            
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydowm_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mp = pygame.mouse.get_pos()
                self._check_play_button(mp)

    def _check_play_button(self,mp):
        if self.play_button.rect.collidepoint(mp) and not self.game_active:
            self.stats_new_game()


    def stats_new_game(self):
        self.stats.reset_stats()
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
        self.game_active = True

        self.bullets.empty()
        self.aliens.empty()

        self._create_fleet()
        self.ship.center_ship()

            #隐藏光标
        pygame.mouse.set_visible(False)

        self.settings.initialize_dynamic_settings()
        

    def cr(self):
        
        if self.m % 5 == 0:
            self.rains()
            self.m += 1
        else:
            self.m+=1

                
    def rains(self):
        self._down_rain()
        for rain in self.rain.sprites():
            if rain.y == 0:
                rain.x_update()
            

    def _check_keydowm_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            if self.game_active:
                self.music._check_fire_music()
        elif event.key == pygame.K_q:
            exit()
        elif event.key == pygame.K_p:
            if not self.game_active:
                self.stats_new_game()
        
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        

    def _down_rain(self):
        new_rain = Rain(self)
        self.rain.add(new_rain)
    def _breaks(self):
        new_b = AlienBreak(self)
        self.ab.add(new_b)
    def _update_screen(self):
        
        
        self.screen.blit(self.background,(0,0))
        self.bullets.draw(self.screen)
        for rain in self.rain.sprites():
            rain.draw_rain()
        for ab in self.ab.sprites():
            ab.draw_ab()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()
            
        pygame.display.flip()
        self.clock.tick(60)

        
        

    def _update_bullets(self): 
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        self._check_bullet_rain_collisions()

    def _update_ab(self): 
        self.ab.update()
        for ab in self.ab.copy():
            if ab.rect.bottom >= self.settings.screen_height:
                self.ab.remove(ab)
        if pygame.sprite.spritecollideany(self.ship,self.ab):
            self.settings.ship_blood -= 2.5
            
            self.sb.prep_blood()
            self._check_blood()
            
                    
    def cab(self):
        self._breaks()
        for ab in self.ab.sprites():
            for alien in self.aliens.sprites():
                if ab.y == alien.rect.top:
                    ab.x_update()
    def _update_rain(self): 
        self.rain.update()

        for rain in self.rain.copy():
            if rain.rect.bottom >= self.settings.screen_height:
                self.rain.remove(rain)
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,False,True)
        
        

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
            self.sb.prep_blood()
            self.settings.ship_blood = self.settings.ship_full_blood

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points
                
            
            self.sb.prep_score()
            self.sb.check_high_score()
            self.sb.prep_high_score()
            
            self.music._check_break_music()
            
      
    def _check_bullet_rain_collisions(self):
        c = pygame.sprite.groupcollide(self.bullets,self.rain,True,True)

        if c:
            for rain in c.values():
                self.stats.score += self.settings.rain_points 
            self.sb.prep_score()
            self.sb.check_high_score()
            self.sb.prep_high_score()

    def _check_blood(self):
        if self.settings.ship_blood <= 0:
            self._ship_hit()

   
    def _create_fleet(self):
       alien = Alien(self)
       alien_width,alien_height = alien.rect.size

       current_x,current_y = alien_width,alien_height
       while current_y < (self.settings.screen_height - 3 * alien_height):
           while current_x < (self.settings.screen_width -  2 * alien_width):
               self._create_alien(current_x,current_y)
               current_x += 1.5 * alien_width

           current_x = alien_width
           current_y += 2 * alien_height

    def _create_alien(self,x_position,y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        self._check_fleet_edges() 
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.bullets.empty() 
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()
            
            self.settings.ship_blood = self.settings.ship_full_blood
            
            sleep(1)
            
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
            self.settings.ship_full_blood = 100
            self.settings.ship_blood = self.settings.ship_full_blood
            

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break


    def exit_game(self):
        if self.stats.high_score > int(self.stats.c): 
            path = Path('high_score.txt')
            path.write_text(str(self.stats.high_score))
            
        self.music._stop_music()
        sys.exit()
        exit()

    
        
if __name__ == '__main__':
    ai=AllenInvasion()
    ai.run_game()

