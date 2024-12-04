import pygame
import random
from projectile import Projectile
class Enemy:
    Speed = 5
    Size = 20
    def __init__(self, x, y, enemy_size_x, enemy_size_y):
        self.x = x
        self.y = y
        self.enemy_size_x = enemy_size_x
        self.enemy_size_y = enemy_size_y
    
    def hitbox(self):
        return pygame.Rect(self.x, self.y, Enemy.Size, Enemy.Size)
    
    def tick(self):
        self.x = 1
        """
        Initializes the enemy object
        Args:
            x (int): starting x coordinate
            y (int): starting y coordinate
            img_file (str): path to img file
        """
        
    def shoot(self):
        """
        creates an enemy projectile
        args: None
        return: Bullet
        """