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
    objCollection = []
    fieldCollection = []

    def __init__(self, pos=Vector3.Zero(), vel=Vector3.Zero(), mass=1, bounds = Bounds(), dynamic=True, objects = [], fields = []):
        self.position = pos
        self.velocity = vel
        self.mass = mass
        self.bounds = bounds
        self.dynamic = dynamic
        self.objCollection = objects
        self.fieldCollection = fields

    # Returns the velocity of the object
    def GetVelocity(self) -> Vector3:
        return self.velocity
    
    # Returns the momentum of the object
    def GetMomentum(self) -> Vector3:
        return self.GetVelocity() * self.mass

    # Returns the net acceleration due to fields on the generic object, TO BE OVERRIDEN IN SUBCLASSES
    def GetNetAcceleration(self) -> Vector3:
        netAcc = Vector3.Zero()
        for field in self.fieldCollection:
            if field.InsideBounds(self.position):
                netAcc += field.acceleration
        return netAcc

    # Returns the net force acting on the object
    def GetNetForce(self) -> Vector3:
        return self.GetNetAcceleration() * self.mass

    # Returns the net impulse acting on the object
    def GetNetImpulse(self) -> Vector3:
        return self.GetNetForce() * C.TIMESTEP

    # Updates the position and velocity of this object by [TIMESTEP] seconds
    def Tick(self):
        self.velocity += self.GetNetAcceleration() * C.TIMESTEP
        self.position += self.GetVelocity() * C.TIMESTEP

    def CollisionCheck(self, other):
        # If the closest point on the bounds of the object is inside this objects bounds, a collision has occured
        return self.bounds.InsideBounds(self.position, other.bounds.ClosestPointOnBounds(other.position, self.position))

        

class CelestialObject(PhysObject):
    def __init__(self, pos=Vector3.Zero(), vel=Vector3.Zero(), mass=1, bounds=Bounds(), dynamic=True, objects = [], fields = []):
        super().__init__(pos, vel, mass, bounds, dynamic, objects, fields)

    # Returns the net acceleration due to fields on the object, AND acceleration due to other Celestial Objects
    def GetNetAcceleration(self) -> Vector3:
        netAcc = super().GetNetAcceleration()
        for celobj in self.objCollection:
            if celobj == self:
                continue
            if type(celobj) != CelestialObject:
                continue
            netAcc += PhysChis.GravitationalFields.AccelerationByMass(self.position, celobj.position, celobj.mass)
        return netAcc


class StandardObjects(Enum):
    EARTH = CelestialObject(mass=5.972e24, bounds=RadialBounds(radius=6378100))
    BASEBALL = CelestialObject(mass=0.145, bounds=RadialBounds(radius=0.0365))