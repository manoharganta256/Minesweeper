from string import ascii_lowercase, digits
from random import randint
import sys


def set_grid(grid_size, numberofmines):
    empty_grid = [[0 for i in range(grid_size)] for i in range(grid_size)]
    global show
    show = [[False for i in range(grid_size)] for i in range(grid_size)]
    show_grid(empty_grid)
    mines = getmines(grid_size, numberofmines)
    for x, y in mines:
        empty_grid[x][y] = '•'
    empty_grid = setnumbers(empty_grid)
    return empty_grid


def setnumbers(grid):
    grid_size = len(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == '•':
                if i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] != '•':
                    grid[i-1][j-1] += 1
                if i-1 >= 0 and j >= 0 and grid[i-1][j] != '•':
                    grid[i-1][j] += 1
                if i-1 >= 0 and j+1 < grid_size and grid[i-1][j+1] != '•':
                    grid[i-1][j+1] += 1
                if i >= 0 and j-1 >= 0 and grid[i][j-1] != '•':
                    grid[i][j-1] += 1
                if i >= 0 and j+1 < grid_size and grid[i][j+1] != '•':
                    grid[i][j+1] += 1
                if i+1 < grid_size and j-1 >= 0 and grid[i+1][j-1] != '•':
                    grid[i+1][j-1] += 1
                if i+1 < grid_size and j >= 0 and grid[i+1][j] != '•':
                    grid[i+1][j] += 1
                if i+1 < grid_size and j+1 < grid_size and grid[i+1][j+1] != '•':
                    grid[i+1][j+1] += 1
    return grid


def getmines(grid_size, numberofmines=15):
    mines = []
    while numberofmines > 0:
        cell = getcell(grid_size)
        if cell in mines:
            continue
        else:
            mines.append(cell)
            numberofmines -= 1
    return mines


def getcell(grid_size):
    x = randint(0, grid_size-1)
    y = randint(0, grid_size-1)
    return [x, y]


def show_grid(grid):
    grid_size = len(grid)
    toplabel = '    '
    for i in range(grid_size):
        toplabel += str(i)
        if i > 9:
            toplabel += '  '
        else:
            toplabel += '   '
    print(toplabel)
    horizontal = ''
    for i in range(grid_size):
        s = ascii_lowercase[i]+' | '
        for j in range(grid_size):
            if not show[i][j]:
                s += ' '+' | '
            else:
                s += str(grid[i][j])+' | '
        horizontal = '----'*grid_size
        print('   '+horizontal)
        print(s)
    print('   '+horizontal)


def play_game(grid_size=10, numberofmines=15):
    print('Type the row followed by the column (eg. a5).')
    grid = set_grid(grid_size, numberofmines)
    global show
    while True:
        print('Enter Cell(q to Quit) :', end=' ')
        cell = input()
        if cell == 'q':
            sys.exit(0)
        if (cell[0] in ascii_lowercase[:grid_size]) and (int(cell[1:]) < grid_size) and (len(cell) == 2 or 3):
            col = int(cell[1:])
            row = ord(cell[0])-ord('a')
            if grid[row][col] == '•':
                print('Oops! Thats a Mine! Game Over.')
                show = [[True]*grid_size]*grid_size
                show_grid(grid)
                break
            else:
                resetgrid(grid, row, col)
        else:
            print('Invalid Cell')
            continue
        show_grid(grid)
        count = sum([row.count(False) for row in show])
        print('Remaining Cells :', count, 'Mines :', numberofmines)
        if count <= numberofmines:
            print('Congratulation. YOU WON!')
            break


def resetgrid(grid, row, col):
    global show
    grid_size = len(grid)
    if grid[row][col] == 0:
        empty_neighbours = [[row, col]]
        show[row][col] = True
        for i, j in empty_neighbours:
            if i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] != '•':
                if grid[i-1][j-1] == 0 and [i-1, j-1] not in empty_neighbours:
                    empty_neighbours.append([i-1, j-1])
                show[i-1][j-1] = True
            if i-1 >= 0 and j >= 0 and grid[i-1][j] != '•':
                if grid[i-1][j] == 0 and [i-1, j] not in empty_neighbours:
                    empty_neighbours.append([i-1, j])
                show[i-1][j] = True
            if i-1 >= 0 and j+1 < grid_size and grid[i-1][j+1] != '•':
                if grid[i-1][j+1] == 0 and [i-1, j+1] not in empty_neighbours:
                    empty_neighbours.append([i-1, j+1])
                show[i-1][j+1] = True
            if i >= 0 and j-1 >= 0 and grid[i][j-1] != '•':
                if grid[i][j-1] == 0 and [i, j-1] not in empty_neighbours:
                    empty_neighbours.append([i, j-1])
                show[i][j-1] = True
            if i >= 0 and j+1 < grid_size and grid[i][j+1] != '•':
                if grid[i][j+1] == 0 and [i, j+1] not in empty_neighbours:
                    empty_neighbours.append([i, j+1])
                show[i][j+1] = True
            if i+1 < grid_size and j-1 >= 0 and grid[i+1][j-1] != '•':
                if grid[i+1][j-1] == 0 and [i+1, j-1] not in empty_neighbours:
                    empty_neighbours.append([i+1, j-1])
                show[i+1][j-1] = True
            if i+1 < grid_size and j >= 0 and grid[i+1][j] != '•':
                if grid[i+1][j] == 0 and [i+1, j] not in empty_neighbours:
                    empty_neighbours.append([i+1, j])
                show[i+1][j] = True
            if i+1 < grid_size and j+1 < grid_size and grid[i+1][j+1] != '•':
                if grid[i+1][j+1] == 0 and [i+1, j+1] not in empty_neighbours:
                    empty_neighbours.append([i+1, j+1])
                show[i+1][j+1] = True
    else:
        show[row][col] = True


if __name__ == '__main__':
    print("1. Grid Size = 9\n2.Grid Size = 16\n3.Custom\nYour Choice: ",end = "")
    choice = int(input())
    grid_size = None
    numberofmines = None
    if choice == 1:
        grid_size = 9
        numberofmines = 10
        play_game(grid_size, numberofmines)
    elif choice == 2:
        grid_size = 16
        numberofmines = 40
        play_game(grid_size, numberofmines)
    elif choice == 3:
        grid_size = int(input("Enter Grid Size: "))
        numberofmines = int(input("Enter numberofmines: "))
        play_game(grid_size, numberofmines)
    else:
        print("I think you don't wanna play")
