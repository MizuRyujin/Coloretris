import random
from turtle import color, update
import pygame

from enum import Enum

## CLASSES SHOULD BE MOVED TO INDIVIDUAL FILES !! ##


class PieceColor(Enum):
    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


class Board:

    def __init__(self, grid_columns, grid_rows, cell_size, origin) -> None:
        self.grid_columns = grid_columns
        self.grid_rows = grid_rows
        self.cell_size = cell_size
        self.board_origin = origin

    def create_board(self):
        self.game_grid = [[PieceColor.NONE for x in range(
            self.grid_columns)] for y in range(self.grid_rows)]

    def update_board(self, piece):
        new_grid = []
        for y, row in enumerate(self.game_grid):
            for x, column in enumerate(row):            
                if(y, x) == (piece.pos_y, piece.pos_x):
                    self.game_grid[y][x] = piece.color
            



class Piece:

    def __init__(self, color):
        self.name = "piece"
        self.pos_x = 0
        self.pos_y = 0
        self.sprite = None
        self.color = color


# Initialize pygame
pygame.init()

# GLOBAL VARS
# Screen
screen_width = 1280
screen_height = 720
screen_res = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_res)
pygame.display.set_caption("Coloretris!!")

# Board
board_rows = 10
board_columns = 7
cell_size = 50

board_width = cell_size * board_columns
board_height = cell_size * board_rows

top_left_x = (screen_width - board_width) // 2
top_left_y = screen_height - board_height
board = Board(board_columns, board_rows, cell_size, (top_left_x, top_left_y))

# Initialize Assets -> path: "ProjetoFinal/Assets/<AssetName>"
font = pygame.freetype.Font("ProjetoFinal/Assets/NotoSans-Regular.ttf", 16)
sprite = pygame.image.load("ProjetoFinal/Assets/EggBlue.png")
sprite.convert()

# Color dictionary
color_dict = {
    "base": (10, 10, 10),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}


def gameloop():
    global board
    global screen

    clock = pygame.time.Clock()
    last_time = pygame.time.get_ticks() / 1000
    board.create_board()
    
    current_piece = get_new_piece()
    while True:
        clock.tick(60)
        # Process system events (Put this in a input manager)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
        elapsed_time = (pygame.time.get_ticks() - last_time)
        # Display menu scene
        # If Start option was selected load game scene

        # Display game scene
        # Start game loop

        # Clears the screen to black
        board.update_board(current_piece)
        draw_board(board, screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


def main_menu():
    pass

def get_new_piece():
    return Piece(get_random_color())

def get_random_color():
    # Force random choice to disregard NONE value
    color = random.choice(list(PieceColor)[1:])
    return color


def draw_grid(board, screen):
    # This function draws the grey grid lines that we see
    sx = top_left_x
    sy = top_left_y
    for i in range(board.grid_rows):
        s1 = (sx, sy + i * board.cell_size)
        e1 = (sx + board_width, sy + i * board.cell_size)
        pygame.draw.line(screen, (128, 128, 128), s1, e1)  # horizontal lines
        for j in range(board.grid_columns + 1):
            s2 = (sx + j * board.cell_size, sy)
            e2 = (sx + j * board.cell_size, sy + board_height)
            pygame.draw.line(screen, (128, 128, 128), s2, e2)


def draw_board(board, screen):
    screen.fill(color_dict.get("base"))
    draw_grid(board, screen)
    for y, row in enumerate(board.game_grid):
        row = list(row)
        for x, column in enumerate(row):
            if column == PieceColor.RED:
                pygame.draw.rect(screen, color_dict.get("red"), ( top_left_x + x * board.cell_size, top_left_y + y * board.cell_size, board.cell_size, board.cell_size), 0)
            if column == PieceColor.GREEN:         
                pygame.draw.rect(screen, color_dict.get("green"), (top_left_x + x * board.cell_size, top_left_y + y * board.cell_size, board.cell_size, board.cell_size), 0)
            if column == PieceColor.BLUE:
                pygame.draw.rect(screen, color_dict.get("blue"), (top_left_x + x * board.cell_size, top_left_y + y * board.cell_size, board.cell_size, board.cell_size), 0)



gameloop()
