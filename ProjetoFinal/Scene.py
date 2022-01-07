import pygame

class Scene:
    def __init__(self) -> None:
        self.pieces = []
    
    def add_game_object(self, Piece):
        self.pieces.append(Piece)