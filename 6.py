import turtle as tr

tr.bgcolor("black")
tr.setup(1000,1000)
tr.speed(speed=0)
tr.color("red")
tr.hideturtle()

gs = tr.Screen()
gs.title("Ilgaz's Graphics")

r = int(input("circle radius"))

y = 0
x = 0
z = 0
points = []
points2 = []
pointleft = []
pointright = []

def dot(x, y):
    tr.setx(x-1)
    tr.sety(y-1)
    tr.pendown()
    tr.setx(x)
    tr.sety(y)
    tr.penup()

dot(0, 0)

while y != r:
    while x != r:
        z = 0
        y2 = y
        for i in range(0, 1):
            x2 = x
            for i in range(0, 1):
                if x**2 + y**2 == r**2:
                    z = z + 1
                x = x + 1
                x = round(x, 0)
            x = x2
            if x**2 + y**2 == r**2:
                z = z + 0
            y = y + 1
            y = round(y, 0)
        y = y2
        if z >= 1:
            points.append([x,y])
            points2.append([[x,y],z])
        x = x + 1
    y = y + 1
    x = 0

dot(r, 0)
dot(0, r)
dot(-r, 0)
dot(0, -r)

for i in points:
    dot(i[0], i[1])
    dot(i[0], -i[1])
    dot(-i[0], i[1])
    dot(-i[0], -i[1])

tr.done()