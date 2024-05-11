from physics.vector2d import Vector2D


class World:
    """
    Simple world class
    """
    def __init__(self, center: Vector2D, width: float, height: float):
        self.center = center
        self.width = width
        self.height = height
