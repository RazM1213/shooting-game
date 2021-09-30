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

#Instance of the enemy class:
enemy = Enemy(100,410,64,64,450)

#Instance of the player class:
player = Player(300,410,64,64)

#Bullets have been shot:
bullets = []
shootLoop = 0
#Pending lives:
last = Lives(10,10)
second = Lives(50,10)
first = Lives(90,10)
lives = [last, second, first]

run = True

#Game main loop:
while run:

    clock.tick(33)
    if enemy.visible:
        if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player.hitbox[1] + player.hitbox[3] > enemy.hitbox[1]:
            if player.hitbox[0] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                player.hit()
                lives.pop()
                if len(lives) == 0:
                    win.blit(text, (70,240))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    run = False
    redraw_game_window()
    #Declaring the amount of miliseconds between iterations of the loop:
    pygame.time.delay(30)

    #The main for loop for each event in the game:
    for event in pygame.event.get():
        #Setting an operation for pressing X on the game window:
        if event.type == pygame.QUIT:
            run = False

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    if enemy.visible == True:
        for bullet in bullets:
            #Check 2 things: Whether the bullet is below the top y level, Wether the bullet is above the low y level
            if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                #Check 2 things: Whether the bullet is in the right side of the left x level, Whether the bullet is in the left side of the right x level
                if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                    #If all the above happens -- > it's a hit, and we vanish the bullet.
                    enemy.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    #Creating a variable 'KEYS' which stands for all the keys operations that we will choose that
    #will be pressed in the game:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        Projectile.play_sound()
        if player.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 10:
            bullets.append(Projectile(round(player.x + player.width//2), round(player.y + player.height//2), 6, (0,0,0), facing))
        shootLoop = 1

    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False

    elif keys[pygame.K_RIGHT] and player.x < 500 - player.vel - player.width:
        player.x += player.vel
        player.left = False
        player.right = True
        player.standing = False
    else:
        player.standing = True
        player.walkCount = 0

    if not(player.is_jump):
        if keys[pygame.K_UP]:
            player.is_jump = True
            player.standing = True
            player.walkCount = 0

    else:
        if player.jump_count >= -8:
            neg = 1
            if player.jump_count < 0:
                neg = -1
            player.y -= (player.jump_count ** 2) / 2 * neg
            player.jump_count -= 1
        else:
            player.is_jump = False
            player.jump_count = 8

pygame.quit()