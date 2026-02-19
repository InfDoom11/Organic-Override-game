import pygame
from Core.Entities.Enemy import Enemy

class EnemyFactory:
    @staticmethod
    def CreateEnemy(levelOfEnemy):
        """Creates a simple enemy with rect, velocity and health."""
        
        enemy_stats = {
            1: {'rect': pygame.Rect(600, 260, 50, 60), 'vel': -60, 'health': 30},
            2: {'rect': pygame.Rect(600, 260, 50, 60), 'vel': -20, 'health': 70},
            3: {'rect': pygame.Rect(600, 260, 50, 60), 'vel': -5, 'health': 100}
        }
        
        stats = enemy_stats.get(levelOfEnemy, enemy_stats[1])
        return Enemy(stats['rect'], stats['vel'], stats['health'])