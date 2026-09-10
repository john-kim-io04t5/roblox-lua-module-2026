"""pytest tests for core module of roblox-lua-module-2026."""

import pytest
from roblox_lua_module_2026.core import (
    automate_character_movement,
    detect_collision,
    streamline_development,
)

def test_automate_character_movement() -> None:
    """Test automate_character_movement function."""
    result = automate_character_movement("walk", 10)
    assert result == "Character is walking at speed 10"

def test_detect_collision() -> None:
    """Test detect_collision function."""
    result = detect_collision("player", "wall")
    assert result == "Collision detected between player and wall"

def test_streamline_development() -> None:
    """Test streamline_development function."""
    result = streamline_development("script", "optimize")
    assert result == "Script optimized for better performance"
