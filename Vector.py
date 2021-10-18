import math

class Vector3:
    x, y, z = 0, 0, 0
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '<' + "{:.3e}".format(self.x) + ' , ' + "{:.3e}".format(self.y) + ' , ' + "{:.3e}".format(self.z) + '>'
        
    # OPERATION OVERRIDES -----------------------------------------------------------

    # Overrides '+' Operation
    def __add__(self, other): 
        return Vector3.Add(self, other)

    # Overrides '-' Operation
    def __sub__(self, other):
        return Vector3.Subtract(self, other)

    # Overrides '*' Operation
    def __mul__(self, other):
        return Vector3.Multiply(self, other)

    # Overrides '/' Operation
    def __truediv__(self, other):
        return Vector3.Divide(self, other)

    # COMPARISON OVERRIDES ----------------------------------------------------------

    # Overrides '<' Comparison
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y and self.z < other.z
    
    # Overrides '<=' Comparison
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y and self.z <= other.z

    # Overrides '==' Comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    # Overrides '>=' Comparison
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y and self.z >= other.z

    # Overrides '>' Comparison
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y and self.z > other.z

    # Overrides '!=' Comparison
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.z != other.z


    # SELF REFERENCIAL MODIFYING FUNCTIONS ------------------------------------------

    # Normaliizes this vector
    def Normalize(self):
        self = self.Normalized()

    def Invert(self):
        self = self.Inverted()

    # SELF REFERENCIAL RETURNING FUNCTIONS ------------------------------------------

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

    # GENERAL VECTOR FUNCTIONS ------------------------------------------------------

    # Vector representation of 0
    def Zero():
        return Vector3(0, 0, 0)

    # Vector representation of 1
    def One():
        return Vector3(1, 1, 1)

    # Adds two vectors
    def Add(vec1, vec2):
        try:
            return Vector3(vec1.x + vec2.x, vec1.y + vec2.y, vec1.z + vec2.z)
        except:
            raise TypeError("Cannot [V3] add a " + vec1.__class__.__name__ + " and a " + vec2.__class__.__name__)

    # Subtracts two vectors
    def Subtract(vec1, vec2):
        try:
            return Vector3(vec1.x - vec2.x, vec1.y - vec2.y, vec1.z - vec2.z)
        except:
            raise TypeError("Cannot [V3] subtract a " + vec1.__class__.__name__ + " and a " + vec2.__class__.__name__)

    # Subtraction but worded different
    def VecFromTo(vecFrom, vecTo):
        return Vector3.Subtract(vecTo, vecFrom)

    # Multiplies Vector
    def Multiply(vec, b):
        try:
            return Vector3(vec.x * b, vec.y * b, vec.z * b)
        except:
            raise TypeError("Cannot [V3] multiply a " + vec.__class__.__name__ + " and a " + b.__class__.__name__)

    # Divides Vector by a scalar
    def Divide(vec, b):
        try:
            if b != 0:
                return Vector3(vec.x / b, vec.y / b, vec.z / b)
            else:
                return None
        except:
            raise TypeError("Cannot [V3] divide a " + vec.__class__.__name__ + " and a " + b.__class__.__name__)