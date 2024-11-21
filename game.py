import pygame as pg
import sys,time
from bird import Bird
from pipe import Pipe

pg.init()


class Game:
    def __init__(self):
        #setting window
        self.width =500
        self.height = 600
        self.scale_factor=1.5
        self.win =pg.display.set_mode((self.width,self.height))
        self.clock=pg.time.Clock()
        self.move_speed=200
        self.start_m=False
        self.score=0
        self.font=pg.font.Font("assets/font.ttf",14)
        self.score_t=self.font.render("Score:0",True,(255,0,0))
        self.score_trect=self.score_t.get_rect(center=(100,20))
        self.restart_t=self.font.render("Restart",True,(255,0,0))
        self.restart_trect=self.score_t.get_rect(center=(250,300))
       
        self.bird=Bird(self.scale_factor)
        self.isenter=False
        self.isgame_started=True
        self.pipes=[]
        self.generate_c=71
        self.setup()

        self.gloop()

    def gloop(self):
        last_time=time.time()
        while True:
            ntime=time.time()
            dl=ntime-last_time
            last_time=ntime
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type==pg.KEYDOWN and self.isgame_started:
                    if event.key==pg.K_RETURN:
                        self.isenter=True
                        self.bird.update_on=True
                    if event.key==pg.K_SPACE and self.isenter:
                        self.bird.fly(dl)
                if event.type==pg.MOUSEBUTTONUP:
                    if self.restart_trect.collidepoint(pg.mouse.get_pos()):
                        self.restart()

            self.updation(dl)
            self.check()
            self.checks()
            self.draw()
            pg.display.update()
            self.clock.tick(60)

    def restart(self):
        self.score=0
        self.score_t=self.font.render("Score:0",True,(255,0,0))
        self.isenter=False
        self.isgame_started=True
        self.bird.reset()
        self.pipes.clear()
        self.generate_c=71
        self.bird.update_on=False

    def updation(self,dl):
        if self.isenter:
            self.ground1_rect.x-=int(self.move_speed*dl)
            self.ground2_rect.x-=int(self.move_speed*dl)
            
            if self.ground1_rect.right<0:
                self.ground1_rect.x=self.ground2_rect.right
            if self.ground2_rect.right<0:
                self.ground2_rect.x=self.ground1_rect.right
           
            if self.generate_c>70:
                self.pipes.append(Pipe(self.scale_factor,self.move_speed))
                self.generate_c=0
            self.generate_c+=1
            for pipe in self.pipes:
                pipe.update(dl)

            if len(self.pipes)!=0:
                if self.pipes[0].rect_up.right<0:
                    self.pipes.pop(0)

        
         
        self.bird.update(dl)
    
    def checks(self):
        if len(self.pipes)>0:
            if (self.bird.rect.left>self.pipes[0].rect_down.left and self.bird.rect.right<self.pipes[0].rect_down.right and not self.start_m):
               self.start_m=True
            if (self.bird.rect.left>self.pipes[0].rect_down.right and self.start_m):
                self.start_m=False
                self.score+=1
                self.score_t=self.font.render(f"Score:{self.score}",True,(255,0,0))
    
               
    
    def check(self):
     if len(self.pipes):
        if (self.bird.rect.colliderect(self.pipes[0].rect_down) or
               self.bird.rect.colliderect(self.pipes[0].rect_up)):
                self.isenter=False
                self.isgame_started=False
        if self.bird.rect.bottom>498:
                 self.bird.update_on= False
                 self.isenter= False
                 self.isgame_started=False


    def draw(self):
        self.win.blit(self.bg_img,(0,-300))
        for pipe in self.pipes:
            pipe.drawPipe(self.win)
        self.win.blit(self.ground1_img,self.ground1_rect)
        self.win.blit(self.ground2_img,self.ground2_rect)
        self.win.blit(self.bird.image,self.bird.rect)
        self.win.blit(self.score_t,self.score_trect)
        if not self.isgame_started:
            self.win.blit(self.restart_t,self.restart_trect)


    def setup(self):
         #loading images
        self.bg_img=pg.transform.scale_by(pg.image.load("assets/bg.png").convert(),self.scale_factor)
        self.ground1_img=pg.transform.scale_by(pg.image.load("assets/ground.png").convert(),self.scale_factor)
        self.ground2_img=pg.transform.scale_by(pg.image.load("assets/ground.png").convert(),self.scale_factor)
        self.ground1_rect=self.ground1_img.get_rect()
        self.ground2_rect=self.ground2_img.get_rect()
        self.ground1_rect.x=0
        self.ground2_rect.x=self.ground1_rect.right
        self.ground1_rect.y=500
        self.ground2_rect.y=500


g=Game()