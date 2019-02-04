import random
import pygame as sys , os
from pygame.locals import *

sys.init()

running = True
clock = sys.time.Clock()

#colors
red = ( 255, 0 , 0 )
black  = ( 0, 0, 0)
white = (255 , 255 , 255)
green = (127,255,0)
cyan = (0, 255, 255)

#screen and resolution
resolution = (400 , 500)
screen = sys.display.set_mode(resolution)
sys.display.set_caption("Flappy bird")


class Bird(sys.sprite.Sprite):

    velx = 0
    vely = 0
    posx = 100
    posy = 200
    gravity = 0.4
    times = 3
  #  myImage = sys.image.load("Bird.png")


   # print(myImage.get_rect().height)
    def __init__(self):
        sys.sprite.Sprite.__init__(self)
        self.image = sys.image.load("Bird.png").convert_alpha()
        self.rect = self.image.get_rect()

    def draw(self):
        y = self.posy

        screen.blit(self.image , (self.posx , y))

        if self.posy <= 10 :
            self.posy = 10

    def update(self):

        self.posy += self.vely
        self.vely += self.gravity
        self.posx += self.velx

    def jump(self):
        self.vely = -6

    def getPosX(self):
        posx = self.posx + 32
        return posx

    def getPosY(self):
        return self.posy

    def getVelX(self):
        return self.velx

    def getVelY(self):
        return self.vely

    def setX(self , posx):
        self.posy = posx


class Pipes(sys.sprite.Sprite):

    height = random.randint(-190, 0)
    velx = -2
    pipeDist = 0
    def __init__(self, posX):
        sys.sprite.Sprite.__init__(self)
        self.upper = sys.image.load("upper.jpg").convert_alpha()
        self.down = sys.image.load("down.jpg").convert_alpha()
        self.upperRect = self.upper.get_rect()
        self.downRect = self.down.get_rect()

        self.posX = posX

    def draw(self):

        self.pipeDist = self.height + 288 + 95
        screen.blit(self.upper, (self.posX, self.height))
        screen.blit(self.down, (self.posX, self.pipeDist))
        self.downrect.center(self.posX, self.pipeDist)
        self.downRect.fill(green)

    def update(self):
        self.posX += self.velx

        if self.posX == -50:
            self.posX = 400
            self.height = random.randint(-190, 0)

    def getX(self):
        return self.posX

    def getbotY(self):
        height = range(self.pipeDist , self.pipeDist + 288)
        return height

    def getUpY(self):
        upY = self.height + 288
        return upY

bird = Bird()
pipe2 = Pipes(500)
pipe3 = Pipes(700)
pipes = sys.sprite.Group()
pipes.add(pipe2)
pipes.add(pipe3)

while running:
    clock.tick(75)
    screen.fill(cyan)



    #pipes
    #pipe2.draw()
    #pipe3.draw()
    pipes.update()

    #bird
    bird.draw()
    bird.update()

    #colision

    #screen
    sys.display.flip()

    for event in sys.event.get():
        if event.type == sys.QUIT:
            running = False

        if event.type == sys.KEYDOWN:
            if event.key == K_SPACE:
                bird.jump()


