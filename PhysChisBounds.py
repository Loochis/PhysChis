from Vector import Vector3

# Generic boundary, basically useless
class Bounds():
    position = Vector3.Zero()
    def __init__(self, pos=Vector3.Zero()):
        self.position = pos

    def InsideBounds(self, offset:Vector3, point: Vector3):
        raise NotImplementedError

    def DistToCenter(self, offset:Vector3, point: Vector3):
        return Vector3.Length(self.position - point)

    def ClosestPointOnBounds(self, point: Vector3) -> Vector3:
        raise NotImplementedError

# Spherical boundary
class RadialBounds(Bounds):
    radius = 0
    def __init__(self, pos=Vector3.Zero(), radius=0):
        super().__init__(pos)
        self.radius = radius

    def InsideBounds(self, offset:Vector3, point: Vector3):
        return Vector3.Length2(self.position + offset - point) <= self.radius**2

    def ClosestPointOnBounds(self, offset:Vector3, point: Vector3) -> Vector3:
        return Vector3.VecFromTo(self.position + offset, point).Normalized() * self.radius

# Box boundary
class BoxBounds(Bounds):
    corners = [Vector3.One(), Vector3.One() * -1] # Corners are relative to the position
    def __init__(self, pos=Vector3.Zero(), corners = [Vector3.One(), Vector3.One() * -1]):
        super().__init__(pos)
        self.corners = corners

    def InsideBounds(self, offset:Vector3, point: Vector3):
        lower = Vector3(min(self.corners[0].x, self.corners[1].x), min(self.corners[0].y, self.corners[1].y), min(self.corners[0].z, self.corners[1].z)) # Get bottom left of box
        higher = Vector3(max(self.corners[0].x, self.corners[1].x), max(self.corners[0].y, self.corners[1].y), max(self.corners[0].z, self.corners[1].z)) # Get top right of box
        return lower + self.position + offset < point < higher + self.position + offset