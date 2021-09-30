import pygame
import os.path

class Enemy:
    walk_right = [pygame.image.load(os.path.join('Images', 'R1E.png')),
                  pygame.image.load(os.path.join('Images', 'R2E.png')),
                  pygame.image.load(os.path.join('Images', 'R3E.png')),
                  pygame.image.load(os.path.join('Images', 'R4E.png')),
                  pygame.image.load(os.path.join('Images', 'R5E.png')),
                  pygame.image.load(os.path.join('Images', 'R6E.png')),
                  pygame.image.load(os.path.join('Images', 'R7E.png')),
                  pygame.image.load(os.path.join('Images', 'R8E.png')),
                  pygame.image.load(os.path.join('Images', 'R9E.png')),
                  pygame.image.load(os.path.join('Images', 'R10E.png')),
                  pygame.image.load(os.path.join('Images', 'R11E.png'))]

    walk_left = [pygame.image.load(os.path.join('Images', 'L1E.png')),
                 pygame.image.load(os.path.join('Images', 'L2E.png')),
                 pygame.image.load(os.path.join('Images', 'L3E.png')),
                 pygame.image.load(os.path.join('Images', 'L4E.png')),
                 pygame.image.load(os.path.join('Images', 'L5E.png')),
                 pygame.image.load(os.path.join('Images', 'L6E.png')),
                 pygame.image.load(os.path.join('Images', 'L7E.png')),
                 pygame.image.load(os.path.join('Images', 'L8E.png')),
                 pygame.image.load(os.path.join('Images', 'L9E.png')),
                 pygame.image.load(os.path.join('Images', 'L10E.png')),
                 pygame.image.load(os.path.join('Images', 'L11E.png')), ]

    def __init__(self, x, y, width, height, end):
        self.x = x #X argument of enemy location
        self.y = y #Y argument of enemy location
        self.width = width #Width of enemy - according to sprite
        self.height = height #Height of enemy - according to sprite
        self.end = end
        self.path = [self.x,self.end] #Stands for the start and finish point of the enemy
        self.walk_count = 0 #Counts enemy's steps (each sprite is a step)
        self.vel = 3 #Stands for enemy's speed
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.health = 9
        self.visible = True

    def move(self):
        #vel > 0 means that the enemy goes right:
        if self.vel > 0:
            #If the current enemy x location, plus, the velocity is lower than the end x location:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * (-1)
                self.walk_count = 0

        else:
            #Considering the case where the vel is negative - the enemy goes left:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * (-1)
                self.walk_count = 0

    def hit(self):
        if self.health > 0:
            hitSound = pygame.mixer.Sound(os.path.join('Sounds', 'hit.wav'))
            hitSound.play()
            self.health -= 1
        else:
            self.visible = False

        print('HIT')

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walk_count + 1 >= 33:
                self.walk_count = 0
            if self.vel > 0:
                win.blit(Enemy.walk_right[self.walk_count // 3], (round(self.x), round(self.y)))
                self.walk_count += 1
            elif self.vel < 0:
                win.blit(Enemy.walk_left[self.walk_count // 3], (round(self.x), round(self.y)))
                self.walk_count += 1

            pygame.draw.rect(win,(255,0,0),(self.hitbox[0], self.hitbox[1] - 20, 50, 10 ))
            pygame.draw.rect(win,(0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (9 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y, 28, 60)