"""Renamed GameState

`Game` holds the main state for the prototype: player, enemies, HUD,
and the basic update/draw loop hooks used by `main.py`.
"""

import pygame
import json
import os
from .ui import HUD
from game.core import Game

#Should inherit from Game so that it retains all its properties from pygame
class Game:
    """This is the Game state 

    On Initiation it will render the canvas and get populated with relevant entities

    The `Game` class calls spawning simple placeholder enemies,
    routing player input (polled), performing collisions and basic
    combat resolution, drawing the world and saving/loading basic
    persistent state.
    """

    def __init__(self, screen):
        # Graphics surface and dimensions
        self.screen = screen
        self.width, self.height = screen.get_size()

        RenderEntities()

        # Save file location (relative to package)
        self.save_path = os.path.join(os.path.dirname(__file__), '..', 'save.json')
        self.load()

    
    def update(self, dt):
        """Advance game state: handle input, update player and enemies.

        Input actions (attack, dodge, parry, throw) are polled here and
        forwarded to the `Player` methods. Enemy movement and simple
        collision resolution are performed in this method as well.
        """
        #I abstracted this again because its a really important functionality and should
        #be separated for better control
        CommandService.FirePlayerCommands()    
        #Also abstracted here as well    
        HandleCollisions()       

    def draw(self):
        """Render the world, player, enemies and UI.

        Currently this draws a simple grid, placeholder rectangles for
        entities and delegates HUD drawing to the `HUD` class.
        """
        self.screen.fill(self.bg_color)

        # Optional grid to hint at an explorable space during prototyping
        for x in range(0, self.width, 64):
            pygame.draw.line(self.screen, (20, 20, 30), (x, 0), (x, self.height))

        # Draw player and enemies
        self.player.draw(self.screen)

        #This won't work since there are no enemies in the array. You have to populate the
        #the array and at an appropriate time as well.
        # for e in self.enemies:
        #     pygame.draw.rect(self.screen, (180, 80, 80), e['rect'])

        #this might be better
        self.enemy.draw(self.screen)

        # Draw HUD on top of the scene
        self.hud.draw(self.screen)

    def save(self):
        """Persist minimal state to a JSON save file.

        This demo saves only the player's health. In a full game the
        save would include position, inventory, story flags, etc.
        """
        data = {
            'player': {'health': self.player.health}
        }
        try:
            with open(self.save_path, 'w') as f:
                json.dump(data, f)
        except Exception:
            # Ignore save errors in this minimal prototype
            pass

    def load(self):
        """Load previously saved state if available."""
        try:
            with open(self.save_path, 'r') as f:
                data = json.load(f)
                self.player.health = data.get('player', {}).get('health', self.player.health)
        except Exception:
            # No save or parse error — continue with defaults
            pass

    #method made to abstract populating the world with entities
    #Necessary because as the development progress gets more complex, abstraction 
    #becomes not only our best tool, but our saving grace
    def RenderEntities():
        # Gameplay objects
        self.player = SpawnServicePlayer.spawn_Player(100, 250)
        self.hud = HUD(self.player)
        self.bg_color = (30, 30, 40)

        # Simple enemy list; spawn one for demonstration
        #Changed this to match what we are working with
        self.enemies = SpawnService.spawn_Enemies()
    #method to abstract collision handling
    def HandleCollisions():
         # Updates enemies and check collisions with the player
        for e in list(self.enemies):
            e['rect'].x += int(e['vel'] * dt)

            # Basic collision handling: damage, parry reflect or enemy hurt
            if e['rect'].colliderect(self.player.rect):
                if not self.player.invulnerable:
                    if self.player.is_parrying:
                        # Successful parry reflects enemy direction
                        e['vel'] *= -1
                    elif self.player.is_attacking:
                        # Attacking damages the enemy
                        e['health'] -= 25
                        if e['health'] <= 0:
                            self.enemies.remove(e)
                    else:
                        # Default: player takes damage
                        self.player.health -= 10
        HandleProjectileCollisions()
        self.player.update(dt)
    #method to abstract the projectile collision handling 
    def HandleProjectileCollisions():
        # Projectiles can hit enemies; apply damage and remove projectiles
        for p in list(self.player.projectiles):
            for e in list(self.enemies):
                if p['rect'].colliderect(e['rect']):
                    e['health'] -= 20
                    if e['health'] <= 0:
                        self.enemies.remove(e)
                    try:
                        self.player.projectiles.remove(p)
                    except ValueError:
                        pass
