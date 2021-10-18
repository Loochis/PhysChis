import PhysChis
from Vector import Vector3
import Constants

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

    def GetVelocity(self):
        return self.velocity
    
    def GetMomentum(self):
        return self.GetVelocity()

    def GetNetForce(self):
        raise NotImplementedError

    def GetNetImpulse(self):
        return self.GetNetForce()