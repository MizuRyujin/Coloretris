import pygame
import piece


class Board:
    grid_size = (0, 0)
    cell_size = (0, 0)
    game_grid = []
    board_origin = (0, 0)

    def __init__(self, grid_size, cell_size, origin) -> None:
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.board_origin = origin

    def fill_board(self, screen_res_with_offset):
        y_screen_pos = self.board_origin[1]
        for y in range(0, self.grid_size[0]):
            aux = []
            x_screen_pos = self.board_origin[0]
            for x in range(0, self.grid_size[1]):
                aux.append([(x_screen_pos, y_screen_pos), None])
                x_screen_pos = x_screen_pos + self.cell_size[0] if not x_screen_pos + \
                    self.cell_size[0] > screen_res_with_offset[0] else self.board_origin[0]

            self.game_grid.append(aux)
            y_screen_pos = y_screen_pos + self.cell_size[1] if not y_screen_pos + \
                self.cell_size[1] > screen_res_with_offset[1] else self.board_origin[1]

    def add_piece(self, piece):
        for row in range(0, len(self.game_grid)):
            x = 0
            for column in self.game_grid[row]:
                column.pop()
                piece.position = column[0]
                piece.grid_position = (x, row)
                column.append(piece)
                x += 1

    def get_board(self):
        return self.game_grid

    def draw_board():
        pass
