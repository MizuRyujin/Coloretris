# Coloretris

This project is a implementation of Match-3 with Tetris game in Pygame.<br> Made for the class of Fundamentos de Programação, course Videojogos at Universidade Lusófona.<br>

Created by:
- [Miguel Fernández](https://github.com/MizuRyujin)

## Controls:
- Left and Right arrow key -> Move piece left or right on the board;
- Down arrow key -> Move piece faster;
- On main menu, press any key to begin

## References:
- [Pygame documentation](https://www.pygame.org/docs/)
- PowerPoint presentations by [Diogo De Andrade](https://github.com/DiogoDeAndrade) and [Phil Lopes](https://github.com/WorshipCookies)
- [Pygame classes](https://www.youtube.com/watch?v=7iZ5cJGjcgU&list=PLheBz0T_uVP2u0N3tNHlWQ6494JX_ZqQY&ab_channel=DiogoAndrade) by [Diogo De Andrade](https://github.com/DiogoDeAndrade)
- [Get random enum value](https://stackoverflow.com/questions/24243500/random-choice-on-enum)
- [Tetris in Pygame Tutorial](https://www.youtube.com/watch?v=uoR4ilCWwKA&list=WL&index=6&t=561s&ab_channel=TechWithTim) by [Tim Ruscica](https://github.com/techwithtim)
- [Pystroids](https://github.com/DiogoDeAndrade/Pysteroids) by [Diogo De Andrade](https://github.com/DiogoDeAndrade)

## Known issues
  - This project has a file named main_2.py. The reason for this is that when creating a build using pyinstaller for main.py, when running said build there's a traceback error saying "board module not found". This only happens when building main.py that has modules imported from respective files. <br> When building for main_2.py which has all the classes in the same file, the build is successful.
