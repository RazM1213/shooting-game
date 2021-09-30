import pygame
import os.path
from classes.Enemy import Enemy
from classes.Lives import Lives
from classes.Player import Player
from classes.Projectile import Projectile
pygame.init()

#Setting the game up:
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")
icon = pygame.image.load(os.path.join('images', 'standing.png'))
pygame.display.set_icon(icon)
score = 0
lives = 3

clock = pygame.time.Clock()

background = pygame.image.load(os.path.join('images', 'bg.jpg'))
char = pygame.image.load(os.path.join('images', 'standing.png'))

font_gameover = pygame.font.SysFont('comicsans',70,True,True)
font_score = pygame.font.SysFont('comicsans', 30, True)
text = font_gameover.render('GAME OVER!', 1, (0,0,0))

background_sound = pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.play()

def redraw_game_window():
    win.blit(background, (0,0))

    for bullet in bullets:
        bullet.draw(win)

    player.draw(win)

    enemy.draw(win)

    for life in lives:
        life.draw(win)

    text_score = font_score.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text_score, (370, 10))

    pygame.display.update()