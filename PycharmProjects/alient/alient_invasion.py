import pygame
from settings import Settings
from ship import  Ship
import game_functions as gf
from bullet import Bullet
from pygame.sprite import Group
import threading as thd
from alient import Alient

def run_game():
    #初始化 Setting类
    se = Settings()

    #初始化程序并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((se.screen_width,se.screen_height))
    pygame.display.set_caption("Alient_Invasion")

    # 初始化 ship类
    ship = Ship(se,screen)



    #创建一个用于存储子弹的编组
    bullets = Group()
    alients = Group()



    #开始游戏的主循环
    while True:

        #调用game_functions文件中的方法来监听键盘和鼠标的事件
        gf.check_events(se,screen,ship,bullets)

        #不断获取键盘事件并移动飞船位置
        ship.update()


        ship.allow_bullets(se,screen,ship,bullets)
        bullets.update()

        gf.alient_come(se,screen,alients)
        alients.update()


        # 删除已消失的子弹
        for bullet in bullets:
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        # 删除已触底的外星人飞船
        for alient in alients:
            if (alient.bottom >= screen.get_rect().bottom):
                alients.remove(alient)


        # 调用game_functions文件中的方法来绘制屏幕,飞船，子弹以及使其可见
        gf.update_screen(se,screen,ship,bullets,alients)

        # 子弹和外星人飞船的撞击
        gf.bullet_ram_alientship(bullets,alients)


if __name__ == "__main__":
    run_game()
