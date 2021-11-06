import math
import PhysChis
from PhysChisBounds import Bounds, RadialBounds
from Vector import Vector3
import Constants as C
from enum import Enum

# Field: Acts as a constant acceleration (gravity)
class Field:
    acceleration = Vector3.Zero()
    bounds = None
    globalBounds = True

    def __init__(self, acceleration = Vector3.Zero(), bounds = None, globalBounds = True):
        self.acceleration = acceleration
        self.bounds = bounds
        self.globalBounds = globalBounds

    def InsideBounds(self, pos):
        return self.globalBounds or self.bounds.InsideBounds(pos)

    def DistToCenter(self, pos):
        return self.bounds.DistToCenter(pos)

# Generic object: follows standard newtonian motion
class PhysObject:
    position = Vector3.Zero()
    velocity = Vector3.Zero()
    mass = 1
    dynamic = True
    bounds = Bounds()

    def __init__(self, pos=Vector3.Zero(), vel=Vector3.Zero(), mass=1, bounds = Bounds(), dynamic=True):
        self.position = pos
        self.velocity = vel
        self.mass = mass
        self.bounds = bounds
        self.dynamic = dynamic

    # Returns the velocity of the object
    def GetVelocity(self) -> Vector3:
        return self.velocity

    def GetTotalEnergy(self) -> float:
        return 
    
    def GetGamma(self) -> float:
        return PhysChis.Reletavistic.GetGamma(self.velocity.Length())
    
    # Returns the momentum of the object
    def GetMomentum(self) -> Vector3:
        return self.GetVelocity() * self.mass * self.GetGamma()

    # Returns the Approx. momentum of the object
    def GetMomentumApprox(self) -> Vector3:
        return self.GetVelocity() * self.mass


    def SetMomentum(self, momentum: Vector3):
        self.velocity = (momentum / self.mass) / math.sqrt(1 + (momentum.Length()/(self.mass*C.C))**2)

    def SetMomentumApprox(self, momentum: Vector3):
        self.velocity = momentum / self.mass

    # Returns the net acceleration due to fields on the generic object, TO BE OVERRIDEN IN SUBCLASSES
    def GetNetAcceleration(self, objects) -> Vector3:
        netAcc = Vector3.Zero()
        for obj in objects:
            if type(obj) != Field:
                continue
            if obj.InsideBounds(self.position):
                netAcc += obj.acceleration
        return netAcc

    # Returns the net force acting on the object
    def GetNetForce(self, objects) -> Vector3:
        return self.GetNetAcceleration(objects) * self.mass

    # Returns the net impulse acting on the object
    def GetNetImpulse(self, objects) -> Vector3:
        return self.GetNetForce(objects) * C.TIMESTEP

    def GetRestEnergy(self):
        return self.mass*(C.C**2)
    
    def GetTotalEnergy(self):
        return self.GetRestEnergy()*self.GetGamma()

    def GetKineticEnergy(self):
        return self.GetTotalEnergy() - self.GetRestEnergy()

    def GetKineticEnergyApprox(self):
        return self.velocity.Length2()*self.mass*0.5

    def SetKineticEnergy(self, energy):
        newMomentum = math.sqrt(((energy+self.GetRestEnergy())**2) - (self.mass*(C.C**2))**2)/C.C
        self.SetMomentum(self.velocity.Normalized() * newMomentum)

    # Updates the position and velocity of this object by [TIMESTEP] seconds
    def Tick(self, objects):
        self.velocity += self.GetNetAcceleration(objects) * C.TIMESTEP
        self.position += self.GetVelocity() * C.TIMESTEP

    def CollisionCheck(self, other):
        # If the closest point on the bounds of the object is inside this objects bounds, a collision has occured
        return self.bounds.InsideBounds(self.position, other.bounds.ClosestPointOnBounds(other.position, self.position))

        

class CelestialObject(PhysObject):
    def __init__(self, pos=Vector3.Zero(), vel=Vector3.Zero(), mass=1, bounds=Bounds(), dynamic=True):
        super().__init__(pos, vel, mass, bounds, dynamic)

    # Returns the net acceleration due to fields on the object, AND acceleration due to other Celestial Objects
    def GetNetAcceleration(self, objects) -> Vector3:
        netAcc = super().GetNetAcceleration(objects)
        for celobj in objects:
            if celobj == self:
                continue
            if type(celobj) != CelestialObject:
                continue
            netAcc += PhysChis.GravitationalFields.AccelerationByMass(self.position, celobj.position, celobj.mass)
        return netAcc


class System(PhysObject):
    objects = []
    def __init__(self, objects = []):
        self.objects = objects

    def NumObjects(self):
        numObjs = 0
        for obj in self.objects:
            if isinstance(obj, PhysObject):
                numObjs += 1
        if numObjs > 0:
            return numObjs
        else:
            raise Warning("No non-field objects in system!")

    def GetNetMass(self):
        netM = 0
        for obj in self.objects:
            if isinstance(obj, PhysObject):
                netM += obj.mass
        return netM

    def CenterOfMass(self):
        centerM = Vector3.Zero()
        for obj in self.objects:
            if isinstance(obj, PhysObject):
                centerM += obj.position * obj.mass
        return centerM / self.GetNetMass()

    def CenterOfMassVelocity(self):
        centerMV = Vector3.Zero()
        for obj in self.objects:
            if isinstance(obj, PhysObject):
                centerMV += obj.velocity * obj.mass
        return centerMV / self.GetNetMass()

    def Tick(self):
        for obj in self.objects:
            if isinstance(obj, PhysObject):
                obj.Tick(self.objects)

    def GetMomentum(self):
        momentum = Vector3.Zero()
        for obj in self.objects:
            if isinstance(obj, PhysObject):
                momentum += obj.GetMomentum()
        return momentum

    def GetVelocity(self):
        vel = Vector3.Zero()
        for obj in self.objects:
            if isinstance(obj, PhysObject):
                vel += obj.GetVelocity()
        return vel

    def GetNetAcceleration(self):
        acc = Vector3.Zero()
        for obj in self.objects:
            if isinstance(obj, PhysObject):
                acc += obj.GetNetAcceleration(self.objects)
        return acc

    def GetNetForce(self):
        force = Vector3.Zero()
        for obj in self.objects:
            if isinstance(obj, PhysObject):
                force += obj.GetNetForce(self.objects)
        return force

