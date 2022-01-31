from piece_color import PieceColor

class Board:

    def __init__(self, grid_columns, grid_rows, cell_size, origin) -> None:
        self.grid_columns = grid_columns
        self.grid_rows = grid_rows
        self.cell_size = cell_size
        self.board_origin = origin
        self.fixed_positions = []

    def create_board(self):
        self.game_grid = [[PieceColor.NONE for i in range(
            self.grid_columns)] for i in range(self.grid_rows)]

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