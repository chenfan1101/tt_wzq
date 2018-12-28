class Settings():
    '''存储《外星人入侵》的所有的设置的类'''
    def __init__(self):
        '''初始化游戏设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # 飞船的移动速度
        self.ship_speed_factor = 1.5

        #子弹设置
        self.bullet_speed_factor = 1  #子弹移动的速度
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 90,90,90
        #子弹发射的速度
        self.show_bullet_speed = 1

        #外星人敌机的移动速度
        self.alient_speed_factor = 1.5
        #子弹发射的速度
        self.show_alient_bullet_speed = 1
        #最多允许存在的外星人数量
        self.show_alient_number = 100

