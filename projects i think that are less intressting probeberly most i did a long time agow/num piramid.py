n = int(input("Inpunt number of primidlayer: "))
primidlayer = ""
n = n + 2
ls = [[0,1,0]]

for i in range(0, n):
    lc = [0]
    ll = ls[i]
    for y in range(0, i+1):
        np = ll[0+y] + ll[1+y]
        lc.append(np)
    lc.append(0)
    ls.append(lc)

layernum = len(ls)
layer = ls[layernum-1]
mid = len(layer)
spacenum = len(str(layer[round(mid/2)]))
spaces = ""
for i in range(spacenum):
    spaces += " "

print(spacenum)

lastnum = 0
for i in range(0, n):
    numbers = ls[i-1]
    y = i * 2 - 1
    for i in range(0, n - i):
        for i in range(len(spaces)-1):
            primidlayer += " "
    for i in range(0, y):
        if i % 2 == 1:
            primidlayer += str(numbers[int((i+1)/2)])
            lastnum = str(numbers[int((i+1)/2)])
        else:
            for i in range(len(spaces)-len(str(lastnum))+1):
                primidlayer += " "
    print(primidlayer)
    primidlayer = ""