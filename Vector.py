import math

class Vector3:
    x, y, z = 0, 0, 0
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '<' + "{:.3e}".format(self.x) + ' , ' + "{:.3e}".format(self.y) + ' , ' + "{:.3e}".format(self.z) + '>'
        
    # Magnitude of the Vector squared
    def Length2(self):
        return (self.x**2) + (self.y**2) + (self.z**2)

    # Magnitude of the vector
    def Length(self):
        return math.sqrt(self.Length2())

    # Normalized version of the vector
    def Normalized(self):
        length = self.Length()
        return Vector3(self.x / length, self.y / length, self.z / length)

    # Inverted version of the vector
    def Inverted(self):
        return Vector3(-self.x, -self.y, -self.z)

    # Adds to this vector
    def PlusEquals(self, vec):
        return Vector3(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    # Vector representation of 0
    def Zero():
        return Vector3(0, 0, 0)

    # Vector representation of 1
    def One():
        return Vector3(1, 1, 1)

    # Adds two vectors
    def Add(vec1, vec2):
        return Vector3(vec1.x + vec2.x, vec1.y + vec2.y, vec1.z + vec2.z)

    # Subtracts two vectors
    def Subtract(vec1, vec2):
        return Vector3(vec1.x - vec2.x, vec1.y - vec2.y, vec1.z - vec2.z)

    # Subtraction but worded different
    def VecFromTo(vecFrom, vecTo):
        return Vector3.Subtract(vecTo, vecFrom)

    # Multiplies Vector by a scalar
    def Multiply(vec, b):
        return Vector3(vec.x * b, vec.y * b, vec.z * b)

    # Divides Vector by a scalar
    def Divide(vec, b):
        if b != 0:
            return Vector3.Multiply(vec, 1.0 / b)
        else:
            return None