from Vector import Vector3

ONE_OVER_4PIE0 = 9e9
G = 6.674e-11
class ElectricFields:

    # Calculates the electric force acting on Particle 1
    def ForceOnP1(r1, r2, q1, q2):
        r = Vector3.VecFromTo(r1, r2)
        force = Vector3.Multiply(r.Normalized(), -q1*q2*ONE_OVER_4PIE0)
        force = Vector3.Divide(force, r.Length2())
        return force

    # Calculates the eletric force acting on Particle 2
    def ForceOnP2(r1, r2, q1, q2):
        r = Vector3.VecFromTo(r2, r1)
        force = Vector3.Multiply(r.Normalized(), -q1*q2*ONE_OVER_4PIE0)
        force = Vector3.Divide(force, r.Length2())
        return force

class GravitationalFields:
    def ForceonMScalar(rMag, m1, m2):
        force = m1*m2*G
        force /= rMag**2
        return force

    # Calculates the gravitational force acting on Mass 1
    def ForceOnM1(r1, r2, m1, m2):
        r = Vector3.VecFromTo(r1, r2)
        force = Vector3.Multiply(r.Normalized(), m1*m2*G)
        force = Vector3.Divide(force, r.Length2())
        return force

    # Calculates the gravitational force acting on Mass 2
    def ForceOnM2(r1, r2, m1, m2):
        r = Vector3.VecFromTo(r2, r1)
        force = Vector3.Multiply(r.Normalized(), m1*m2*G)
        force = Vector3.Divide(force, r.Length2())
        return force

class Newtonian():
    def TimeStepVelocity(v: Vector3, f: Vector3, m: float, timeStep: float):
        a = Vector3.Divide(f, m)
        return Vector3.Add(v, Vector3.Multiply(a, timeStep))

    def TimeStepPosition(r, v, timeStep):
        return Vector3.Add(r, Vector3.Multiply(v, timeStep))
