from PhysChisBounds import RadialBounds
from PhysChisObjects import CelestialObject, Field, PhysObject, System
from Vector import Vector3
import Constants as C

#### OBJECT CREATION ####

ballSystem = System()

gravityField = Field(acceleration=Vector3(0,-9.8,0),globalBounds=True)

ball1 = PhysObject(mass=0.9, vel=Vector3(4,-5,3), pos=Vector3(0, 0, 0), bounds=RadialBounds(radius=0))
ball2 = PhysObject(mass=0.9, vel=Vector3(7,9,9), pos=Vector3(-1.5e11, 0, 0), bounds=RadialBounds(radius=0))
ballSystem.objects.append(ball1)
ballSystem.objects.append(ball2)
ballSystem.objects.append(gravityField)

#### SIMULATION ####

time = 0

ballSystem.Tick()
print(ballSystem.GetMomentum())