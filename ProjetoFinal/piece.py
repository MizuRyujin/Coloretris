import pygame

class Piece(object):
 
    def __init__(self, color):
        self.x = 0
        self.y = 0
        self.color = color
    
    def render(self, screen):
        screen.blit(self.sprite,
                        (self.position[0], self.position[1]))
    
    def move():
        pass
