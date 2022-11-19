n = int(input("Input Number of layers:"))

primidlayer = ""

for i in range(0, n):
    for y in range(0, n-i):
        primidlayer = primidlayer + " "
    for i in range(0, i*2):
        if i % 2 != 1:
            primidlayer = primidlayer + "*"
        else:
            primidlayer = primidlayer + " "
    print(primidlayer)
    primidlayer = ""