#should inherit the class (maybe its called Object) that pygame uses, and has the function
#update(dt)
import pygame
class Enemy:
    def __init__(self, rect, vel, health):
        self.rect = rect
        self.vel = vel
        self.health = health
        self.color = (255, 0, 0)
        self.is_attacking = False

    def draw(self, surface):
        """Render the enemy,and an attack arc 

        These are placeholder visuals meant to be replaced with sprites
        or animations during iteration.
        """
        pygame.draw.rect(surface, self.color, self.rect)
        if self.is_attacking:
            # Visual hint for the attack (placeholder)
            arc = pygame.Rect(self.rect.right, self.rect.y + 10, 20, 40)
            pygame.draw.rect(surface, (200, 50, 50), arc)