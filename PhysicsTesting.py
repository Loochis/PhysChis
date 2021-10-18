from PhysChisObjects import Field, Object
from Vector import Vector3
import PhysChis

gravityField = Field(Vector3(0, -9.8, 0), globalBounds=True)
ball1 = Object(mass=1, fields=[gravityField])

print(ball1.GetNetImpulse())