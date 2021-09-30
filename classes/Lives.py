import pygame
import os.path

class Lives:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self,win):
        win.blit(pygame.image.load(os.path.join('Images', 'life.png')), (self.x, self.y))