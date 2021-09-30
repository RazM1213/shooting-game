import pygame
import os.path

class Player:
    walk_right = [pygame.image.load(os.path.join('images', 'R1.png')),
                  pygame.image.load(os.path.join('images', 'R2.png')),
                  pygame.image.load(os.path.join('images', 'R3.png')),
                  pygame.image.load(os.path.join('images', 'R4.png')),
                  pygame.image.load(os.path.join('images', 'R5.png')),
                  pygame.image.load(os.path.join('images', 'R6.png')),
                  pygame.image.load(os.path.join('images', 'R7.png')),
                  pygame.image.load(os.path.join('images', 'R8.png')),
                  pygame.image.load(os.path.join('images', 'R9.png'))]

    walk_left = [pygame.image.load(os.path.join('images', 'L1.png')),
                 pygame.image.load(os.path.join('images', 'L2.png')),
                 pygame.image.load(os.path.join('images', 'L3.png')),
                 pygame.image.load(os.path.join('images', 'L4.png')),
                 pygame.image.load(os.path.join('images', 'L5.png')),
                 pygame.image.load(os.path.join('images', 'L6.png')),
                 pygame.image.load(os.path.join('images', 'L7.png')),
                 pygame.image.load(os.path.join('images', 'L8.png')),
                 pygame.image.load(os.path.join('images', 'L9.png'))]

    def __init__(self, x, y, width, height):
        self.x = x #The x argument of the char location
        self.y = y #The y argument of the char location
        self.width = width #The width of the char (according to the sprites)
        self.height = height #The height of the char (according to the sprites)
        self.is_jump = False #Determines wether the char is in mid air or not.
        self.jump_count = 8 #Determines the number of pixels per jump.
        self.vel = 5 #Stands for the 'speed' of the char.
        self.left = False #Determines wether the char is facing left
        self.right = False #Determines wether the char is facing right
        self.walk_count = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52) #Rectangle hitbox

    def draw(self,win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not self.standing:
            if self.left:
                win.blit(Player.walk_left[self.walk_count // 3], (round(self.x), round(self.y)))
                self.walk_count += 1
            elif self.right:
                win.blit(Player.walk_right[self.walk_count // 3], (round(self.x), round(self.y)))
                self.walk_count += 1
        else:
            if self.right:
                win.blit(Player.walk_right[0], (round(self.x), round(self.y)))
            else:
                win.blit(Player.walk_left[0], (round(self.x), round(self.y)))
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def hit(self):
        self.x = 60
        self.y = 410
        self.walk_count = 0
        pygame.display.update()

        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 101
                    pygame.quit()