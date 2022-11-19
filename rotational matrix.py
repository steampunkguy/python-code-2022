"""
made 2 weeks afer perspective
"""
import turtle as tr
import math
import numpy as np

point1 = tr.Turtle()
point2 = tr.Turtle()

point1.hideturtle()
point2.hideturtle()
point2.speed(speed=0)
point1.speed(speed=0)

tr.hideturtle()
tr.setup(1000,1000)
tr.speed(speed=0)
tr.color("red")
tr.tracer(1, 0) 
tr.penup()

#to rotate it edit values
Xaxis = 75
Yaxis = 96
Zaxis = 16

#rotation matrixes
Xaxisrotation = np.array([[1, 0, 0], [0, math.cos(Xaxis), -math.sin(Xaxis)], [0, math.sin(Xaxis), math.cos(Xaxis)]])
Yaxisrotation = np.array([[math.cos(Yaxis), 0, math.sin(Yaxis)], [0, 1, 0], [-math.sin(Yaxis), 0, math.cos(Yaxis)]])
Zaxisrotation = np.array([[math.cos(Zaxis), -math.sin(Zaxis), 0], [math.sin(Zaxis), math.cos(Zaxis), 0], [0, 0, 1]])

cubepoints = []

#all the lines for the cube edit to make diffrent shapes or just make a new shape
cube = np.array([[0,0,0], [100,0,0], [100,0,100], [100,0,0], [100,100,0], [100,100,100], [100,100,0], [0,100,0], [0,100,100], [0,100,0], [0,0,0], [0,0,100], [0,100,100], [100,100,100], [100,0,100], [0,0,100]])

#draws lines from point to point
def connect(points):
    for i in points:
        point1.pendown()
        point2.pendown()
        point1.goto(i[0], i[1])
        point2.clear()

#makes the red dots
def dot(x, y):
    tr.goto(x,y)    
    tr.dot(20)
    cubepoints.append([x,y])

#the function calculate the rotation
def calculatexy(shape ,addx ,addy ,addz):
    for i in shape:

        i = np.matmul(Xaxisrotation, i)
        i = np.matmul(Yaxisrotation, i)
        i = np.matmul(Zaxisrotation, i)

        totalx = i[0] + addx
        totaly = i[1] + addy
        totalz = i[2] + addz
        
        dot(totalx, totaly)

"""
this is all the functions put together
"""

calculatexy(cube, 0, 0, 0)

connect(cubepoints)
tr.done()