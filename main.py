import pygame
import game_functions as gf

from settings import settings
from ship import ship
from pygame.sprite import Group
from alien import Alien
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard



def run_game():
    # 定义全局变量
    global ship
    # 初始化并创建一个窗口对象
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建按钮
    play_button = Button(ai_settings, screen, "PLAY")
    # 储存信息
    stats = Gamestats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = ship(ai_settings, screen)
    # 储存子弹编组
    bullets = Group()

    # 创建外星人群
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.undate_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


run_game()
