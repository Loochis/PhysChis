from PhysChisObjects import Field, Object
from Vector import Vector3
import Constants as C

gravityField = Field(Vector3(0, -9.8, 0), globalBounds=True)
ball1 = Object(mass=1, fields=[gravityField], vel=Vector3(0,0,0), pos=Vector3(0, 10, 0))

time = 0
while(ball1.position.y > 0):
    print("pos:",ball1.position,"t:",round(time, len(str(C.TIMESTEP))))
    ball1.Tick()
    time += C.TIMESTEP