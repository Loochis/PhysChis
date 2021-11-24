from Vector import Vector3
import Constants as C
import math

class Kinematics:
    def VWithoutD(vi, a, t):
        return vi + a*t
    def DwithoutA(vi, vf, t):
        return (vi+vf)*0.5*t
    def VfWithoutT(vi, a, d):
        return vi**2 + 2*a*d
    def AWithoutT(vi, vf, d):
        return (vf**2 - vi**2) / (2*d)

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


class Newtonian:
    def TimeStepVelocity(v: Vector3, f: Vector3, m: float, timeStep: float):
        a = f / m
        return v + (a * timeStep)

    def TimeStepPosition(r, v, timeStep):
        return r + (v * timeStep)

    # Calculates p2f
    def MomentumTransfer(p1i, p2i, p1f):
        netP = p1i+p2i
        p2f = netP-p1f
        return p2f

    # Calculates p1f and p2f where they are the same
    def MomentumSplit(p1i, p2i):
        netP = p1i+p2i
        return netP/2.0

    # Calculates v1f and v2f where they are the same (Momentum transfer)
    def CollideToSameVelocity(v1i, v2i, m1, m2):
        p1i = v1i*m1
        p2i = v2i*m2
        return (p1i + p2i) / (m1 + m2)
    
    def GetOrbitalVelocity(r, mP):
        return math.sqrt((C.G*mP)/r)
    
    def GetOrbitalRadius(v, mP):
        return (C.G*mP)/(v**2)
    
    def GetSpringStiffnessFromGravity(m, x):
        return (m*9.8) / x
        

class Reletavistic:
    def GetGamma(v):
        return 1.0 / math.sqrt(1 - (v**2 / C.C**2))
    
    def MatchSpeedToEnergy(mKinetic, mStatic):
        eStatic = mStatic*C.C**2
        eRestKinetic = mKinetic*C.C**2
        gamma = (eStatic/eRestKinetic)+1
        return math.sqrt((1 - ((1 / gamma)**2)) * C.C**2)

class Energy:
    def WorkOverDistance(force, displacement):
        return Vector3.Dot(force, displacement)
    
    def GetRestEnergy(mass):
        return mass*C.C**2
    
    def GetTotalEnergy(mass, speed):
        return Energy.GetRestEnergy(mass)*Reletavistic.GetGamma(speed)
        
    def GetKineticEnergy(speed, mass):
        return Energy.GetRestEnergy(mass)*(Reletavistic.GetGamma(speed)-1)
    
    def GetKineticEnergyApprox(speed, mass):
        return 0.5 * mass * (speed**2)
    
    def GetSpeedFromEnergyApprox(energy, mass):
        return math.sqrt(energy / (mass * 0.5))
    
    def GetSpeedFromEnergy(energy, mass):
        newMomentum = math.sqrt(((energy+Energy.GetRestEnergy(mass))**2) - (mass*(C.C**2))**2)/C.C
        return (newMomentum / mass) / math.sqrt(1 + (newMomentum/(mass*C.C))**2)
    
    def GravPotentialAtDist(m1, m2, height):
        return (-C.G*m1*m2)/height
    
    def GetEscapeVelocityApprox(mPlanet, hieghtInitial, finalSpeed):
        eFinalOverM = 0.5*finalSpeed**2
        eInitialOverM = Energy.GravPotentialAtDist(mPlanet, 1, hieghtInitial)
        eDiff = eFinalOverM - eInitialOverM
        return Energy.GetSpeedFromEnergyApprox(eDiff, 1)
    
    def ElectricPotentialAtDist(c1, c2, dist):
        return (C.ONE_OVER_4PIE0*c1*c2)/dist
    
    def DistAtElectricPotential(c1, c2, energy):
        return (C.ONE_OVER_4PIE0*c1*c2) / energy
    
    def ElasticPotentialAtDistance(k, x):
        return 0.5*k*x**2
    
    def DistanceFromElasticPotential(k, pE):
        return math.sqrt(pE / (0.5*k))
    
class Thermal:
    def DeltaTEToDeltaTemp(c, mKG, deltaTE):
        return deltaTE / (c*(mKG*1000))
    
    def DeltaTempToDeltaTE(c, mKG, deltaTemp):
        return deltaTemp*c*(mKG*1000)
    
    def TempFromMix(m1, c1, t1, m2, c2, t2):
        a = m1*c1*1000
        b = m2*c2*1000
        return (a*t1 + b*t2)/(a + b)
