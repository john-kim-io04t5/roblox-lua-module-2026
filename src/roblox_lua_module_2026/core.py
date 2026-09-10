from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    """Configuration for the Roblox Lua module.

    Attributes:
        character_speed: The speed at which the character moves.
        collision_radius: The radius used for collision detection.
        debug_mode: Whether to enable debug logging.
    """
    character_speed: float = 16.0
    collision_radius: float = 2.0
    debug_mode: bool = False

def _log_debug(message: str, config: Config) -> None:
    """Log a debug message if debug mode is enabled.

    Args:
        message: The message to log.
        config: The configuration object.
    """
    if config.debug_mode:
        print(f"[DEBUG] {message}")

def run(config: Optional[Config] = None) -> int:
    """Run the Roblox Lua module with the given configuration.

    Args:
        config: The configuration to use. If None, a default configuration is used.

    Returns:
        int: 0 if successful, non-zero otherwise.
    """
    if config is None:
        config = Config()

    _log_debug("Starting Roblox Lua module", config)

    # Example: Automate character movement
    _log_debug(f"Setting character speed to {config.character_speed}", config)

    # Example: Automate collision detection
    _log_debug(f"Setting collision radius to {config.collision_radius}", config)

    _log_debug("Roblox Lua module completed successfully", config)
    return 0
