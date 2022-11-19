"""
sub = 1
cru = 2
bat = 3
air = 4
"""

gamestate = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]]

def placeships(ships,shipname,shipleanth):
    error = 0
    currentships = 0
    
    while currentships < ships:
        
        direction = input("horazontal/vertical(1/2): ")
        
        if direction == "1":
            row = int(input("ship row ship will point right 1-9: "))
            colum = int(input("ship colum ship will point right 1-9: "))
            if colum > 9:
                error = 1
            elif colum < 1:
                error = 1
            elif row > 9:
                error = 1
            elif row < 1:
                error = 1
            if error == 0:
                for i in range(shipleanth):
                    if gamestate[row-1][colum-1+i] != 0:
                        error = 2
                if error == 0:
                    for i in range(shipleanth):
                       gamestate[row-1][colum-1+i] = shipname
                    currentships += 1
    
        if direction == "2":
            row = int(input("ship row ship will point down 1-9: "))
            colum = int(input("ship colum ship will point down 1-9: "))
            if colum > 9:
                error = 1
            elif colum < 1:
                error = 1
            elif row > 9:
                error = 1
            elif row < 1:
                error = 1
            if error == 0:
                for i in range(shipleanth):
                    if gamestate[row-1+i][colum-1] != 0:
                        error = 2
                if error == 0:
                    for i in range(shipleanth):
                       gamestate[row-1+i][colum-1] = shipname
                    currentships += 1
    
        if error == 1:
            print("[]==============================================================================[]")
            print("  there was an error with the number you inputed for the position with your ship")
            print("[]==============================================================================[]")
            error = 0
        elif error == 2:
            print("[]===========================================================[]")
            print("  there was an error with this ship coliding with another one")
            print("[]===========================================================[]")
            error = 0

#placeships(4,1,2)
#placeships(3,2,3)
placeships(2,3,4)
#placeships(1,4,5)

print("    1   2   3   4   5   6   7   8   9   10 ")
print("  o---o---o---o---o---o---o---o---o---o---o")
for i in range(10):
    if i < 9:
        line = str(i+1) + " |"
    else:
        line = str(i+1) + "|"
    for j in gamestate[i]:
        if j == 0:
            line += "   |"
        elif j == 1:
            line += " S |" 
        elif j == 2:
            line += " C |"
        elif j == 3:
            line += " B |"
        elif j == 1:
            line += " A |"
    print(line)
    print("  o---o---o---o---o---o---o---o---o---o---o")




