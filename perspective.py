"""
this is a very old pice of code i made at the start of year 10 this was with around 
2-4 weeks of me lerning codeing how i learn was i learned the basics at shcool then 
i found this website https://www.w3schools.com/python/default.asp read throu all the
diffrent function and then decided to do this so its relay mesy and hard to read and 
iv used all the wrong techniques but with my next project with rotational matrixes i
learn how to make it better i dident even import math for sine tan and cosine i just
coded there defantions in
"""

import turtle as tr

tr.hideturtle()
tr.bgcolor("black")
tr.setup(1000,1000)
tr.speed(speed=0)
tr.color("red")
tr.tracer(0, 0) 
tr.penup()

#shifts entire world
wx = 0
wy = 0
wz = 0
#edits the camera possition
fovz = 87
fovx = 54
fovy = 105

#makes a dot
def dot(x, y):
    tr.setx(x-1)
    tr.sety(y-1)
    tr.pendown()
    tr.setx(x)
    tr.sety(y)
    tr.penup()

#calculates perspective and then displays
def calculatexy(shape ,x ,y ,z):
    for i in shape:
        tr.color(i[1])
        xyz = i[0]

        totalx = xyz[0] + x
        totaly = xyz[1] + y
        totalz = xyz[2] + z

        o = fovz + totalz
        a = totalx + fovx
        try:
            tanO = o / a
            screenX = fovz / tanO
        except:
            screenX = 0

        o = fovz + totalz
        a = totaly + fovy
        try:
            tanO = o / a
            screenY = fovz / tanO
        except:
            screenY = 0

        dot(screenX, screenY)

#this automaticly makes a cube at a point and displayes it
def cubemaker(length, colour, colour2, shapename, x, y, z):
    shapename = []
    n = int(length/2)
    for i in range(-n, n):
        shapename.append([[i, n, -n],colour2])
    for i in range(-n, n):
        shapename.append([[i, -n, -n],colour2])
    for i in range(-n, n):
        shapename.append([[n, i, -n],colour2])
    for i in range(-n, n):
        shapename.append([[-n, i, -n],colour2])
    for i in range(-n, n):
        shapename.append([[n, -n, i],colour])
    for i in range(-n, n):
        shapename.append([[-n, n, i],colour])
    for i in range(-n, n):
        shapename.append([[-n, -n, i],colour])
    for i in range(-n, n):
        shapename.append([[n, n, i],colour])
    for i in range(-n, n):
        shapename.append([[i, n, n],colour])
    for i in range(-n, n):
        shapename.append([[i, -n, n],colour])
    for i in range(-n, n):
        shapename.append([[n, i, n],colour])
    for i in range(-n, n):
        shapename.append([[-n, i, n],colour])
    calculatexy(shapename, x, y, z)

# the code of what you see

cubemaker(100, "red", "blue", "square", 0, 0, 0)

tr.done()