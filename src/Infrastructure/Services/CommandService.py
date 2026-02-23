import pygame

class CommandService:
    KEY_MAP = {
        pygame.K_SPACE: 'attack',
        pygame.K_LSHIFT: 'dodge',
        pygame.K_e: 'parry',
        pygame.K_q: 'throw'
    }
    
    @staticmethod
    def FirePlayerCommands(player, dt):
        keys = pygame.key.get_pressed()
        player.handle_input(keys, dt)
        
        for key, action in CommandService.KEY_MAP.items():
            if keys[key]:
                if action == 'attack':
                    player.attack()
                elif action == 'dodge':
                    player.dodge()
                elif action == 'parry':
                    player.parry()
                elif action == 'throw':
                    player.throw()
        
        player.update(dt)