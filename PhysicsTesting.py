from Vector import Vector3
import PhysChis

rStar = Vector3(7e12, 2e12, 0)
rPlanet = Vector3(3e12, 6e12, 0)
mStar = 9e30
mPlanet = 7e24

vPlanetInitial = Vector3(0.6e4, 1.7e4, 0)
rPlanetInitial = rPlanet
vPlanet = vPlanetInitial

timeStep = 1e6

force = PhysChis.GravitationalFields.ForceOnM2(rStar, rPlanet, mStar, mPlanet)
vPlanet = PhysChis.Newtonian.TimeStepVelocity(v=vPlanet, f=force, m=mPlanet, timeStep=timeStep)
rPlanet = PhysChis.Newtonian.TimeStepPosition(rPlanet, vPlanet, timeStep)

print(rPlanet)