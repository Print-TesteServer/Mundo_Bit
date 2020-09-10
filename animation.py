import pygame
from simpleTimer import *

class Animation():
    def __init__(self, animation_frames, delay_to_next_frame):
        self.animation_frames = animation_frames
        self.delay_to_next_frame = delay_to_next_frame
        self.frame = 0
        self.image = pygame.image.load(self.animation_frames[self.frame])
        self.timer = Timer()
        self.state = "run"

    def update(self):
        if self.timer.getTimer() >= self.delay_to_next_frame:
            if self.frame <len(self.animation_frames)-1:
                self.frame += 1
            else:
                self.frame = 0
            self.timer.resetTimer()
        self.image = pygame.image.load(self.animation_frames[self.frame])

    def pause(self):
        self.timer.pauseTimer()
        self.state = "paused"

    def resume(self):
        self.timer.resetTimer()
        self.state = "run"
