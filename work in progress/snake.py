import random

size = int(input("size of the grid: "))

food = False
game = []

for i in range(size):
    row = []
    for i in range(size):
        row += [0]
    game.append(row)

game[random.randint(-1,size-1)][random.randint(-1,size-1)] = 1

def drawscreen(size,game,food):
    for i in range(-1,size-1):
        for j in range(-1,size-1):
            if game[i][j] == 2:
                food = True
    if food == False:
        game[random.randint(-1,size-1)][random.randint(-1,size-1)] = 2
    for i in range(size):
        line = "|"
        row = game[i]
        for y in range(size):
            space = row[y]
            if space == 0:
                line += "  "
            elif space == 1:
                line += "[]"
            elif space == 2:
                line += "{}"
        line += "|"
        print(line)
        
def move(size,game):
    snake = []
    eatfood = False
    move = input("W A S D: ")
    if move == "w":
        for i in range(-1, size-1):
            for j in range(-1, size-1):
                if game[i][j] == 1:
                    snake.append([i,j])
        for i in snake:
            if game[i[0]-1][i[1]] == 2:
                eatfood = True
        if eatfood == False:
            for i in snake:
                game[i[0]][i[1]] = 0
            for i in snake:
                game[i[0]-1][i[1]] = 1
        else:
            for i in snake:
                game[i[0]-1][i[1]] = 1
    if move == "s":
        for i in range(-1, size-1):
            for j in range(-1, size-1):
                if game[i][j] == 1:
                    snake.append([i,j])
        for i in snake:
            if game[i[0]+1][i[1]] == 2:
                eatfood = True
        if eatfood == False:
            for i in snake:
                game[i[0]][i[1]] = 0
            for i in snake:
                game[i[0]+1][i[1]] = 1
        else:
            for i in snake:
                game[i[0]+1][i[1]] = 1
    if move == "a":
        for i in range(-1, size-1):
            for j in range(-1, size-1):
                if game[i][j] == 1:
                    snake.append([i,j])
        for i in snake:
            if game[i[0]][i[1]-1] == 2:
                eatfood = True
        if eatfood == False:
            for i in snake:
                game[i[0]][i[1]] = 0
            for i in snake:
                game[i[0]][i[1]-1] = 1
        else:
            for i in snake:
                game[i[0]][i[1]-1] = 1
    if move == "d":
        for i in range(-1, size-1):
            for j in range(-1, size-1):
                if game[i][j] == 1:
                    snake.append([i,j])
        for i in snake:
            if game[i[0]][i[1]+1] == 2:
                eatfood = True
        if eatfood == False:
            for i in snake:
                game[i[0]][i[1]] = 0
            for i in snake:
                game[i[0]][i[1]+1] = 1
        else:
            for i in snake:
                game[i[0]][i[1]+1] = 1

for i in range(10):
    drawscreen(size,game,food)
    move(size,game)
drawscreen(size,game,food)
print(game)
