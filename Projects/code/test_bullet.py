from unittest.mock import Mock
import pytest
from bullet import Bullet  # 替换为实际的子弹模块

@pytest.fixture
def mock_ai_game():
    """创建 Mock 对象来模拟 ai_game 对象."""
    return Mock()

def test_bullet_update(mock_ai_game):
    """测试子弹的更新方法."""
    # 创建子弹对象，传入模拟的 ai_game 对象
    bullet = Bullet(mock_ai_game)

    # 设置子弹的初始状态
    bullet.rect.x = 10
    bullet.settings.bullet_speed = 5

    # 调用子弹的更新方法
    bullet.update()

    # 断言子弹的位置是否按预期更新
    assert bullet.rect.x == 15

def test_bullet_check_edges(mock_ai_game):
    """测试子弹的检查边缘方法."""
    # 创建子弹对象，传入模拟的 ai_game 对象
    bullet = Bullet(mock_ai_game)

    # 设置子弹的初始位置
    bullet.rect.x = 800

    # 调用子弹的检查边缘方法
    result = bullet.check_edges()

    # 断言子弹是否到达屏幕右边缘
    assert result is True
