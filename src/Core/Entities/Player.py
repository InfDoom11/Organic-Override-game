"""Player module: movement and basic combat primitives.

This implements a simple top-down/side-view-friendly `Player` with
movement, attack, dodge, parry and a projectile throw. The code uses
timers to manage short windows (attack cooldowns, dodge invulnerability
and parry frames) which are common mechanics in skill-based combat.
"""

import pygame
import math
from .player import Player

#should inherit Player thats coming from pygame
class Player:
    """Represents the player entity and its combat/movement state.

    Attributes:
        rect (pygame.Rect): Position and size for collision and drawing.
        color (tuple): Draw color for the placeholder sprite.
        speed (float): Movement speed in pixels/second.
        health (int): Current health value.

    Combat-related attributes:
        is_attacking, attack_timer, attack_cooldown: control attack timing.
        is_dodging, dodge_timer, dodge_duration, invulnerable: dodge state.
        is_parrying, parry_timer, parry_window: parry timing window.
        projectiles (list): simple dicts representing thrown projectiles.
    """

    def __init__(self, x, y):
        # Core properties: collision rect, color, movement
        self.rect = pygame.Rect(x, y, 40, 60)
        self.color = (50, 160, 220)
        self.speed = 220
        self.health = 100

        # combat states and timers
        self.is_attacking = False
        self.attack_timer = 0.0
        self.attack_cooldown = 0.35

        self.is_dodging = False
        self.dodge_timer = 0.0
        self.dodge_duration = 0.25
        self.invulnerable = False

        self.is_parrying = False
        self.parry_window = 0.2
        self.parry_timer = 0.0

        # simple projectile storage (rect + velocity)
        self.projectiles = []

    def handle_input(self, keys, dt):
        """Read movement keys and translate the player.

        Uses normalized diagonal movement so speed is consistent in all
        directions and multiplies by `dt` for framerate independence.
        """
        dx = dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += 1

        if dx != 0 or dy != 0:
            # normalize vector then apply speed and dt
            length = math.hypot(dx, dy)
            dx /= length
            dy /= length
            self.rect.x += dx * self.speed * dt
            self.rect.y += dy * self.speed * dt

    # Action commands: these set states/timers that are processed in update
    def attack(self):
        """Begin an attack if not on cooldown."""
        if not self.is_attacking and self.attack_timer <= 0:
            self.is_attacking = True
            self.attack_timer = self.attack_cooldown

    def dodge(self):
        """Start a short dodge that grants temporary invulnerability."""
        if not self.is_dodging:
            self.is_dodging = True
            self.dodge_timer = self.dodge_duration
            self.invulnerable = True

    def parry(self):
        """Enter a short parry window that can reflect or interrupt attacks."""
        self.is_parrying = True
        self.parry_timer = self.parry_window

    def throw(self):
        """Spawn a simple forward projectile from the player's center."""
        px = self.rect.centerx
        py = self.rect.centery
        proj = {"rect": pygame.Rect(px, py - 6, 12, 12), "vel": 500}
        self.projectiles.append(proj)

    def update(self, dt):
        """Update timers and move any active projectiles.

        This method decrements timers each frame and clears states when
        windows expire (attack end, dodge end, parry end). It also
        advances projectiles and removes them when off-screen.
        """
        if self.is_attacking:
            self.attack_timer -= dt
            if self.attack_timer <= 0:
                self.is_attacking = False

        if self.is_dodging:
            self.dodge_timer -= dt
            if self.dodge_timer <= 0:
                self.is_dodging = False
                self.invulnerable = False

        if self.is_parrying:
            self.parry_timer -= dt
            if self.parry_timer <= 0:
                self.is_parrying = False

        # Update simple projectile positions and remove off-screen ones
        for p in list(self.projectiles):
            p['rect'].x += int(p['vel'] * dt)
            if p['rect'].x > 900:
                self.projectiles.remove(p)

    def draw(self, surface):
        """Render the player, an attack arc and any projectiles.

        These are placeholder visuals meant to be replaced with sprites
        or animations during iteration.
        """
        pygame.draw.rect(surface, self.color, self.rect)
        if self.is_attacking:
            # Visual hint for the attack (placeholder)
            arc = pygame.Rect(self.rect.right, self.rect.y + 10, 20, 40)
            pygame.draw.rect(surface, (200, 50, 50), arc)

        for p in self.projectiles:
            pygame.draw.rect(surface, (230, 200, 60), p['rect'])
