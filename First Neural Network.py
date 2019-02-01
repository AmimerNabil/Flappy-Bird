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


class Bird:

    velx = 0
    vely = 0
    posx = 100
    posy = 200
    gravity = 0.4
    times = 3
    myImage = sys.image.load("Bird.png")
    imageRect = myImage.get_rect()
   # print(myImage.get_rect().height)


    def __init__(self , number):
        self.number = number

    def draw(self):
        y = self.posy

        screen.blit(self.myImage , (self.posx , y))

        if self.posy <= 10 :
            self.posy = 10

    def update(self):

        self.posy += self.vely
        self.vely += self.gravity
        self.posx += self.velx

    def jump(self):
        self.vely = -6

    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def getVelX(self):
        return self.velx

    def getVelY(self):
        return self.vely


class Pipes:

    height = random.randint(-190, 0)
    upper = sys.image.load("upper.jpg")
    down = sys.image.load("down.jpg")
    velx = -2
    upperRect = upper.get_rect()
    downRect = down.get_rect()
    print(upperRect.width)
    pipeDist = 0

    def __init__(self, posX):
        self.posX = posX

    def draw(self):

        self.pipeDist = self.height + 288 + 95
        screen.blit(self.upper, (self.posX, self.height))
        screen.blit(self.down, (self.posX, self.pipeDist))

    def update(self):
        self.posX += self.velx

        if self.posX == -50:
            self.posX = 400
            self.height = random.randint(-190, 0)

    def getX(self):
        return self.posX

    def getbotY(self):
        return self.pipeDist

    def getUpY(self):
        upY = self.height + 288
        return upY


bird = Bird(1)
pipe2 = Pipes(500)
pipe3 = Pipes(700)


while running:
    clock.tick(75)
    screen.fill(cyan)
    print(pipe2.getUpY())

    #pipes
    pipe2.draw()
    pipe2.update()
    pipe3.draw()
    pipe3.update()

    #bird
    bird.draw()
    bird.update()

    #colision
    print("wassgud")

    #screen
    sys.display.flip()

    for event in sys.event.get():
        if event.type == sys.QUIT:
            running = False

        if event.type == sys.KEYDOWN:
            if event.key == K_SPACE:
                bird.jump()


