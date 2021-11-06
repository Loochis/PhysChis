from PhysChis import Newtonian, Reletavistic, Energy
from PhysChisBounds import RadialBounds
from PhysChisObjects import CelestialObject, Field, PhysObject, System
from Vector import Vector3
import Constants as C

#### OBJECT CREATION ####

system = System()

nucleus = PhysObject(mass=3.902996e-25, vel=Vector3(0,0,0))
he4 = PhysObject(mass=6.640678e-27, vel=Vector3(0,0,0))
nucleus2 = PhysObject(mass=3.836448e-25, vel=Vector3(0,0,0))

#### SIMULATION ####
print(nucleus.GetRestEnergy())
print(he4.GetRestEnergy() + nucleus2.GetRestEnergy())
print((nucleus.GetRestEnergy() - (he4.GetRestEnergy() + nucleus2.GetRestEnergy()))/C.EV)