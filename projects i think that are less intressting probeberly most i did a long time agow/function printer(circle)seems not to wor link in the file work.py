#httpsonlinegdb.comc9a7tgxRad
r = 1

x = -r
y = -r
circle = ""

while y != r:
    while x != r:
        z = 0
        y2 = y
        for i in range(0, 100):
            x2 = x
            for i in range(0, 100):

                if x**2 + y**2 < 0.001 + r**2 and x**2 + y**2 > r**2 - 0.001 :
                    z = z + 1

                x = x + 0.001
                x = round(x, 3)
            x = x2
            if x**2 + y**2 < 0.001 + r**2 and x**2 + y**2 > r**2 - 0.001:
                z = z + 1

            y = y + 0.001
            y = round(y, 3)
        
        y = y2
        if z >= 1:
            circle = circle + "[]"
        else:
            circle = circle + "  "

        x = x + 0.1
        x = round(x, 1)
    else:
        y = y + 0.1
        y = round(y, 1)
        print(circle)
        circle = ""