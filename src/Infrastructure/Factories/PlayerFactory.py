from Core.Entities.Player import Player

class PlayerFactory:
    @staticmethod
    def CreatePlayer(x, y):
        if x < 0 or y < 0:
            raise ValueError("Position must be non-negative")
        p = Player(x, y)
        return p