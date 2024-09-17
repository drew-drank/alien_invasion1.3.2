from pathlib import Path
class GameStats:

    def __init__(self,ai_game):
        
        self.settings = ai_game.settings
        self.reset_stats()
        
        self.v_high_score()

    
    def v_high_score(self):
        p = Path('high_score.txt')
        self.c = p.read_text().rstrip()
        self.high_score = int(self.c)
        
        
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.settings.ship_full_blood = 100
        self.settings.ship_blood = self.settings.ship_full_blood
        
