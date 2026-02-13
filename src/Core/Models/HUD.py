"""Lesson 1.

Name the file the name of the class that you define in the file. Expections happen with
functional programming or with an auxillary class that only the main class has access 
to.
This is industry practice for Object Oriented programming and that's the best approach
for creating games."""

"This file was initially render for simple UI elements"

import pygame


class HUD:
    """Minimal HUD for the prototype.

    This class handles rendering simple UI elements like the player's
    health and contextual prompts (e.g., a parry indicator). In a full
    game this would be replaced with a layered UI system and icons.
    """

    def __init__(self, player):
        # Reference to the player so the HUD can display status
        self.player = player
        self.font = pygame.font.SysFont(None, 22)

    def draw(self, surface):
        # Draw a simple health label in the top-left corner
        health_text = f"Health: {self.player.health}"
        txt = self.font.render(health_text, True, (220, 220, 220))
        surface.blit(txt, (8, 8))

        # Show contextual prompts when certain states are active
        if self.player.is_parrying:
            p = self.font.render("Parry!", True, (240, 200, 60))
            surface.blit(p, (8, 34))
