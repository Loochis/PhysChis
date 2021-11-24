from PhysChis import Kinematics, Newtonian, Reletavistic, Energy, Thermal
from PhysChisBounds import RadialBounds
from PhysChisObjects import CelestialObject, Field, PhysObject, System
from Vector import Vector3
import Constants as C

#### OBJECT CREATION ####

system = System()

print(Thermal.TempFromMix(0.075, 0.7, 45, 0.006, 1.1, 19))