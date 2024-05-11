class Vector2D:
    """
    Simple 2D Vector class
    """
    __slots__ = ('x', 'y')

    def __init__(self, x: float = 0.0, y: float = 0.0):
        """
        Initialize the vector
        :param x: Position on x-axis
        :param y: Position on y-axis
        """
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False

    def __abs__(self):
        """
        Norm of the vector
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    norm = __abs__

    def __add__(self, other):
        assert isinstance(other, Vector2D)
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        assert isinstance(other, Vector2D)
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        assert isinstance(other, Vector2D)
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        assert isinstance(other, Vector2D)
        self.x -= other.x
        self.y -= other.y

    def __mul__(self, other):
        assert isinstance(other, (int, float, Vector2D))
        if type(other) in (int, float):
            return Vector2D(self.x * other, self.y * other)
        return Vector2D(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__

    def __imul__(self, other):
        assert isinstance(other, (int, float))
        self.x *= other
        self.y *= other

    def __truediv__(self, other):
        assert isinstance(other, (int, float))
        return Vector2D(self.x / other, self.y / other)

    def __idiv__(self, other):
        assert isinstance(other, (int, float))
        self.x /= other
        self.y /= other

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __pos__(self):
        return Vector2D(self.x, self.y)

    def normalize(self):
        """
        Normalize the vector
        """
        length = self.norm()
        return Vector2D(self.x / length, self.y / length)

    def dot(self, other) -> float:
        """
        Dot product
        """
        assert isinstance(other, Vector2D)
        return self.x * other.x + self.y * other.y

    def distance(self, other) -> float:
        """
        Distance between two vectors
        """
        assert isinstance(other, Vector2D)
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f"Vector2D(x={self.x}, y={self.y})"

    def __pow__(self, power):
        assert isinstance(power, (int, float))
        return Vector2D(self.x ** power, self.y ** power)

    def sign(self):
        """
        Return the sign of each component of the vector, i.e -1 if the value is negative and 1 if positive
        """
        return Vector2D(1 if self.x >= 0 else -1, 1 if self.y >= 0 else -1)
