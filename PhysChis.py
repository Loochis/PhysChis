from Vector import Vector3
import Constants as C

class ElectricFields:
    # Calculates the electric force acting on Particle 1
    def ForceOnP1(r1, r2, q1, q2):
        r = Vector3.VecFromTo(r1, r2)
        force = r.Normalized() * (-q1*q2*C.ONE_OVER_4PIE0)
        force /= r.Length2()
        return force

    # Calculates the eletric force acting on Particle 2
    def ForceOnP2(r1, r2, q1, q2):
        r = Vector3.VecFromTo(r2, r1)
        force = r.Normalized() * (-q1*q2*C.ONE_OVER_4PIE0)
        force /= r.Length2()
        return force

class GravitationalFields:
    def ForceonMScalar(rMag, m1, m2):
        force = m1*m2*C.G
        force /= rMag**2
        return force

    # Calculates the gravitational force acting on Mass 1
    def ForceOnM1(r1, r2, m1, m2):
        r = Vector3.VecFromTo(r1, r2)
        force = r.Normalized() * (m1*m2*C.G)
        force /= r.Length2()
        return force

    # Calculates the gravitational force acting on Mass 2
    def ForceOnM2(r1, r2, m1, m2):
        r = Vector3.VecFromTo(r2, r1)
        force = r.Normalized() * (m1*m2*C.G)
        force /= r.Length2()
        return force

    # Calculates the acceleration (force on m=1) by another mass due to gravity
    def AccelerationByMass(rPoint, rMass, mass):
        r = Vector3.VecFromTo(rPoint, rMass)
        acceleration = r.Normalized() * (mass*C.G)
        acceleration /= r.Length2()
        return acceleration


class Newtonian():
    def TimeStepVelocity(v: Vector3, f: Vector3, m: float, timeStep: float):
        a = f / m
        return v + (a * timeStep)

    def TimeStepPosition(r, v, timeStep):
        return r + (v * timeStep)
