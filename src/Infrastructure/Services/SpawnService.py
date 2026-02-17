from ../../Core/Entities/ import Enemy
from ../../Core/Models import GameLevel

class SpawnService: 
    #This is set as the player advances, and is used to manipulate the spawningLevel
    def gameLevel

    #This is important because as the game becomes more complex, you need to be able to
    #explicitly control and consistently create players, so having that code in one place
    #makes that possible
    def spawn_Player(x,y):
        #There may be properties that you want to streamline in creation so a factory
        #works
        #And I found a PlayerFactory merited if we consider multipler options
        return PlayerFactory.CreatePlayer()

    #This spawns a number of enemies as requested
    def spawn_Enemies(numberOfEnemies):        
        #Creates the number of enemies given with the factory and returns the collection
        for numberOfEnemies
        Enemies.append(EnemyFactory.CreateEnemy(gameLevel.levelNumber));
    return Enemies;
    #This is an override of spawn_Enemy(numberOfEnemies) that spawns a number dependant
    #on the gamelevel
    def spawn_Enemies():        
        #Creates the number of enemies given with the factory and returns the collection
        for GameLevel*3
        Enemies.append(EnemyFactory.CreateEnemy(gameLevel.levelNumber));
    return Enemies;
        
        
