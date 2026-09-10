# Usage

This document describes how to use **roblox-lua-module-2026**.

## Install

```bash
pip install -e .
```

## Basic example

```python
from roblox_lua_module_2026.core import Config, run

cfg = Config(verbose=True, targets=["alpha", "beta"])
run(cfg)
```

## CLI

```bash
roblox_lua_module_2026 alpha beta -v
```

## Theme

This project is oriented around: This module provides a collection of Lua scripts designed for Roblox game development. It is used by developers and modders to enhance game functionality and streamline development processes. One key feature is the ability to automate common tasks, such as character movement and collision detection, saving developers valuable time..
