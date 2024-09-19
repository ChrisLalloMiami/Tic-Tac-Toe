def printGrid(grid: list) -> None:
    print(
        f'-----------\n'
        f' {grid[0][0]} | {grid[0][1]} | {grid[0][2]} \n'
        f'-----------\n'
        f' {grid[1][0]} | {grid[1][1]} | {grid[1][2]} \n'
        f'-----------\n'
        f' {grid[2][0]} | {grid[2][1]} | {grid[2][2]} \n'
        f'-----------\n'
    )

def checkForWin(grid: list, role: str) -> bool:
    # Vertical wins
    if grid[0][0] == role and grid[1][0] == role and grid[2][0] == role:
        return True
    if grid[0][1] == role and grid[1][1] == role and grid[2][1] == role:
        return True
    if grid[0][2] == role and grid[1][2] == role and grid[2][2] == role:
        return True
    
    # Horizontal wins
    if grid[0][0] == role and grid[0][1] == role and grid[0][2] == role:
        return True
    if grid[1][0] == role and grid[1][1] == role and grid[1][2] == role:
        return True
    if grid[2][0] == role and grid[2][1] == role and grid[2][2] == role:
        return True
    
    # Diagonal wins
    if grid[0][0] == role and grid[1][1] == role and grid[2][2] == role:
        return True
    if grid[0][2] == role and grid[1][1] == role and grid[2][0] == role:
        return True
    
    return False

def isCenter(row: int, col: int) -> bool:
    if row == 1 and col == 1:
        return True
    return False

def isCorner(row: int, col: int) -> bool:
    if row == 0 and col == 0:
        return True
    if row == 0 and col == 2:
        return True
    if row == 2 and col == 0:
        return True
    if row == 2 and col == 2:
        return True
    return False

def isEdge(row: int, col: int) -> bool:
    if row == 0 and col == 1:
        return True
    if row == 1 and col == 0:
        return True
    if row == 1 and col == 2:
        return True
    if row == 2 and col == 1:
        return True
    return False

def isBlock(grid: list, AI_role: str, row: int, col: int) -> bool:
    '''
    '''
