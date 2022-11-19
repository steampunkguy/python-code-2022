import random
import math
from tkinter import PIESLICE
from turtle import right

p1 = 0
p2 = 0

print("started")

def botrandom(nimbord):
    space = random.randint(-1 ,len(nimbord)-1)
    nimbord[space] = nimbord[space] - random.randint(1,nimbord[space])
    for i in nimbord:
        if i == 0:
            nimbord.remove(0)
    
def botlogs(nimbord):
    num = 0
    place = 0
    for i in range(len(nimbord)):
        if nimbord[i] > num:
            place = i
            num = nimbord[i]
    if num > 1:
        minus = math.log(num, 2)
    else:
        minus = 1
    delnum = round(minus)
    if delnum < 1:
        delnum = 1
    nimbord[place] -= delnum
    for i in nimbord:
        if i == 0:
            nimbord.remove(0)

def botsmatach(nimbord):
    plays = 0
    binarylist = []
    bins = []
    wbin = []
    for i in nimbord:
        binarylist.append(str(bin(i))[2:])
    for i in range(len(binarylist)):
        if len(binarylist[i]) >= 1:
            if int(binarylist[i][len(binarylist[i])-1]) == 1:
                wbin.append(i)
    bins.append(wbin)
    wbin = []
    for i in range(len(binarylist)):
        if len(binarylist[i]) >= 2:
            if int(binarylist[i][len(binarylist[i])-2]) == 1:
                wbin.append(i)
    bins.append(wbin)
    wbin = []
    for i in range(len(binarylist)):
        if len(binarylist[i]) >= 3:
            if int(binarylist[i][len(binarylist[i])-3]) == 1:
                wbin.append(i)
    bins.append(wbin)
    wbin = []
    for i in range(len(binarylist)):
        if len(binarylist[i]) >= 4:
            if int(binarylist[i][len(binarylist[i])-4]) == 1:
                wbin.append(i)
    bins.append(wbin)

    pairs = 0
    for i in bins:
        pairs += len(i)%2

    minus = 0
    if pairs == 1:
        for i in range(4):
            if len(bins[i])%2 == 1:
                for j in range(5):
                    if j in (bins[i]):
                        if i == 0:
                            minus = [j,1]
                        else:
                            minus = [j,i^2]
                        play = 1
    elif pairs == 2:
        for i in range(3):
            if len(bins[i])%2 == 1:
                for j in range(4):
                    if len(bins[j])%2 == 1:
                        for k in range(5):
                            if k in (bins[i] and bins[j]):
                                if i == 0:
                                    minus = [k,
                                    1+j^2]
                                elif j == 0:
                                    minus = [k,i^2+1]
                                else:
                                    minus = [k,i^2+j^2]
                                play = 1
                                print(minus)
    elif pairs == 3:
        for i in range(3):
            if len(bins[i])%2 == 1:
                for j in range(4):
                    if len(bins[j])%2 == 1:
                        for k in range(4):
                            if len(bins[k])%2 == 1:
                                for l in range(5):
                                    if l in (bins[i] and bins[j] and bins[k]):
                                        if i == 0:
                                            minus = [l,1+j^2+k^2]
                                        elif j == 0:
                                            minus = [l,i^2+1+k^2]
                                        elif k == 0:
                                            minus = [l,i^2+j^2+1]
                                        else:
                                            minus = [l,i^2+j^2+k^2]
                                        play = 1
    

    print(minus,pairs)

    for i in nimbord:
        if i == 0:
            nimbord.remove(0)

def play():
    #nimbord = [random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9)]
    nimbord = [2,2,1,1,5]
    while len(nimbord) != 1:
        botsmatach(nimbord)
        if len(nimbord) == 1:
            return(0)
        #botrandom(nimbord)
        if len(nimbord) == 1:
            return(1)

for i in range(100):
    player = play()
    if player == 1:
        p2 += 1
    else:
        p1 += 1
print(p1,p2)