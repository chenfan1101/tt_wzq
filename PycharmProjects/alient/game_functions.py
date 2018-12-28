import  sys
import  pygame
from alient import Alient

def check_events(settings,screen,ship,bullets):
    # 监视键盘和鼠标的事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #捕获到键盘按下时
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        # 捕获到键盘松开时
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

#响应按键时的处理
def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #允许发射子弹
        ship.allow_bullet = True


#响应按键松开时的处理
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = False
    elif event.key == pygame.K_SPACE:
        #允许发射子弹
        ship.allow_bullet = True

#更新屏幕图像
def update_screen(settings,screen,ship,bullets,alients):
    # 每次循环时都会绘制屏幕
    screen.fill(settings.bg_color)

    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for alient in alients.sprites():
        alient.blitme()

    # 调用类ship中的方法绘制飞船
    ship.blitme()

    # 让绘制的屏幕可见
    pygame.display.flip()

#飞船来袭
def alient_come(settings,screen,alients):
    if len(alients) == 0:
        new_alient = Alient(settings,screen)
        alients.add(new_alient)
    elif len(alients)<= settings.show_alient_number:
        for alient in alients:
            if(alient.rect.bottom == 200):
                new_alient = Alient(settings, screen)
                alients.add(new_alient)



#飞船和外星人飞船撞击
def ship_ram_alientship(ship,alients):
    return


#子弹和外星人飞船的撞击
def bullet_ram_alientship(bullets,alients):
    for alient in alients:
        for bullet in bullets:
            if(bullet.rect.bottom <= alient.rect.bottom and bullet.rect.bottom>=alient.rect.bottom-100):
                if(bullet.rect.left>=alient.rect.left and bullet.rect.left <= alient.rect.left+100):
                    bullets.remove(bullet)
                    alients.remove(alient)


