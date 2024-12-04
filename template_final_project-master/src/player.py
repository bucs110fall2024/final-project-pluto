import pygame
class Player:
    Speed = 5
    Size = 10
    def __init__(self, x, y, player_size_x, player_size_y):
        self.x = x
        self.y = y
        self.player_size_x = player_size_x
        self.player_size_y = player_size_y
        self.alive = True
        
    def hitbox(self):
        return pygame.Rect(self.x, self.y, Player.Size, Player.Size)
        
        """_summary_
        Initializes the player character
        Args:
            x (int): starting x coordinate
            y (int): starting y coordinate
            img_file (str): path to img file
        """
    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x = max(0, min(self.x - Player.Speed,self.player_size_x - Player.Size))
            
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x = max(0, min(self.x + Player.Speed, self.player_size_x - Player.Size ))
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y = max(0, min(self.y - Player.Speed, self.player_size_y - Player.Size))
        
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y = max(0, min(self.y + Player.Speed, self.player_size_y - Player.Size))
        
    def draw(self, surface):
        if self.alive:
            color = (pygame.Color('white') if self.alive
                     else pygame.Color('black'))
            pygame.draw.rect(surface, color, (self.x, self.y, Player.Size, Player.Size))
    
    def move_right(self):
        """
        moves position right by 1
        args: None
        return: None
        """
        
    def move_left(self):
        """
        moves position left by 1
        args: None
        return: None
        """
    
    def move_up(self):
        """
        moves position up by 1
        args: None
        return: None
        """
        
    def move_down(self):
        """
        moves position down by 1
        args: None
        return: None
        """
        
    def shoot_straight(self):
        """
        creates a bullet object ahead of the player
        args: None
        return: Bullet
        """
        
    def shoot_homing(self):
        """
        creates a homing bullet ahead of the player
        args: None
        return: Bullet
        """