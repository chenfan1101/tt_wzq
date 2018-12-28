import random
from pygame.sprite import Sprite
import pygame


class Alient(Sprite):
    def __init__(self,settings,screen):
        super(Alient, self).__init__()
        self.scr = screen

        self.image = pygame.image.load("images/alient.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.x = random.randrange(10,1200,2) # 生成从1到1200的间隔为2的随机整数
        # self.y = random.randrange(10,20,2)
        self.rect.left = self.x
        # self.rect.bottom = self.y

        # 转换rect.centerx，只能取整数换成能够取小数
        self.bottom = float(self.rect.bottom)

        #移动速度
        self.alient_speed = settings.alient_speed_factor
        #移动标志
        self.moving_bottom = True

        #是否允许发射子弹
        self.allow_bullet = settings.show_alient_bullet_speed




    def update(self):
        # self.rect.right<self.screen_rect.right用来判断不会超出屏幕宽度
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.alient_speed
        # 根据self.center 更新rect对象
        self.rect.bottom = self.bottom


    def blitme(self):
        '''在指定的位置绘制敌机'''
        self.scr.blit(self.image,self.rect)





