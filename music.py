import pygame
class Music:
    def __init__(self):
        self.mixer = pygame.mixer
        self.mixer.init()
        self.myymusic = pygame.mixer.Sound("images/fire.wav")
        self.mymusic = pygame.mixer.Sound("images/break.wav")
        self.mixer.music.load('images/background.ogg')

    def _check_fire_music(self):
        self.myymusic.set_volume(0.7)
        self.myymusic.play()
        
    def _check_break_music(self):
        self.mymusic.set_volume(0.5)
        self.mymusic.play()

    def _check_background_music(self):
        self.mixer.music.play(-1) 

    def _stop_music(self):
        self.myymusic.stop()
        self.mymusic.stop()
        pygame.mixer.music.stop()
