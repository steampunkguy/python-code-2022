import math
import random
import operator

def botplay(game):
    n = 1
    while n == 1:
        play = random.randint(-1,8)
        if game[play] == 0:
            game[play] = 1
            n = 2

#ony coment i know theres other activation functions but this seemed to be a good one
def sigmoid(inputs, output):
    for i in inputs:
        x = 1.0/(1.0 + pow(math.e, -float(i)))     
        output.append(x)

class neuronLayers:
    def __init__(self, wights, inputs, bias, numberOfNeurons):
        self.inputs = inputs
        self.wights = wights
        self.bias = bias
        self.numberOfNeurons = numberOfNeurons

    def nuronLayer(self, output):
        for neuron in range(0, self.numberOfNeurons):
            biasN = self.bias[neuron]
            wightsN = self.wights[neuron]
            out = 0
            for conection in range(0, len(self.inputs)):
                out = wightsN[conection] * self.inputs[conection] + float(out)
            out += biasN
            output.append(out)

def nbotplay(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game):
    output = []
    outputs1 = []
    outputs2 = []
    outputs3 = []
    outputs4 = []
    inputs2 = []
    inputs3 = []
    inputs4 = []

    layer1 = neuronLayers(wights1, game, bias1, 4)
    layer1.nuronLayer(outputs1)
    sigmoid(outputs1, inputs2)
    layer2 = neuronLayers(wights2, inputs2, bias2, 3)
    layer2.nuronLayer(outputs2)
    sigmoid(outputs2, inputs3)
    layer3 = neuronLayers(wights3, inputs3, bias3, 3)
    layer3.nuronLayer(outputs3)
    sigmoid(outputs3, inputs4)
    layer3 = neuronLayers(wights4, inputs4, bias4, 9)
    layer3.nuronLayer(outputs4)
    sigmoid(outputs4, output)

    x = 0
    n = 0
    m = 0

    dictonary = {}
    for i in output:
        dictonary.update({x:i})
        x += 1
    
    answer = sorted(dictonary.items() , key=operator.itemgetter(1))

    while n == 0:
        if game[answer[m][0]] == 0:
            game[answer[m][0]] = 2
            n += 1
        else:
            m += 1

def printmach(game):
    x = 0
    for i in game:
        if i == 0:
            print(" |", end="")
        if i == 1:
            print("x|", end="")
        if i == 2:
            print("o|", end="")
        x += 1
        if x == 3:
            print(" ")
            x = 0
    print(" ")

def win(game):
    wins = [[1,1,1,0,0,0,0,0,0],
            [0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,1,1,1],
            [1,0,0,1,0,0,1,0,0],
            [0,1,0,0,1,0,0,1,0],
            [0,0,1,0,0,1,0,0,1],
            [1,0,0,0,1,0,0,0,1],
            [0,0,1,0,1,0,1,0,0]]
    
    team1 = []
    team2 = []

    for i in game:
        if i == 1:
            team1.append(1)
        else:
            team1.append(0)
    
    for i in game:
        if i == 2:
            team2.append(1)
        else:
            team2.append(0)

    for i in wins:
        score = 0
        for j in range(-1, 8):
            if i[j] == 1:
                if i[j] == team1[j]:
                    score += 1
        if score == 3:
            print("bot wins")
            quit()
        score = 0
        for j in range(-1, 8):
            if i[j] == 1:
                if i[j] == team2[j]:
                    score += 1
        if score == 3:
            print("ai wins")
            quit()

def fastwin(game, out):
    wins = [[1,1,1,0,0,0,0,0,0],
            [0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,1,1,1],
            [1,0,0,1,0,0,1,0,0],
            [0,1,0,0,1,0,0,1,0],
            [0,0,1,0,0,1,0,0,1],
            [1,0,0,0,1,0,0,0,1],
            [0,0,1,0,1,0,1,0,0]]
    
    team1 = []
    team2 = []

    for i in game:
        if i == 1:
            team1.append(1)
        else:
            team1.append(0)
    
    for i in game:
        if i == 2:
            team2.append(1)
        else:
            team2.append(0)

    for i in wins:
        score = 0
        for j in range(-1, 8):
            if i[j] == 1:
                if i[j] == team1[j]:
                    score += 1
        if score == 3:
            out = 1
        score = 0
        for j in range(-1, 8):
            if i[j] == 1:
                if i[j] == team2[j]:
                    score += 1
        if score == 3:
            out = 2
    print(out, game)

def quickturn1(game, outcome, timesplayed):
    try:
        if outcome[timesplayed] == 1 or 2:
            return
    except:
        pass
    botplay(game)
    wins = [[1,1,1,0,0,0,0,0,0],
            [0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,1,1,1],
            [1,0,0,1,0,0,1,0,0],
            [0,1,0,0,1,0,0,1,0],
            [0,0,1,0,0,1,0,0,1],
            [1,0,0,0,1,0,0,0,1],
            [0,0,1,0,1,0,1,0,0]]
    
    team1 = []
    team2 = []

    for i in game:
        if i == 1:
            team1.append(1)
        else:
            team1.append(0)
    
    for i in game:
        if i == 2:
            team2.append(1)
        else:
            team2.append(0)

    for i in wins:
        score = 0
        for j in range(-1, 8):
            if i[j] == 1:
                if i[j] == team1[j]:
                    score += 1
        if score == 3:     
            outcome.append(1)
        score = 0
        for j in range(-1, 8):
            if i[j] == 1:
                if i[j] == team2[j]:
                    score += 1
        if score == 3:
            outcome.append(2)
    if outcome == 2:
        exit()
    elif outcome == 1:
        exit()

def quickturn2(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game, winer, timesplayed):
    nbotplay(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game)
    wins = [[1,1,1,0,0,0,0,0,0],
            [0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,1,1,1],
            [1,0,0,1,0,0,1,0,0],
            [0,1,0,0,1,0,0,1,0],
            [0,0,1,0,0,1,0,0,1],
            [1,0,0,0,1,0,0,0,1],
            [0,0,1,0,1,0,1,0,0]]
    
    team1 = []
    team2 = []

    for i in game:
        if i == 1:
            team1.append(1)
        else:
            team1.append(0)
    
    for i in game:
        if i == 2:
            team2.append(1)
        else:
            team2.append(0)

    for i in wins:
        score = 0
        for j in range(-1, 8):
            if i[j] == 1:
                if i[j] == team1[j]:
                    score += 1
        if score == 3:
            outcome.append(1)
        score = 0
        for j in range(-1, 8):
            if i[j] == 1:
                if i[j] == team2[j]:
                    score += 1
        if score == 3:
            outcome.append(2)
    if outcome == 2:
        exit()
    elif outcome == 1:
        exit()


def quickplay(outcome, answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game, timesplayed):
    quickturn1(game, outcome, timesplayed)
    quickturn2(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game, outcome, timesplayed)
    quickturn1(game, outcome, timesplayed)
    quickturn2(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game, outcome, timesplayed)
    quickturn1(game, outcome, timesplayed)
    quickturn2(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game, outcome, timesplayed)
    quickturn1(game, outcome, timesplayed)
    quickturn2(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game, outcome, timesplayed)
    quickturn1(game, outcome, timesplayed)
    if timesplayed > len(outcome)-1:
        outcome.append(0)

def slowplay(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game):
    botplay(game)
    printmach(game)
    win(game)
    nbotplay(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game)
    printmach(game)
    win(game)
    botplay(game)
    printmach(game)
    win(game)
    nbotplay(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game)
    printmach(game)
    win(game)
    botplay(game)
    printmach(game)
    win(game)
    nbotplay(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game)
    printmach(game)
    win(game)
    botplay(game)
    printmach(game)
    win(game)
    nbotplay(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game)
    printmach(game)
    win(game)
    botplay(game)
    printmach(game)
    win(game)

def randomlearning(wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, Nwights1, Nbias1, Nwights2, Nbias2, Nwights3, Nbias3, Nwights4, Nbias4):
    for i in range(len((wights1))):
        for j in range(len(wights1[i])):
            Nwights1[i][j] = round(wights1[i][j] + random.randrange(-100, 100, 1)/100, 2)

    for i in range(len((wights2))):
        for j in range(len(wights2[i])):
            Nwights2[i][j] = round(wights2[i][j] + random.randrange(-100, 100, 1)/100, 2)
    
    for i in range(len((wights3))):
        for j in range(len(wights3[i])):
            Nwights3[i][j] = round(wights3[i][j] + random.randrange(-100, 100, 1)/100, 2)

    for i in range(len((wights4))):
        for j in range(len(wights4[i])):
            Nwights4[i][j] = round(wights4[i][j] + random.randrange(-100, 100, 1)/100, 2)
    
    for i in range(len((bias1))):
        Nbias1[i] = round(bias1[i] + random.randrange(-100, 100, 1)/100, 2)

    for i in range(len((bias2))):
        Nbias2[i] = round(bias2[i] + random.randrange(-100, 100, 1)/100, 2)

    for i in range(len((bias3))):
        Nbias3[i] = round(bias3[i] + random.randrange(-100, 100, 1)/100, 2)

    for i in range(len((bias4))):
        Nbias4[i] = round(bias4[i] + random.randrange(-100, 100, 1)/100, 2)

def trainrandom1timep(outcome, answer, game, timesplayed, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, Nwights1, Nbias1, Nwights2, Nbias2, Nwights3, Nbias3, Nwights4, Nbias4, betterworse):
    
    timesplayed = 0
    outcome = []
    game = [0,0,0,0,0,0,0,0,0]
    answer = 0

    for i in range(1,10001):
        quickplay(outcome, answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game, timesplayed)
        game = [0,0,0,0,0,0,0,0,0]
        answer = 0
        timesplayed = i

    wins1 = 0
    wins2 = 0

    for i in outcome:
        if i == 1:
            wins1 += 1
        elif i == 2:
            wins2 += 1
        elif i == 0:
            wins2 += 0.5

    print(wins1, wins2)

    randomlearning(wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, Nwights1, Nbias1, Nwights2, Nbias2, Nwights3, Nbias3, Nwights4, Nbias4)

    timesplayed = 0
    outcome = []
    game = [0,0,0,0,0,0,0,0,0]
    answer = 0

    for i in range(1,10001):
        quickplay(outcome, answer, Nwights1, Nbias1, Nwights2, Nbias2, Nwights3, Nbias3, Nwights4, Nbias4, game, timesplayed)
        game = [0,0,0,0,0,0,0,0,0]
        answer = 0
        timesplayed = i

    wins3 = 0
    wins4 = 0

    for i in outcome:
        if i == 1:
            wins3 += 1
        elif i == 2:
            wins4 += 1
        elif i == 0:
            wins4 += 0.5

    print(wins3, wins4)

    if wins2 > wins4:
        print("worse")
        betterworse[0] = 2
    else:
        print("better")
        betterworse[0] = 1

betterworse = [0]

timesplayed = 0

outcome = []
game = [0,0,0,0,0,0,0,0,0]
answer = 0

Nbias1 = [0,1,1,1]
Nwights1 = [[1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1]]

Nbias2 = [1,1,1]
Nwights2 = [[1,1,1,1],
           [1,1,1,1],
           [1,1,1,1]]

Nbias3 = [1,1,1]
Nwights3 = [[1,1,1],
           [1,1,1],
           [1,1,1]]

Nbias4 = [1,1,1,1,1,1,1,1,1]
Nwights4 = [[1,1,1],
           [1,1,1],
           [1,1,1],
           [1,1,1],
           [1,1,1],
           [1,1,1],
           [1,1,1],
           [1,1,1],
           [1,1,1]]

bias1 = [0,1,1,1]
wights1 = [[1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1]]

bias2 = [1,1,1]
wights2 = [[1,1,1,1],
           [1,1,1,1],
           [1,1,1,1]]

bias3 = [1,1,1]
wights3 = [[1,1,1],
           [1,1,1],
           [1,1,1]]

bias4 = [1,1,1,1,1,1,1,1,1]
wights4 = [[1,1,1],
           [1,1,1],
           [1,1,1],
           [1,1,1],
           [1,1,1],
           [1,1,1],
           [1,1,1],
           [1,1,1],
           [1,1,1]]

for i in range(10): 
    print(wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4)
    trainrandom1timep(outcome, answer, game, timesplayed, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, Nwights1, Nbias1, Nwights2, Nbias2, Nwights3, Nbias3, Nwights4, Nbias4, betterworse)
    print(betterworse)
    print(betterworse)
    if betterworse[0] == 1:
        wights1 = Nwights1
        bias1 = Nbias1
        wights2 = Nwights2
        bias2 = Nbias2
        wights3 = Nwights3
        bias3 = Nbias3
        wights4 = Nwights4
        bias4 = Nbias4

slowplay(answer, wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, game)

#wights1, bias1, wights2, bias2, wights3, bias3, wights4, bias4, Nwights1, Nbias1, Nwights2, Nbias2, Nwights3, Nbias3, Nwights4, Nbias4
