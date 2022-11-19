import turtle as tr

x = 0

def circle():
    tr.hideturtle()
    tr.bgcolor("black")
    tr.setup(1000,1000)
    tr.speed(speed=0)
    tr.color("red")
    tr.tracer(0, 0)

    gs = tr.Screen()
    gs.title("Ilgaz's Graphics: ")

    r = int(input("circle radius: "))

    y = -r-10
    x = -r-10
    z = 0
    points = []
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

    while y != r+10:
        while x != r+10:
            if (x**2 + y**2)-200 <= r**2 and (x**2 + y**2)+200 >= r**2:
                dot(x, y)
            x = x + 1
        if (x**2 + y**2)-200 <= r**2 and (x**2 + y**2)+200 >= r**2:
            dot(x, y)
        y = y + 1
        x = -r

    dot(r, 0)
    dot(0, r)
    dot(-r, 0)
    dot(0, -r)

    tr.update()

while x != 1:
    circle()
    int = input("Want another circle?(y/n): ")
    if int == "y":
        x = 0
    else:
        x = 1