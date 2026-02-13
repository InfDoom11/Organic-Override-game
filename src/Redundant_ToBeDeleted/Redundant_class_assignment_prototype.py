"""game package

This package exposes the main game classes so callers can import
`Game` and `Player` from `game` directly.
"""
"""I'm assuming that Game is a library that comes from the IDE packages for game dev.
In which case you can just import these libraries in the relevant files. You shouldn't
globally expose types for every file. Cause that can confuse other developers and the 
compiler and your future self about your intentions.

You also had the exact same file with 'calls to main game'. But that was even more 
terribly named because it had nothing to do with calling anything."""

# from .core import Game
# from .player import Player

# __all__ = ["Game", "Player"]
