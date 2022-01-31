import pygame

class Piece(object):
 
    def __init__(self, column, row, color):
        self.x = column
        self.y = row
        self.color = color
    
    def render(self, screen):
        screen.blit(self.sprite,
                        (self.position[0], self.position[1]))
    
    def move():
        pass
