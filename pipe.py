import pygame as pg
from random import randint
class Pipe:
    def __init__(self,scale_factor,move_speed):
        self.imgu=pg.transform.scale_by(pg.image.load("assets/pipeup.png").convert_alpha(),scale_factor)
        self.imgd=pg.transform.scale_by(pg.image.load("assets/pipedown.png").convert_alpha(),scale_factor)
        self.rect_up=self.imgu.get_rect()
        self.rect_down=self.imgd.get_rect()
        self.pipe_dis=200
        self.rect_up.y=randint(250,420)
        self.rect_up.x=500
        self.rect_down.y=self.rect_up.y-self.pipe_dis-self.rect_up.height
        self.rect_down.x=500
        self.move_speed=move_speed

    def drawPipe(self,win):
        win.blit(self.imgu,self.rect_up)
        win.blit(self.imgd,self.rect_down)

    def update(self,dt):
        self.rect_up.x-=int(self.move_speed*dt)
        self.rect_down.x-=int(self.move_speed*dt)


