import turtle as tr
import math
import numpy as np

point1 = tr.Turtle()
point2 = tr.Turtle()

point1.hideturtle()
point2.hideturtle()
point2.speed(speed=0)
point1.speed(speed=0)
point1.penup()
point2.penup()

tr.hideturtle()
tr.setup(1000, 1000)
tr.speed(speed=0)
tr.color("red")
tr.tracer(1, 0)
tr.penup()

degrees = math.pi/360

#to rotate it edit values
Xaxis = 0*degrees
Yaxis = 0*degrees
Zaxis = 0*degrees
fovz = 3000
fovx = 0
fovy = 0

"""
rotation matrixes

Xaxisrotation = np.array([[1, 0, 0], [0, math.cos(Xaxis), -math.sin(Xaxis)], [0, math.sin(Xaxis), math.cos(Xaxis)]])
Yaxisrotation = np.array([[math.cos(Yaxis), 0, math.sin(Yaxis)], [0, 1, 0], [-math.sin(Yaxis), 0, math.cos(Yaxis)]])
Zaxisrotation = np.array([[math.cos(Zaxis), -math.sin(Zaxis), 0], [math.sin(Zaxis), math.cos(Zaxis), 0], [0, 0, 1]])

"""
cubepoints = []

#all the lines for the cube edit to make diffrent shapes or just make a new shape
cube = np.array([[0, 0, 0], [100, 0, 0], [100, 0, 100], [100, 0, 0],
                 [100, 100, 0], [100, 100, 100], [100, 100, 0], [0, 100, 0],
                 [0, 100, 100], [0, 100, 0], [0, 0, 0], [0, 0, 100],
                 [0, 100, 100], [100, 100, 100], [100, 0, 100], [0, 0, 100]])

#draws lines from point to point
def connect(points):
    point1.goto(points[0][0], points[0][1])
    for i in points:
        point1.pendown()
        point2.pendown()
        point1.goto(i[0], i[1])
        point2.clear()
        point1.penup()
        point2.penup()

#makes the red dots
def dot(x, y):
    tr.goto(x, y)
    tr.dot(5)
    cubepoints.append([x, y])


#the function calculate the rotation
def calculatexy(shape, addx, addy, addz, X, Y, Z):
    for i in shape:
        Xaxisrotation = np.array([[1, 0, 0], [0, math.cos(X), -math.sin(X)], [0, math.sin(X), math.cos(X)]])
        Yaxisrotation = np.array([[math.cos(Y), 0, math.sin(Y)], [0, 1, 0], [-math.sin(Y), 0, math.cos(Y)]])
        Zaxisrotation = np.array([[math.cos(Z), -math.sin(Z), 0], [math.sin(Z), math.cos(Z), 0], [0, 0, 1]])

        i = np.matmul(Xaxisrotation, i)
        i = np.matmul(Yaxisrotation, i)
        i = np.matmul(Zaxisrotation, i)

        totalx = i[0] + addx
        totaly = i[1] + addy
        totalz = i[2] + addz

        #"""
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
        #"""
        #dot(totalx, totaly)

"""
this is all the functions put together
"""

rows = 1
collums = 10

for i in range(rows):
  for j in range (collums):
    calculatexy(cube, j*200-collums*100, 0, i*200, Xaxis, Yaxis, Zaxis)
    #calculatexy(cube,-50,0,-50, Xaxis, Yaxis, Zaxis)
    connect(cubepoints)
    cubepoints = []
    Xaxis += 20*degrees
    Yaxis += 20*degrees
    Zaxis += 20*degrees

tr.done()