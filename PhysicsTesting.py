from PhysChis import Kinematics, Newtonian, PhotonsNEnergy, Reletavistic, Energy, Thermal
from PhysChisBounds import RadialBounds
from PhysChisObjects import CelestialObject, Field, PhysObject, System
from Vector import Vector3
import Constants as C

#### OBJECT CREATION ####

system = System()

mEarth = 6e24
mAsteroid = 2100
vf = 8800
rf = 2e7
ri = 4e7

print(PhotonsNEnergy.GetHydrogenAtomEnergyAtLevel(5))