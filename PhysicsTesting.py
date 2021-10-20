from PhysChis import Newtonian
from PhysChisBounds import RadialBounds
from PhysChisObjects import CelestialObject, Field, PhysObject, System
from Vector import Vector3
import Constants as C

#### OBJECT CREATION ####

system = System()

gravityField = Field(acceleration=Vector3(0,0,0),globalBounds=True)

ball1 = PhysObject(mass=12, vel=Vector3(4400,-3100,2600), pos=Vector3(0, 0, 0), bounds=RadialBounds(radius=0))
ball2 = PhysObject(mass=6, vel=Vector3(-750,1800,3500), pos=Vector3(0, 0, 0), bounds=RadialBounds(radius=0))

system.objects.append(ball1)
system.objects.append(ball2)
system.objects.append(gravityField)

#### SIMULATION ####

time = 0

p1i = ball1.GetMomentum()
p2i = ball2.GetMomentum()
ball1.velocity = Vector3(1300, 600, 1900)
ball1.mass -= 2
ball2.mass += 2

ball2.SetMomentum (Newtonian.MomentumTransfer(p1i, p2i, ball1.GetMomentum()))
print(ball2.velocity)