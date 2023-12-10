import pygame
import pytest
from pygame.sprite import GroupSingle
from alien import Alien

def test_alien_initialization():
    ai_game = Mock()
    alien = Alien(ai_game)

    assert alien.rect.x == alien.rect.width
    assert alien.rect.y == alien.rect.height
    assert alien.x == float(alien.rect.x)

def test_alien_movement():
    ai_game = Mock()
    alien = Alien(ai_game)
    initial_x = alien.x

    # Move the alien right
    ai_game.settings.fleet_direction = 1
    alien.update()
    assert alien.rect.x > initial_x  # Ensure the x coordinate increases

    # Move the alien left
    ai_game.settings.fleet_direction = -1
    alien.update()
    assert alien.rect.x < initial_x  # Ensure the x coordinate decreases

def test_check_edges():
    ai_game = Mock()
    alien = Alien(ai_game)

    # Test when the alien is not at the edge
    assert not alien.check_edges()

    # Test when the alien is at the right edge
    ai_game.settings.fleet_direction = 1
    alien.rect.right = ai_game.screen.get_rect().right
    assert alien.check_edges()

    # Test when the alien is at the left edge
    ai_game.settings.fleet_direction = -1
    alien.rect.left = 0
    assert alien.check_edges()
