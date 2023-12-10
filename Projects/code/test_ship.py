from unittest.mock import Mock
from ship import Ship

def test_ship_movement():
    ai_game = Mock()
    ship = Ship(ai_game)
    initial_y = ship.y

    # Move the ship up
    ship.moving_up = True
    ship.update()
    assert ship.rect.y < initial_y  # Ensure the y coordinate decreases

    # Move the ship down
    ship.moving_up = False
    ship.moving_down = True
    ship.update()
    assert ship.rect.y > initial_y  # Ensure the y coordinate increases

def test_ship_not_moving():
    ai_game = Mock()
    ship = Ship(ai_game)
    initial_y = ship.y

    ship.moving_up = False
    ship.moving_down = False
    ship.update()
    assert ship.rect.y == initial_y  # Ensure the y coordinate does not change

def test_ship_centering():
    ai_game = Mock()
    ship = Ship(ai_game)
    ship.rect.y = 100  # Set an initial position not in the center
    ship.center_ship()
    assert ship.rect.midleft == ship.screen_rect.midleft  # Ensure the ship is centered
