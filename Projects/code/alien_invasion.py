import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from stars import Stars

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # 保存游戏状态
        #  计分板
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        
        #创建星星
        self.stars = pygame.sprite.Group()
        self._create_stars()
        
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()

        # 开始外星人入侵
        self.game_active = False

        # 建立按钮
        self.play_button = Button(self, "Play")
        
        
    def _create_stars(self):
        """创建星星并添加到组中"""
        for star_number in range(self.settings.stars_allowed):
            new_star = Stars(self)
            self.stars.add(new_star)

    def run_game(self):
        """开始运行游戏."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def write_high_score(self):
        # 构建文件的相对路径，相对于当前工作目录
        file_path = './Projects/code/x.txt'

        try:
            with open(file_path, mode='w') as file:
                print('Writing to file')
                file.write(str(self.stats.high_score) + '\n')
        except Exception as e:
            print(f"Error writing to file: {e}")



    def _check_events(self):
        """按键和鼠标检测"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.write_high_score()
                #self.sb.save_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """开始一个新游戏当点击play后."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # 重置设置
            self.settings.initialize_dynamic_settings()

            # 重置数据
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            #消除消失的子弹
            self.bullets.empty()
            self.aliens.empty()

            # 建立新的外星人舰队
            self._create_fleet()
            self.ship.center_ship()

            
            # 隐藏鼠标.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """按键响应."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            #self.sb.save_score()
            self.write_high_score()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """释放响应."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一个子弹加入到子弹类中."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """更新子弹位置和删除出屏幕的子弹."""
        # 更新子弹位置
        self.bullets.update()

        #删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """碰撞检测."""
        # 删除和外星人碰撞的子弹
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # 删除存在的子弹，建立新舰队，提升速度
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # 升级
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # 更新飞船.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # 消除原来的子弹和外星人
            self.bullets.empty()
            self.aliens.empty()

            # 建立新的舰队和飞船
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        """检查边缘和外星人更新."""
        self._check_fleet_edges()
        self.aliens.update()

        # 检查飞船和外星人是否碰撞.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 外星人到达底部.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """外星人是否到达底部."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _create_fleet(self):
        """舰队."""
        # 生成舰队.
        # 舰队排列.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # 更新x和y.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """生成外星人."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """检测是否超出边界."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """舰队运动."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """更新屏幕."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.stars.draw(self.screen)
        #画出屏幕信息.
        self.sb.show_score()

        # 没开始时，画出底部
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # 建立类，并开始游戏
    ai = AlienInvasion()
    ai.run_game()