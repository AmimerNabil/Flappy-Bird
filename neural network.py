import random
import pygame as sys , os
from pygame.locals import *


sys.init()
resolution = (400 , 500)
FPS = 65
clock = sys.time.Clock()

screen = sys.display.set_mode(resolution)

#image
birdPng = sys.image.load("Bird.png")
upperJpg = sys.image.load("upper.jpg")
downJpg = sys.image.load("down.jpg")
background = sys.image.load("bg.png")
ground = sys.image.load("kwowulfj.png")


red = ( 255, 0 , 0 )
black  = ( 0, 0, 0)
white = (255 , 255 , 255)
green = (127,255,0)
cyan = (0, 255, 255)


class Bird(sys.sprite.Sprite):
    posx = 100
    posy = 150
    vely = 2
    gravity = 0.5

    def __init__(self):
        sys.sprite.Sprite.__init__(self)
        self.image = birdPng
        self.rect = self.image.get_rect()
        self.rect.center = (self.posx , self.posy)

    def update(self):
        self.vely += self.gravity
        self.rect.y += self.vely

        if self.rect.bottom >= 425:
            self.rect.bottom = 425


    def jump(self):

        self.vely = -7


class UPipe(sys.sprite.Sprite):

    velx = -3
    height = random.randint(-160 , -10)

    def __init__(self , posx):
        sys.sprite.Sprite.__init__(self)
        self.image = upperJpg
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = self.height

    def update(self):
        self.rect.x += self.velx

        if self.rect.x < -50:
            self.rect.x = 400
            self.height = random.randint(-160, -10)
            self.rect.y = self.height

    def getBottom(self):
        return self.height + 288 + 90

    def getx(self):
        x = self.rect.x
        return x


#object upper pipe
pipeU = UPipe(400)
pipeU2 = UPipe(625)


class DPie(sys.sprite.Sprite):
    velx = -3

    def __init__(self , posx , pipe):
        sys.sprite.Sprite.__init__(self)
        self.y = pipe
        posy = UPipe.getBottom(pipe)

        self.image = downJpg
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    def update(self):
        self.rect.x += self.velx

        if self.rect.x < -50:
            self.rect.x = 400
            self.rect.y = UPipe.getBottom(self.y)



#object down pipe
pipeD = DPie(400 , pipeU)
pipeD2 = DPie(625 , pipeU2)


Sprites = sys.sprite.Group()
bird = Bird()
Sprites.add(bird)


pipes = sys.sprite.Group()

pipes.add(pipeU)
pipes.add(pipeD)
pipes.add(pipeU2)
pipes.add(pipeD2)


running = True


while running:
    clock.tick(FPS)
    screen.fill(cyan)

    bg = (0 , 0)
    screen.blit(background , bg )
    gd = (0 , 425)
    screen.blit(ground , gd)

    pipes.update()
    pipes.draw(screen)

    Sprites.draw(screen)
    Sprites.update()

    if sys.sprite.collide_rect(bird , pipeU):
        running = False

    if sys.sprite.collide_rect(bird , pipeD):
        running = False

    sys.display.flip()

    for events in sys.event.get():
        if events.type == QUIT:
            running = False

        if events.type == KEYDOWN:
            if events.key == K_SPACE:
                bird.jump()
