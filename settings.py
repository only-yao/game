class settings():

    """储存所有设置的类"""
    def __init__(self):
        """初始化设置"""
        # 屏幕设置
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # 飞船设置
        self.ship_speed_factor = 8
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 20
        self.bullet_width = 5
        self.bullet_hight = 150
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 5

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # -1左  1右
        self.fleet_direction = 1

        # 飞船速度增加倍数
        self.speedup_scale = 2
        self.initialize_dynamic_settings()

        # 计分
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        """"初始化设置"""
        self.ship_speed_factor = 8
        self.bullet_speed_factor = 20
        self.alien_speed_factor = 1
        # -1左  1右
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
