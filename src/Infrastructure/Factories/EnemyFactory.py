class EnemyFactory:
    #I took the function you defined and put it where it would belong. Abstracting 
    #creating the enemy with other things. Why?
    #By separating concerns it becomes easier to maintain and develop and debug

    def CreateEnemy(levelOfEnemy)
    """Creates a simple enemy as a dict with rect, velocity and health.

        This is a placeholder stub to demonstrate collisions and damage.
        """
    #I'm not sure if python has a switch syntax, but I'm just spitting choices based on
    #the parameter
    switch 
    levelOfEnemies:1
    e = {'rect': pygame.Rect(600, 260, 50, 60), 'vel': -60, 'health': 30}
    levelOfEnemies:2
    e = {'rect': pygame.Rect(600, 260, 50, 60), 'vel': -20, 'health': 70}
    levelOfEnemies:3
    e = {'rect': pygame.Rect(600, 260, 50, 60), 'vel': -5, 'health': 100}
    return e