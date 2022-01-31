import enum
import random
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
        self.fixed_positions = []

    def create_board(self):
        self.game_grid = [[PieceColor.NONE for x in range(
            self.grid_columns)] for y in range(self.grid_rows)]

    def update_board(self, piece):
        for y, row in enumerate(self.game_grid):
            for x in range(len(row)):
                piece_pos = (piece.pos_y, piece.pos_x)
                if(y, x) == piece_pos:
                    self.game_grid[y][x] = piece.color
                elif self.fixed_positions.count(piece_pos) == 0 and self.fixed_positions.count((y, x)) == 0:
                    self.game_grid[y][x] = PieceColor.NONE

    def add_fixed_piece(self, position):
        self.fixed_positions.append(position)


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

    is_running = True
    should_get_new_piece = False
    clock = pygame.time.Clock()

    fall_speed = 1
    fall_time = clock.get_time() / 1000

    board.create_board()

    current_piece = get_new_piece()

    # Commence the actual game loop
    while is_running:
        clock.tick(60)
        fall_time += clock.get_time() / 1000

        if fall_time >= fall_speed:
            fall_time = 0
            current_piece.pos_y += 1
            if not valid_space(current_piece, board) and current_piece.pos_y > 0:
                current_piece.pos_y -= 1
                board.add_fixed_piece(
                    (current_piece.pos_y, current_piece.pos_x))
                should_get_new_piece = True

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.pos_x -= 1
                    if not valid_space(current_piece, board):
                        current_piece.pos_x += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.pos_x += 1
                    if not valid_space(current_piece, board):
                        current_piece.pos_x -= 1

                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.pos_y += 1
                    if not valid_space(current_piece, board):
                        current_piece.pos_y -= 1

        # Update board with new piece position
        board.update_board(current_piece)

        # If the current piece has hit something
        if should_get_new_piece:
            board.add_fixed_piece((current_piece.pos_y, current_piece.pos_x))
            current_piece = get_new_piece()
            should_get_new_piece = False
            clear_same_colour_cells(board)

        draw_board(board, screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # If the next piece is on a occupied space in the first row, lose
        if check_lost(board, (current_piece.pos_y, current_piece.pos_x)):
            is_running = False

    # When gameloop is terminated return to main menu
    main_menu()


def main_menu():
    # Display menu scene
    # If Start option was selected load game scene
    run_menu = True
    screen.fill(color_dict.get("base"))
    while run_menu:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run_menu = False
                pygame.display.quit()
                quit()
    
    pygame.display.flip()


# Gameloop methods
# Gets a new piece of random color and set it to the center of the grid
def get_new_piece():
    piece = Piece(get_random_color())
    piece.pos_x = board_columns // 2
    return piece

# Gets a random color from color enum
def get_random_color():
    # Force random choice to disregard NONE value
    color = random.choice(list(PieceColor)[1:])
    return color

# Method to check if a piece is moving to a valid space
def valid_space(piece, board):
    piece_pos = (piece.pos_x, piece.pos_y)
    free_pos = []
    for y, row in enumerate(board.game_grid):
        for x, column in enumerate(row):
            if column == PieceColor.NONE:
                free_pos.append((x, y))  # save occupied pos to compare after
    if free_pos.count(piece_pos) > 0:
        return True
    else:
        return False

# Method to check if game is lost
def check_lost(board, pos):
    if board.fixed_positions.count(pos):
        return True
    return False

# Method to clear all cells with more than 3 neighbors of the same colour
def clear_same_colour_cells(board):
    for y in range(len(board.game_grid)-1, -1, -1):
        row = board.game_grid[y]
        for x in range(len(row)):
            pass
        # y_pos = y
        # for x, column in enumerate(row):
        #     x_pos = x

# Render methods
# Draws the actual game board with the pieces
def draw_board(board, screen):
    screen.fill(color_dict.get("base"))
    draw_grid(board, screen)
    for y, row in enumerate(board.game_grid):
        row = list(row)
        for x, column in enumerate(row):
            if column == PieceColor.RED:
                pygame.draw.rect(screen, color_dict.get("red"), (top_left_x + x * board.cell_size,
                                 top_left_y + y * board.cell_size, board.cell_size, board.cell_size), 0)
            if column == PieceColor.GREEN:
                pygame.draw.rect(screen, color_dict.get("green"), (top_left_x + x * board.cell_size,
                                 top_left_y + y * board.cell_size, board.cell_size, board.cell_size), 0)
            if column == PieceColor.BLUE:
                pygame.draw.rect(screen, color_dict.get("blue"), (top_left_x + x * board.cell_size,
                                 top_left_y + y * board.cell_size, board.cell_size, board.cell_size), 0)
    # Draw board border
    pygame.draw.rect(screen, (200, 200, 200), (top_left_x,
                     top_left_y, board_width, board_height), 5)

# This function draws the grey grid lines that we see
def draw_grid(board, screen):
    sx = top_left_x
    sy = top_left_y
    for i in range(board.grid_rows):
        s1 = (sx, sy + i * board.cell_size)
        e1 = (sx + board_width, sy + i * board.cell_size)
        pygame.draw.line(screen, (128, 128, 128), s1, e1)  # horizontal lines
        for j in range(board.grid_columns):
            s2 = (sx + j * board.cell_size, sy)
            e2 = (sx + j * board.cell_size, sy + board_height)
            pygame.draw.line(screen, (128, 128, 128), s2, e2)


# Main methods
gameloop()
