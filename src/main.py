from constants import *
from funcs import *

# The active play grid
grid = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

player_role = '' # The player's role (X or O)
AI_role = ''     # The AI's role (X or O)
open_moves = 9   # The number of remaining moves on the board (0 - 9)

# Let player choose X's or O's
while player_role != 'X' and player_role != 'O':
    player_role = input('Player: Select your role (X or O): ').strip().upper()
    if player_role != 'X' and player_role != 'O':
        print('Please select either X or O\n')
        continue
    print(f'You selected {player_role}\'s\n')
    
    # Set AI role
    if player_role == 'X':
        AI_role = 'O'
    else:
        AI_role = 'X'

# Print an empty grid
printGrid(grid)

# Run game
while True:
    # Get user's location to play
    loc = input(f'Select a location to place an {player_role} in the form "0 0": ').strip().split()
    real_row = int(loc[0])
    real_col = int(loc[1])
    row = real_row - 1
    col = real_col - 1

    # Check input
    if row > 2 or row < 0 or col > 2 or col < 0:
        print('Please enter rows/columns within the bounds [1, 3]\n')
        continue
    
    # Try to fill requested location in grid
    if grid[row][col] == '-':
        grid[row][col] = player_role
        print(f'Played an {player_role} in ({real_row}, {real_col})')
        open_moves -= 1
    else:
        print(f'({real_row}, {real_col}) occupied by an {grid[row][col]}')
        continue

    # Print updated grid
    printGrid(grid)

    # Check for player win
    player_win = checkForWin(grid, player_role)
    if player_win:
        print('Player wins')
        exit()
    
