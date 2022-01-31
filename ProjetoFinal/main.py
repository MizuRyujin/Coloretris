import pygame
import piece
import board


# Initialize pygame
pygame.init()

# GLOBAL VARS
board_rows = 10
board_columns = 7
screen_width = 1280
screen_height = 720
screen_res = (screen_width, screen_height)
board_width = screen_width / board_columns
board_height = screen_height / board_rows
cell_size = 100

screen = pygame.display.set_mode(screen_res)


# Initialize Assets -> path: "ProjetoFinal/Assets/<AssetName>"
font = pygame.freetype.Font("ProjetoFinal/Assets/NotoSans-Regular.ttf", 16)
sprite = pygame.image.load("ProjetoFinal/Assets/EggBlue.png")

# Reduce piece scale
# sprite_size = sprite.get_size()
# sprite_scale = (sprite_size[0] / board_width,
#                 sprite_size[1] / board_height)
# sprite = pygame.transform.scale(sprite, (sprite.get_size()[0] - sprite.get_size(
# )[0] * sprite_scale[0], sprite.get_size()[1] - sprite.get_size()[1] * sprite_scale[1]))

# Create "prefab" of game piece
piece_prefab = piece.Piece(0)
piece_prefab.sprite = sprite

# Initialize grid (screen size / sprite size)
board_screen_pos = (
    (board_width / 3) * 1.5, board_height / 5)

board = board.Board(
    (10, 7), (boa + 10, cell_size + 10), board_screen_pos)
board.create_board(board_width, board_height)
board.add_piece(piece_prefab)


# Retrieve the amount of time since pygame.init() was called
last_time = pygame.time.get_ticks() / 1000

while True:
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
    screen.fill((70, 70, 70))
    board.draw_board(screen)

    # Swaps the back and front buffer, effectively displaying what we rendered
    pygame.display.flip()
