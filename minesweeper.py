<<<<<<< HEAD
from string import ascii_lowercase,digits
from random import randint
def set_grid(grid_size=10,numberofmines=15):
    empty_grid = [[0 for i in range(grid_size)] for i in range(grid_size)]
    global show
    show = [[False for i in range(grid_size)] for i in range(grid_size)]
    show_grid(empty_grid)
    mines = getmines(grid_size,numberofmines)
    for x,y in mines:
        empty_grid[x][y]='X'
    empty_grid = setnumbers(empty_grid)
    return empty_grid
def setnumbers(grid):
    grid_size = len(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j]=='X':
                if i-1>=0 and j-1>=0 and grid[i-1][j-1]!='X':
                    grid[i-1][j-1]+=1
                if i-1>=0 and j>=0 and grid[i-1][j]!='X':
                    grid[i-1][j]+=1
                if i-1>=0 and j+1<grid_size and grid[i-1][j+1]!='X':
                    grid[i-1][j+1]+=1
                if i>=0 and j-1>=0 and grid[i][j-1]!='X':
                    grid[i][j-1]+=1
                if i>=0 and j+1<grid_size and grid[i][j+1]!='X':
                    grid[i][j+1]+=1
                if i+1<grid_size and j-1>=0 and grid[i+1][j-1]!='X':
                    grid[i+1][j-1]+=1
                if i+1<grid_size and j>=0 and grid[i+1][j]!='X':
                    grid[i+1][j]+=1
                if i+1<grid_size and j+1<grid_size and grid[i+1][j+1]!='X':
                    grid[i+1][j+1]+=1
    return grid
def getmines(grid_size,numberofmines=15):
    mines = []
    while numberofmines>0:
        cell = getcell(grid_size)
        if cell in mines:
            continue
        else:
            mines.append(cell)
            numberofmines-=1
    return mines
def getcell(grid_size):
    x = randint(0,grid_size-1)
    y = randint(0,grid_size-1)
    return [x,y]
def show_grid(grid):
    grid_size = len(grid)
    toplabel = '    '
    for i in ascii_lowercase[:grid_size]:
        toplabel+=i+'   '
    print(toplabel)
    for i in range(grid_size):
        s = str(i)+' | '
        for j in range(grid_size):
            if not show[i][j]:
                s+=' '+' | '
            else:
                s+=str(grid[i][j])+' | '
        horizontal = '----'*grid_size
        print('   '+horizontal)
        print(s)
    print('   '+horizontal)
def play_game(grid_size=10,numberofmines=15):
    print('Type the column followed by the row (eg. a5).')
    grid = set_grid(grid_size,numberofmines)
    global show
    while True:
        print('Enter Cell :',end=' ')
        cell = input()
        if (cell[0] in ascii_lowercase[:grid_size]) and (cell[1] in digits[:grid_size]) and (len(cell)==2):
            row=int(cell[1])
            col=ord(cell[0])-ord('a')
            if grid[row][col]=='X':
                print('Oops! Thats a Mine! Game Over.')
                show = [[True]*grid_size]*grid_size
                show_grid(grid)
                break
            else:
                resetgrid(grid,row,col)
        else:
            print('Invalid Cell')
            continue
        show_grid(grid)
        count = sum([row.count(False) for row in show])
        print('Remaining Cells :',count,'Mines :',numberofmines)
        if count<=numberofmines:
            print('Congratulation. YOU WON!')
            break
def resetgrid(grid,row,col):
    global show
    grid_size=len(grid)
    if grid[row][col]==0:
        empty_neighbours=[[row,col]]
        show[row][col]=True
        for i,j in empty_neighbours:
            if i-1>=0 and j-1>=0 and grid[i-1][j-1]!='X':
                if grid[i-1][j-1]==0 and [i-1,j-1] not in empty_neighbours:
                    empty_neighbours.append([i-1,j-1])
                show[i-1][j-1]=True
            if i-1>=0 and j>=0 and grid[i-1][j]!='X':
                if grid[i-1][j]==0 and [i-1,j] not in empty_neighbours:
                    empty_neighbours.append([i-1,j])
                show[i-1][j]=True
            if i-1>=0 and j+1<grid_size and grid[i-1][j+1]!='X':
                if grid[i-1][j+1]==0 and [i-1,j+1] not in empty_neighbours:
                    empty_neighbours.append([i-1,j+1])
                show[i-1][j+1]=True
            if i>=0 and j-1>=0 and grid[i][j-1]!='X':
                if grid[i][j-1]==0 and [i,j-1] not in empty_neighbours:
                    empty_neighbours.append([i,j-1])
                show[i][j-1]=True
            if i>=0 and j+1<grid_size and grid[i][j+1]!='X':
                if grid[i][j+1]==0 and [i,j+1] not in empty_neighbours:
                    empty_neighbours.append([i,j+1])
                show[i][j+1]=True
            if i+1<grid_size and j-1>=0 and grid[i+1][j-1]!='X':
                if grid[i+1][j-1]==0 and [i+1,j-1] not in empty_neighbours:
                    empty_neighbours.append([i+1,j-1])
                show[i+1][j-1]=True
            if i+1<grid_size and j>=0 and grid[i+1][j]!='X':
                if grid[i+1][j]==0 and [i+1,j] not in empty_neighbours:
                    empty_neighbours.append([i+1,j])
                show[i+1][j]=True
            if i+1<grid_size and j+1<grid_size and grid[i+1][j+1]!='X':
                if grid[i+1][j+1]==0 and [i+1,j+1] not in empty_neighbours:
                    empty_neighbours.append([i+1,j+1])
                show[i+1][j+1]=True
    else:
        show[row][col]=True
play_game(grid_size=10,numberofmines=15)
=======
from string import ascii_lowercase,digits
from random import randint
def set_grid(grid_size=10,numberofmines=15):
    empty_grid = [[0 for i in range(grid_size)] for i in range(grid_size)]
    global show
    show = [[False for i in range(grid_size)] for i in range(grid_size)]
    show_grid(empty_grid)
    mines = getmines(grid_size,numberofmines)
    for x,y in mines:
        empty_grid[x][y]='•'
    empty_grid = setnumbers(empty_grid)
    return empty_grid
def setnumbers(grid):
    grid_size = len(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j]=='•':
                if i-1>=0 and j-1>=0 and grid[i-1][j-1]!='•':
                    grid[i-1][j-1]+=1
                if i-1>=0 and j>=0 and grid[i-1][j]!='•':
                    grid[i-1][j]+=1
                if i-1>=0 and j+1<grid_size and grid[i-1][j+1]!='•':
                    grid[i-1][j+1]+=1
                if i>=0 and j-1>=0 and grid[i][j-1]!='•':
                    grid[i][j-1]+=1
                if i>=0 and j+1<grid_size and grid[i][j+1]!='•':
                    grid[i][j+1]+=1
                if i+1<grid_size and j-1>=0 and grid[i+1][j-1]!='•':
                    grid[i+1][j-1]+=1
                if i+1<grid_size and j>=0 and grid[i+1][j]!='•':
                    grid[i+1][j]+=1
                if i+1<grid_size and j+1<grid_size and grid[i+1][j+1]!='•':
                    grid[i+1][j+1]+=1
    return grid
def getmines(grid_size,numberofmines=15):
    mines = []
    while numberofmines>0:
        cell = getcell(grid_size)
        if cell in mines:
            continue
        else:
            mines.append(cell)
            numberofmines-=1
    return mines
def getcell(grid_size):
    x = randint(0,grid_size-1)
    y = randint(0,grid_size-1)
    return [x,y]
def show_grid(grid):
    grid_size = len(grid)
    toplabel = '    '
    for i in ascii_lowercase[:grid_size]:
        toplabel+=i+'   '
    print(toplabel)
    for i in range(grid_size):
        s = str(i)+' | '
        for j in range(grid_size):
            if not show[i][j]:
                s+=' '+' | '
            else:
                s+=str(grid[i][j])+' | '
        horizontal = '----'*grid_size
        print('   '+horizontal)
        print(s)
    print('   '+horizontal)
def play_game(grid_size=10,numberofmines=15):
    print('Type the column followed by the row (eg. a5).')
    grid = set_grid(grid_size,numberofmines)
    global show
    while True:
        print('Enter Cell :',end=' ')
        cell = input()
        if (cell[0] in ascii_lowercase[:grid_size]) and (cell[1] in digits[:grid_size]) and (len(cell)==2):
            row=int(cell[1])
            col=ord(cell[0])-ord('a')
            if grid[row][col]=='•':
                print('Oops! Thats a Mine! Game Over.')
                show = [[True]*grid_size]*grid_size
                show_grid(grid)
                break
            else:
                resetgrid(grid,row,col)
        else:
            print('Invalid Cell')
            continue
        show_grid(grid)
        count = sum([row.count(False) for row in show])
        print('Remaining Cells :',count,'Mines :',numberofmines)
        if count<=numberofmines:
            print('Congratulation. YOU WON!')
            break
def resetgrid(grid,row,col):
    global show
    grid_size=len(grid)
    if grid[row][col]==0:
        empty_neighbours=[[row,col]]
        show[row][col]=True
        for i,j in empty_neighbours:
            if i-1>=0 and j-1>=0 and grid[i-1][j-1]!='•':
                if grid[i-1][j-1]==0 and [i-1,j-1] not in empty_neighbours:
                    empty_neighbours.append([i-1,j-1])
                show[i-1][j-1]=True
            if i-1>=0 and j>=0 and grid[i-1][j]!='•':
                if grid[i-1][j]==0 and [i-1,j] not in empty_neighbours:
                    empty_neighbours.append([i-1,j])
                show[i-1][j]=True
            if i-1>=0 and j+1<grid_size and grid[i-1][j+1]!='•':
                if grid[i-1][j+1]==0 and [i-1,j+1] not in empty_neighbours:
                    empty_neighbours.append([i-1,j+1])
                show[i-1][j+1]=True
            if i>=0 and j-1>=0 and grid[i][j-1]!='•':
                if grid[i][j-1]==0 and [i,j-1] not in empty_neighbours:
                    empty_neighbours.append([i,j-1])
                show[i][j-1]=True
            if i>=0 and j+1<grid_size and grid[i][j+1]!='•':
                if grid[i][j+1]==0 and [i,j+1] not in empty_neighbours:
                    empty_neighbours.append([i,j+1])
                show[i][j+1]=True
            if i+1<grid_size and j-1>=0 and grid[i+1][j-1]!='•':
                if grid[i+1][j-1]==0 and [i+1,j-1] not in empty_neighbours:
                    empty_neighbours.append([i+1,j-1])
                show[i+1][j-1]=True
            if i+1<grid_size and j>=0 and grid[i+1][j]!='•':
                if grid[i+1][j]==0 and [i+1,j] not in empty_neighbours:
                    empty_neighbours.append([i+1,j])
                show[i+1][j]=True
            if i+1<grid_size and j+1<grid_size and grid[i+1][j+1]!='•':
                if grid[i+1][j+1]==0 and [i+1,j+1] not in empty_neighbours:
                    empty_neighbours.append([i+1,j+1])
                show[i+1][j+1]=True
    else:
        show[row][col]=True
play_game(grid_size=9,numberofmines=10)
>>>>>>> 733c93de6b0dbb07a4fe54644187b1e880619501
