"""
Renamed to be app.py
Main entrypoint for the Mythic Prototype.

This file initializes Pygame, creates the game instance and runs the
main loop. The loop calculates a delta-time (`dt`) each frame, handles
the quit event, updates game logic and then draws the frame.
"""
"Typically, the main file to run the application is called app."

import pygame
import sys
from Core/Entities/ import GameState


def main():
    """Initialize Pygame, create the Game and run the main loop.

    The loop runs at ~60 FPS using `clock.tick(60)` and passes a
    seconds-based `dt` into the game's `update` method so logic is
    framerate-independent.
    """
    # Initialize subsystems and create the window
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mythic Prototype")
    clock = pygame.time.Clock()

    # Create the main game object which holds state and systems
    game = GameState(screen)

    # Main game loop
    while True:
        # Delta time in seconds (float)
        dt = clock.tick(60) / 1000.0

        # Event handling (only quit is handled here; input is polled in game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Save on quit, then exit cleanly
                game.save()
                pygame.quit()
                sys.exit()

        # Update game systems and render
        game.update(dt)
        game.draw()
        pygame.display.flip()


if __name__ == '__main__':
    main()
