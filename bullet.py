import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """飞船子弹"""
    def __init__(self, ai_sttings, screen, ship):
        """飞船处创建子弹"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0，0）处设置子弹，再确定位置
        self.rect = pygame.Rect(0, 0, ai_sttings.bullet_width,
                                ai_sttings.bullet_hight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储小数表示子弹位置
        self.y = float(self.rect.y)

        self.color = ai_sttings.bullet_color
        self.speed_factor = ai_sttings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新子弹位置
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullect(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
