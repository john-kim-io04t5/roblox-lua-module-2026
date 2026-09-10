"""Utility helpers for Roblox Lua module development.

This module provides small utility functions to assist with Roblox Lua
scripting, focusing on common tasks like character movement and collision
detection.
"""

from typing import Tuple, Union

def calculate_movement_vector(
    forward: float,
    right: float,
    up: float,
    speed: float = 1.0
) -> Tuple[float, float, float]:
    """Calculate the movement vector based on input directions.

    Args:
        forward: Forward movement direction (-1 to 1).
        right: Right movement direction (-1 to 1).
        up: Up movement direction (-1 to 1).
        speed: Movement speed multiplier (default: 1.0).

    Returns:
        Tuple of (x, y, z) movement vector components.
    """
    x = right * speed
    y = up * speed
    z = forward * speed
    return x, y, z

def check_collision(
    position: Tuple[float, float, float],
    size: Tuple[float, float, float],
    other_position: Tuple[float, float, float],
    other_size: Tuple[float, float, float]
) -> bool:
    """Check if two bounding boxes collide.

    Args:
        position: Position of the first bounding box (x, y, z).
        size: Size of the first bounding box (width, height, depth).
        other_position: Position of the second bounding box (x, y, z).
        other_size: Size of the second bounding box (width, height, depth).

    Returns:
        True if the bounding boxes collide, False otherwise.
    """
    x1, y1, z1 = position
    w1, h1, d1 = size
    x2, y2, z2 = other_position
    w2, h2, d2 = other_size

    return (
        x1 < x2 + w2 and x1 + w1 > x2 and
        y1 < y2 + h2 and y1 + h1 > y2 and
        z1 < z2 + d2 and z1 + d1 > z2
    )

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp a value between a minimum and maximum value.

    Args:
        value: Value to clamp.
        min_val: Minimum value.
        max_val: Maximum value.

    Returns:
        Clamped value.
    """
    return max(min_val, min(value, max_val))
