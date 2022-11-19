string = "011101000110100001101001011100110010000001101001011100110010000001100001001000000110001001101001011011100110000101110010011110010010000001110100011001010111100001110100"
key = 11101001

def Xor(in1, in2, out):
    if in1 != in2:
        out = 1
    else:
        out = 0

def mixrows(cubes,bitchunks):
    for i in bitchunks:
        cube = []
        cube.append(i[0])
        cube.append(i[4])
        cube.append(i[8])
        cube.append(i[12])
        cube.append(i[13])
        cube.append(i[1])
        cube.append(i[5])
        cube.append(i[9])
        cube.append(i[10])
        cube.append(i[14])
        cube.append(i[2])
        cube.append(i[6])
        cube.append(i[15])
        cube.append(i[13])
        cube.append(i[7])
        cube.append(i[3])

        cubes.append(cube)

def addkey(key, sting):
    m = 8
    x = 0
    newstring = [] 
    
    key = str(key)
    
    keyparts = [key[i:i+m] for i in range(0, len(key), m)]
    
    for i in string:
        for j in i:
            if len(keyparts)-1 > x:
                x += 1
            else:
                x = 0
            keybite = keyparts[x]
            for k in range(8):
                newbin = 0
                print(k)
                Xor(keybite[k], j[k], newbin)
                newstring.append(newbin)
            x += 1

def breakeingintochunks(string, smallchunkssections):
    m = 8
    n = 128
    
    chunks = [string[i:i+n] for i in range(0, len(string), n)]
    fullchuncks = []
    
    for i in chunks:
        while len(i) < 128:
            i = i + "0"
        fullchuncks.append(i)
    
    for j in fullchuncks:
        chunksf = [j[i:i+m] for i in range(0, len(j), m)]
        smallchunkssections.append(chunksf)

chunks = []

breakeingintochunks(string, chunks)
addkey(key, chunks)

"""
mixedrows = []
breakeingintochunks(string, chunks)
mixrows(mixedrows,chunks)
print(mixedrows)
"""