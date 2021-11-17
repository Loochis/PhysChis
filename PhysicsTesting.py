from PhysChis import Newtonian, Reletavistic, Energy
from PhysChisBounds import RadialBounds
from PhysChisObjects import CelestialObject, Field, PhysObject, System
from Vector import Vector3
import Constants as C

#### OBJECT CREATION ####

system = System()
e1 = Energy.GravPotentialAtDist(C.SUN_MASS, 1, 4.9e10) + Energy.GetKineticEnergyApprox(9.5e4, 1)
eVf = e1 - Energy.GravPotentialAtDist(C.SUN_MASS, 1, 6e12)
print(eVf)

print(Energy.GetSpeedFromEnergyApprox(4544633823, 1))
print(Energy.GetSpeedFromEnergy(4544633823, 1))