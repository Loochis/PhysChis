from PhysChisBounds import RadialBounds
from PhysChisObjects import CelestialObject, Field, PhysObject, StandardObjects
from Vector import Vector3
import Constants as C

gravityField = Field(Vector3(0, -9.8, 0), globalBounds=True)
ballList = []
ball1 = CelestialObject(mass=0.145, vel=Vector3(0,0,0), pos=Vector3(-0.5, 0, 0), objects=ballList, bounds=RadialBounds(radius=0.0365))
ball2 = CelestialObject(mass=0.145, vel=Vector3(0,0,0), pos=Vector3(0.5, 0, 0), objects=ballList, bounds=RadialBounds(radius=0.0365))
ballList.append(ball1)
ballList.append(ball2)

time = 0
while(True):
    print("pos:",ball1.position,"t:",round(time, len(str(C.TIMESTEP))))
    ball1.Tick()
    time += C.TIMESTEP
    if ball1.CollisionCheck(ball2):
        print("Collided!")
        break

print("the basbeballs touch in: " + str(time/60/60/24) + " days")