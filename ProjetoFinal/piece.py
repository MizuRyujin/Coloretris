import pygame

class Piece:

    def __init__(self):
        self.name = "piece"
        self.grid_position = (0,0)
        self.position = (0,0)
        self.sprite = None
    
    def render(self, screen):
        screen.blit(self.sprite,
                        (self.position[0], self.position[1]))
    
    def move():
        pass
