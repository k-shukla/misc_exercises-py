''' As practice with using classes, I'm going to define a class corresponding to three-vectors
    (named, appropriately, ThreeVec).
   
    ThreeVec will support vector addition and subtraction, scalar multiplication and division, dot
    products (which, perhaps confusingly, will /also/ be represented by *, so that for three vectors
    v1 and v2 and a scalar k, scalar multiplication will be represented as k * v1, and dot products
    will be represented as v1 * v2), magnitudes, the creation of unit vectors, component-by-component
    comparison, and parity. '''

class ThreeVec(object):
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
#    def __str__(self):
#        return "<%s, %s, %s>" % (self.x, self.y, self.z)
    
    def __repr__(self):
        return str([self.x, self.y, self.z])
    
    def __add__(self, vec2):
        if type(vec2) == ThreeVec:
            return ThreeVec(self.x + vec2.x, self.y + vec2.y, self.z + vec2.z)
        else:
            raise TypeError("+ with type 'ThreeVec' supports only operand type 'ThreeVec'")
    
    def __sub__(self, vec2):
        if type(vec2) == ThreeVec:
            return ThreeVec(self.x - vec2.x, self.y - vec2.y, self.z - vec2.z)
        else:
            raise TypeError("- with type 'ThreeVec' supports only operand type 'ThreeVec'")
    
    ''' An added benefit of the way __add__ and __sub__ are defined is that __radd__ and __rsub__ don't need to be defined; v2 + v1
        automatically passes to v2's +/- operations. '''

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            return ThreeVec(other * self.x, other * self.y, other * self.z)
        elif type(other) == ThreeVec:
            return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
        else:
            raise TypeError("* with type 'ThreeVec' supports only operand types 'float', 'int', and 'ThreeVec'")
    
    def __rmul__(self, other):
        if type(other) == float or type(other) == int:
            return ThreeVec(other * self.x, other * self.y, other * self.z)
        elif type(other) == ThreeVec:
            return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
        else:
            raise TypeError("* with type 'ThreeVec' supports only operand types 'float', 'int', and 'ThreeVec'")
    
    def __div__(self, other):
        if type(other) == float or type(other) == int:
            return ThreeVec(self.x/other, self.y/other, self.z/other)
        else:
            raise TypeError("/ with type 'ThreeVec' supports only operand types 'float' and 'int'")
    
    def __truediv__(self, other):
        if type(other) == float or type(other) == int:
            return ThreeVec(self.x/other, self.y/other, self.z/other)
        else:
            raise TypeError("/ with type 'ThreeVec' supports only operand types 'float' and 'int'")
    
    def __xor__(self, vec2):
        if type(vec2) == ThreeVec:
            return ThreeVec((self.y * vec2.z) - (self.z * vec2.y), (self.z * vec2.x) - (self.x * vec2.z), (self.x * vec2.y) - (self.y * vec2.x))
        else:
            raise TypeError("^ with type 'ThreeVec' supports only operand type 'ThreeVec'")
    
    # As with __add__ and __sub__, by construction, we don't need to define __rxor__.
    
    def __abs__(self):
        return self.mag()
    
    # Hopefully, by defining __abs__(self) as just self.mag() I'm not being willfully perverse. =c
    
    def __lt__(self, other):
        raise TypeError("unsupported operand type for '<': 'ThreeVec'")
    
    def __le__(self, other):
        raise TypeError("unsupported operand type for '<=': 'ThreeVec'")
    
    def __eq__(self, other):
        raise TypeError("unsupported operand type for '==': 'ThreeVec'")
    
    def __ne__(self, other):
        raise TypeError("unsupported operand type for '!=': 'ThreeVec'")
    
    def __gt__(self, other):
        raise TypeError("unsupported operand type for '>': 'ThreeVec'")
    
    def __ge__(self, other):
        raise TypeError("unsupported operand type for '>=': 'ThreeVec'")
    
    def unit(self):
        mag = self.mag()
        return ThreeVec(self.x/mag, self.y/mag, self.z/mag)
    
    def equal_components(self, vec2):
        if type(vec2) == ThreeVec:
            if self.x == vec2.x and self.y == vec2.y and self.z == vec2.z:
                return True
            else:
                return False
        else:
            raise TypeError("function 'equal_components' requires type 'ThreeVec'")
    
    def parity(self):
        return ThreeVec(-self.x, -self.y, -self.z)

E_field = ThreeVec(12, 4, 5)
B_field = ThreeVec (5, 3, 5)

print E_field.__dict__
