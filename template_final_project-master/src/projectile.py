import pygame
class Projectile(pygame.sprite.Sprite):
    Size = 10
    def __init__(self, x, y, x_speed, y_speed, color=pygame.Color('red')):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.color = color
        
    def hitbox(self):
        return pygame.Rect(self.x, self.y, Projectile.Size, Projectile.Size)
    
    def tick(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, Projectile.Size, Projectile.Size))
        
   