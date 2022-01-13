import pygame

import piece
import board


# Initialize pygame
pygame.init()

screen_res = (1280, 720)
screen_res_with_offset = (screen_res[0] - 100, screen_res[1] - 100)
screen = pygame.display.set_mode(screen_res)

# Retrieve the ammount of time since pygame.init() was called
last_time = pygame.time.get_ticks() / 1000

# Initialize Assets -> path: "ProjetoFinal/Assets/<AssetName>"
font = pygame.freetype.Font("ProjetoFinal/Assets/NotoSans-Regular.ttf", 16)
piece_sprite = pygame.image.load("ProjetoFinal/Assets/EggBlue.png")

# Reduce piece scale
sprite_size = piece_sprite.get_size()
sprite_scale = (sprite_size[0] / screen_res_with_offset[0],
                sprite_size[1] / screen_res_with_offset[1])
piece_sprite = pygame.transform.scale(piece_sprite, (piece_sprite.get_size()[0] - piece_sprite.get_size(
)[0] * sprite_scale[0], piece_sprite.get_size()[1] - piece_sprite.get_size()[1] * sprite_scale[1]))

# Create "prefab" of game piece
piece_prefab = piece.Piece()
piece_prefab.sprite = piece_sprite

# Initialize grid (screen size / sprite size)
board_screen_pos = (
    (screen_res_with_offset[1] / 3) * 1.5, screen_res_with_offset[1] / 5)

board = board.Board((10, 7), (sprite_size[0] + 10, sprite_size[1] + 10), board_screen_pos)
board.fill_board(screen_res_with_offset)
board.add_piece(piece_prefab)

# Initialize scene collection

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
