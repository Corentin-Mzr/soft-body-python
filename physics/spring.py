from physics.vector2d import Vector2D
from physics.particle import Particle
from physics.physics_settings import *


class Spring:
    """
    Simple spring class
    """
    __slots__ = ('particle1', 'particle2', 'length', 'hooke', 'damp')

    def __init__(self, particle1: Particle,
                 particle2: Particle,
                 length: float,
                 hooke_coef: float = SPRING_CONSTANT,
                 damp_coef: float = SPRING_DAMPING):
        """
        Initialize the spring
        :param particle1: Position of the first particle
        :param particle2: Position of the second particle
        :param length: Length of the spring
        """
        self.particle1 = particle1
        self.particle2 = particle2
        self.length = length
        self.hooke = hooke_coef
        self.damp = damp_coef

    def update(self) -> None:
        """
        Update the spring
        """
        dxdy = self.particle2.position - self.particle1.position
        dist = dxdy.norm()
        spring_force = self.hooke * (dist - self.length)

        dv = self.particle2.velocity - self.particle1.velocity

        if self.particle1.material.mass:
            self.particle1.apply_force(
                spring_force / self.particle1.material.mass * dxdy + self.damp / self.particle1.material.mass * dv
            )

        if self.particle2.material.mass:
            self.particle2.apply_force(
                -spring_force / self.particle2.material.mass * dxdy - self.damp / self.particle2.material.mass * dv
            )
