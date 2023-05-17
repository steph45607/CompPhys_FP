import math

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
        
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )
    

test1 = Vector(7,3,8) + Vector(5,2,1)
print(test1[0])
print(repr(test1))

test2 = Vector(2,7) - Vector(1,4)
print(test2)
print(repr(test2))

test3 = Vector(y=3, z=9)
print(test3)
print(repr(test3))