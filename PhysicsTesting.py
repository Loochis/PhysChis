from PhysChis import Newtonian, Reletavistic, Energy
from PhysChisBounds import RadialBounds
from PhysChisObjects import CelestialObject, Field, PhysObject, System
from Vector import Vector3
import Constants as C

#### OBJECT CREATION ####

system = System()
#e1 = Energy.GravPotentialAtDist(C.EARTH_MASS, 5, C.EARTH_RADIUS + 35)
print(Energy.GetEscapeVelocityApprox(4.9e24 ,6050000, 0))