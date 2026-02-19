from Core.Entities.Enemy import Enemy
from Core.Models.GameLevel import GameLevel
from Infrastructure.Factories.PlayerFactory import PlayerFactory
from Infrastructure.Factories.EnemyFactory import EnemyFactory

class SpawnService:
    def __init__(self, gameLevel):
        self.gameLevel = gameLevel
    
    def spawn_Player(self, x, y):
        return PlayerFactory.CreatePlayer(x, y)
    
    def spawn_Enemies(self, numberOfEnemies=None):
        if numberOfEnemies is None:
            numberOfEnemies = self.gameLevel.number * 3
        
        enemies = []
        for i in range(numberOfEnemies):
            enemies.append(EnemyFactory.CreateEnemy(self.gameLevel.number))
        return enemies