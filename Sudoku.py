
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
def possible(grid, y, x, n):
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(grid,y,x,n):
                        grid[y][x] = n
                        solve(grid)
                        grid[y][x] = 0
                return

    print_board(grid)
    input("more?")

def print_board(board):
    print("--------start--------")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("--------------------")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="") 

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

#print_board(grid)
solve(grid)    
