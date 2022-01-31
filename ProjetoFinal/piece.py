import pygame
 
class Piece:

    def __init__(self, color):
        self.name = "piece"
        self.pos_x = 0
        self.pos_y = 0
        self.sprite = None
        self.color = color
