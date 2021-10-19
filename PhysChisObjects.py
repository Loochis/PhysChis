import PhysChis
from Vector import Vector3
import Constants as C

# Field: Acts as a constant acceleration (gravity)
class Field:
    acceleration = Vector3.Zero()
    bounds = (Vector3.One(), Vector3.One)
    globalBounds = True

    def __init__(self, acceleration = Vector3.Zero(), bounds = (Vector3.One(), Vector3.One()), globalBounds = True):
        self.acceleration = acceleration
        self.bounds = bounds
        self.globalBounds = globalBounds

    def InsideBounds(self, pos):
        return self.globalBounds or (self.bounds[0] <= pos <= self.bounds[1])
        
# Generic object: follows standard newtonian motion
class Object:
    position = Vector3.Zero()
    velocity = Vector3.Zero()
    mass = 1
    dynamic = True
    objCollection = []
    fieldCollection = []

    def __init__(self, pos=Vector3.Zero(), vel=Vector3.Zero(), mass=1, dynamic=True, objects = [], fields = []):
        self.position = pos
        self.velocity = vel
        self.mass = mass
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
        