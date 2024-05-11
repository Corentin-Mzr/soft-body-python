from physics.physics_settings import *


class Material:
    """
    Simple material class
    """
    __slots__ = ('mass', 'friction', 'bounce', 'color')

    def __init__(self,
                 mass: float = PARTICLE_MASS,
                 friction: float = MATERIAL_FRICTION,
                 bounce: float = MATERIAL_BOUNCE,
                 color: tuple[int, int, int] = MATERIAL_COLOR):
        if friction < 0 or friction > 1:
            raise ValueError("Friction must be between 0 and 1")
        if bounce < 0 or bounce > 1:
            raise ValueError("Bounce must be between 0 and 1")
        if mass < 0:
            raise ValueError("Mass must be positive")

        self.mass = mass
        self.friction = friction
        self.bounce = bounce
        self.color = color
