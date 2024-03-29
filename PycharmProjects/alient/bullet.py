from settings import Settings
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''一个对飞船发射的子弹管理的类'''
    def __init__(self,settings,screen,ship):
        '''在飞船所处的位置创建一个子弹类'''
        super(Bullet,self).__init__()
        self.screen = screen
        #在（0，0）处创建一个子弹的矩形，再设置其到正确的位置
        self.rect = pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
        self.rect.centerx = ship.center
        self.rect.top = ship.rect.top
        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        self.y -=self.speed_factor
        self.rect.y = self.y


    #绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)