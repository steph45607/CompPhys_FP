import math

#? Class to make the base vector for velocity and position
class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector ({self.x}, {self.y}, {self.z})"
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("There are only 3 variables in coordinates!!!")
        
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )
    
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return (
                self.x * other.x,
                self.y * other.y,
                self.z * other.z
            )
        elif isinstance(other,(int,float)):
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other
            )
        else:
            raise TypeError("Must be Vector, int or float")
        
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(
                self.x / other,
                self.y / other,
                self.z / other,
            )
        else:
            raise TypeError("Must be int or float")
        
    #// √((x^2) + (y^2) + (z^2))
    def get_magnitude(self):
        #// getting the magnitude/distance of the vectors
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalize(self):
        magnitude = self.get_magnitude()
        #// dividing the vector with its magnitude
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )