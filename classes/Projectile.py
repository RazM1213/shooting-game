import pygame
import os.path

class Projectile:

    def __init__(self,x,y,radius,color,facing):
        self.x = x #Center x value
        self.y = y #Center y value
        self.radius = radius #Radius length
        self.color = color #Bullet color
        self.facing = facing #1 OR -1 depending on the char facing
        self.vel = 8 * facing

    def draw(self,win):
        #The projectile will be a black circle.
        pygame.draw.circle(win,self.color,(self.x,self.y), self.radius)

    @classmethod
    def play_sound(cls):
        bulletSound = pygame.mixer.Sound(os.path.join('Sounds', 'bullet.wav'))
        bulletSound.play()