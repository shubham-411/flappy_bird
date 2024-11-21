import pygame as pg

class Bird(pg.sprite.Sprite):
    def __init__(self,scale_factor):
        super(Bird,self).__init__()
        self.image_l=[pg.transform.scale_by(pg.image.load("assets/birdup.png").convert_alpha(),scale_factor),
                      pg.transform.scale_by(pg.image.load("assets/birddown.png").convert_alpha(),scale_factor)]
        self.image_i= 0
        self.image= self.image_l[self.image_i]
        self.rect=self.image.get_rect(center=(100,100))
        self.yspeed=0
        self.gravity=10
        self.fspeed=250
        self.acount=0
        self.update_on=False

    def update(self,dt):
        if self.update_on:
            self.playa()
            self.applyg(dt)

            if self.rect.y<=0:
              self.rect.y=0
              self.fspeed=0
            elif self.rect.y>=0 and self.fspeed==0:
              self.fspeed=250

    def applyg(self,dt):
         self.yspeed += self.gravity * dt
         self.rect.y += self.yspeed

    def fly(self,dt):
        self.yspeed = -self.fspeed*dt

    def playa(self):
        if self.acount==5:
            self.image=self.image_l[self.image_i]
            if self.image_i==0: self.image_i=1
            else: self.image_i=0
            self.acount=0
        self.acount+=1
    def reset(self):
        self.rect.center=(100,100)
        self.yspeed=0
        
    
