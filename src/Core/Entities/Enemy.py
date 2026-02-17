#should inherit the class (maybe its called Object) that pygame uses, and has the function
#update(dt)
class Enemy:
    def rect 
    def vel
    def health
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