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

    def GetVelocity(self) -> Vector3:
        return self.velocity
    
    def GetMomentum(self) -> Vector3:
        return self.GetVelocity() * self.mass

    def GetNetAcceleration(self) -> Vector3:
        netAcc = Vector3.Zero()
        for field in self.fieldCollection:
            if field.InsideBounds(self.position):
                netAcc += field.acceleration
        return netAcc

    def GetNetForce(self) -> Vector3:
        return self.GetNetAcceleration() * self.mass

    def GetNetImpulse(self) -> Vector3:
        return self.GetNetForce() * C.TIMESTEP

    def Tick(self):
        self.velocity += self.GetNetAcceleration() * C.TIMESTEP
        self.position += self.GetVelocity() * C.TIMESTEP
        