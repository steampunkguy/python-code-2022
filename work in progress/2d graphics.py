resolutionX = 25
resolutionY = 19

wxoff = 0
wyoff = 0

class spaceObject:
    def __init__(self, xoff, yoff, objectSpaceValues, graverty):
        self.xoff = xoff
        self.yoff = yoff
        self.objectSpaceValues = objectSpaceValues
        self.graverty = graverty

def printSpace(objects, wxoff, wyoff, resolutionX, resolutionY):
    filledSpaces = []
    filledSpace = []
    for i in objects:
        for j in i.objectSpaceValues:
            filledSpace.append(j[0]+wxoff+i.xoff)
            filledSpace.append(j[1]+wyoff+i.yoff)
            filledSpaces.append(filledSpace)
            filledSpace = []
    x = -10
    y = -10
    
    border = "0"
    
    for i in range(-(resolutionX+1)*2, resolutionX*2):
        border = border + "-"
    border = border + "0"

    print(border)
    for i in range( -resolutionY ,resolutionY+1):
        line = "|"
        for j in range(-resolutionX, resolutionX+1):
            if [j, -i] in filledSpaces:
                line = line + "[]"
            else:
                line = line + "  "
        line = line + "|"
        print(line)
    print(border)

def runGraverty(objectsinplay, wyoff):
    for i in objectsinplay:
        n = 0
        if i.graverty == True:
            for j in i.objectSpaceValues:
                if j[1] + i.yoff + wyoff <= n:
                    n = j[1] + i.yoff + wyoff
            if n >= -resolutionY + 1:
                i.yoff = i.yoff - 1
            if n <= -resolutionY - 1:
                i.yoff = i.yoff - (n + resolutionY - 1)

def tick(objectsinplay, wxoff, wyoff, resolutionX, resolutionY):
    printSpace(objectsinplay, wxoff, wyoff, resolutionX, resolutionY)
    runGraverty(objectsinplay, wyoff)



square = spaceObject(-5, 2, [[1,1],[1,0],[1,-1],[0,1],[-1,1],[-1,1],[-1,0],[-1,-1],[0,-1]], False)
dot = spaceObject(2, 2, [[0,0]], True)
man = spaceObject(0, 0, [[1,1],[1,0],[1,-1],[0,1],[-1,1],[-1,1],[-1,0],[-1,-1],[0,-1],[0,-2],[0,-3],[1,-3],[2,-3],[-1,-3],[-2,-3],[0,-4],[0,-5],[1,-6],[-1,-6],[-2,-7],[2,-7]],True)

objectsinplay = [man, square, dot]

for i in range(20):
    tick(objectsinplay, wxoff, wyoff, resolutionX, resolutionY)
    imp = input("W A S D to move:")
    if imp == "s":
        man.yoff = man.yoff - 2
    if imp == "w":
        man.yoff = man.yoff + 2
    if imp == "a":
        man.xoff = man.xoff - 2
    if imp == "d":
        man.xoff = man.xoff + 2
    imp = ""