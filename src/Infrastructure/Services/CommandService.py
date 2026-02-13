class CommandService:
    #This is the map of all keys to the actions expected
    def KeyMap
    #This used to be MapKeysToAction but that's a misnomer cause that means setting the 
    #keys to actions, not actually firing them to perform as expected in game
    #If you want to actually map keys to action you can just create an enum
    def FirePlayerCommands(player):
    keys = pygame.key.get_pressed()
        player.handle_input(keys, dt)
    switch KeyMap:
    1: player.attack()
    2:player.dodge()
    3:player.parry()
    4:player.throw()
        player.update(dt)
