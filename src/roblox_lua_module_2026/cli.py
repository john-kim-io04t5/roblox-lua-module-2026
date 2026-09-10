"""Roblox Lua Module 2026: CLI for Roblox Lua script automation.

This module provides a command-line interface for the Roblox Lua Module 2026,
allowing developers to automate common tasks in Roblox game development.
"""

import argparse
from dataclasses import dataclass
from typing import Optional, Sequence

from . import core

@dataclass
class Config:
    """Configuration for the Roblox Lua Module 2026 CLI."""
    script_path: str
    output_path: Optional[str] = None
    optimize: bool = False

def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """Parse command line arguments.

    Args:
        argv: List of arguments, as passed to sys.argv. Defaults to None.

    Returns:
        Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description='Roblox Lua Module 2026 CLI')
    parser.add_argument('script_path', help='Path to the Lua script to process')
    parser.add_argument('-o', '--output', help='Output path for the processed script')
    parser.add_argument('--optimize', action='store_true', help='Optimize the script for performance')
    return parser.parse_args(argv)

def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main entry point for the Roblox Lua Module 2026 CLI.

    Args:
        argv: List of arguments, as passed to sys.argv. Defaults to None.

    Returns:
        Exit code.
    """
    args = parse_args(argv)
    config = Config(args.script_path, args.output, args.optimize)
    return core.run(config)

if __name__ == '__main__':
    raise SystemExit(main())
