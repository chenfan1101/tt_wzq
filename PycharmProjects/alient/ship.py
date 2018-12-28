import  pygame

import time
from bullet import Bullet

class Ship():
    def __init__(self,settings,screen):
        '''初始化飞船并设置其初始位置'''
        self.screen = screen

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #获得屏幕的外接矩形
        self.screen_rect =screen.get_rect()

        #将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #飞船的移动速度
        self.ship_speed_factor = settings.ship_speed_factor

        #转换rect.centerx，只能取整数换成能够取小数
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right= False
        self.moving_left = False

        # 是否允许发射子弹
        self.allow_bullet = False


    def update(self):
        #self.rect.right<self.screen_rect.right用来判断不会超出屏幕宽度
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ship_speed_factor
        #根据self.center 更新rect对象
        self.rect.centerx = self.center


    def blitme(self):
        '''在指定的位置绘制飞船'''
        self.screen.blit(self.image,self.rect)


    #让飞船发射子弹
    def allow_bullets(self,settings,screen,ship,bullets):
        if self.allow_bullet:
            if len(bullets) == 0:
                new_bullet = Bullet(settings,screen,ship)
                bullets.add(new_bullet)
            elif len(bullets)>0:
                #设置子弹的速度，让第一颗子弹移动到700时发射第二颗子弹，实际上让子弹的平路变快，最大不超过800
                 for bullet in bullets:
                    if(bullet.rect.bottom == 700):
                        new_bullet = Bullet(settings, screen, ship)
                        bullets.add(new_bullet)



