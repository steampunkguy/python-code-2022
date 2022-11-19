import math

class body:
    def __init__(self, mass, radius, coordinates, name, movementvector):
        self.mass = mass
        self.radius = radius
        self.coordinates = coordinates
        self.name = name
        self.movementvector = movementvector

def calcuatepull(object1, object2):
    plussacceleration = 86400*((6.67*pow(10.0,-11.0)*((object1.mass*object2.mass)/pow(math.sqrt(pow((object1.coordinates[0]-object2.coordinates[0]),2)+ pow((object1.coordinates[1]-object2.coordinates[1]),2)),2)))/object1.mass)
    disanceammount = plussacceleration/math.sqrt(pow((object1.coordinates[0]-object2.coordinates[0]),2)+ pow((object1.coordinates[1]-object2.coordinates[1]),2))
    object1.movementvector[0] = disanceammount*(object1.coordinates[0] - object2.coordinates[0])
    object1.movementvector[1] = disanceammount*(object1.coordinates[1] - object2.coordinates[1])
    object1.coordinates[0] = 
    object1.coordinates[1] = 

def tick(objects):
    for ob1 in objects:
        for ob2 in objects:
            if ob1 != ob2:
                calcuatepull(ob1, ob2)

earth = body(5.972*pow(10.0,24.0),6371000.0,[0.01,0.01],"earth",[0,0])
human = body(7.342*pow(10.0,22.0),1.5,[384400000.0,0.01], "human",[0,0])


objects = [earth,human]

tick(objects)