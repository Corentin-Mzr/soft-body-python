import math

from physics.vector2d import Vector2D
from physics.material import Material
from physics.world import World
from physics.physics_settings import *


class Particle:
    """
    Simple particle class
    """
    __slots__ = ('previous', 'position', 'velocity', 'acceleration', 'material')

    def __init__(self,
                 x: float = 0.0,
                 y: float = 0.0,
                 vx: float = 0.0,
                 vy: float = 0.0,
                 ax: float = 0.0,
                 ay: float = 0.0,
                 material: Material = None):
        """
        Initialize the particle position and velocity
        :param x: Position on the x-axis
        :param y: Position on the y-axis
        :param vx: Velocity on the x-axis
        :param vy: Velocity on the y-axis
        :param ax: Acceleration on the x-axis
        :param ay: Acceleration on the y-axis
        :param material: Material used
        """
        self.position = Vector2D(x, y)
        self.velocity = Vector2D(vx, vy)
        self.acceleration = Vector2D(ax, ay)

        if material is None:
            self.material = Material()
        else:
            self.material = material

    def update(self, world: World) -> None:
        """
        Update the particle motion
        """
        if self.material.mass:
            grav_acc = Vector2D(0.0, GRAVITY)
            drag_acc = self.material.friction / self.material.mass * self.velocity
            self.apply_force(-grav_acc - drag_acc)

            new_pos = self.position + self.velocity * DELTA_TIME + self.acceleration * 0.5 * DELTA_TIME ** 2
            new_vel = self.velocity + self.acceleration * DELTA_TIME * 0.5

            self.position = new_pos
            self.velocity = new_vel

            self.apply_constraint(world)
            self.reset()

    def apply_force(self, force: Vector2D) -> None:
        """
        Apply a force to the particle
        :param force: Force to apply
        """
        if self.material.mass:
            self.acceleration = self.acceleration + force / self.material.mass

    def reset(self) -> None:
        """
        Reset the particle acceleration
        """
        self.acceleration = Vector2D(0, 0)

    def apply_constraint(self, world: World) -> None:
        """
        Apply constraint when the particle reaches the world borders
        :param world: World where the particle is
        """
        if self.material is None:
            return None

        if self.position.x <= 0.0:
            self.position.x = 0.0
            self.velocity.x = abs(self.velocity.x) * self.material.bounce

        if self.position.x >= world.width:
            self.position.x = world.width
            self.velocity.x = -abs(self.velocity.x) * self.material.bounce

        if self.position.y <= 0.0:
            self.position.y = 0.0
            self.velocity.y = abs(self.velocity.y) * self.material.bounce

        if self.position.y >= world.height:
            self.position.y = world.height
            self.velocity.y = -abs(self.velocity.y) * self.material.bounce

    def check_collision(self, other) -> None:
        assert isinstance(other, Particle)
        if (self.position - other.position).norm() <= 2 * PARTICLE_RADIUS:
            angle = math.atan2(other.position.y - self.position.y, other.position.x - self.position.x)
            self.velocity = -self.velocity.norm() * Vector2D(math.cos(angle), math.sin(angle))
            other.velocity = -other.velocity.norm() * Vector2D(math.cos(angle + math.pi), math.sin(angle + math.pi))

    def apply_impulse(self, impulse: Vector2D) -> None:
        """
        Apply an impulse to the particle, making it move
        :param impulse:
        """
        if self.material.mass:
            self.position += impulse / self.material.mass

    def __str__(self):
        return f"Position : ({self.position}) | Velocity : ({self.velocity}) | Acceleration: ({self.acceleration})"

    def set_color(self, color: tuple[int, int, int]) -> None:
        self.material.color = color

    def set_friction(self, friction: float) -> None:
        self.material.friction = friction

    def set_bounce(self, bounce: float) -> None:
        self.material.bounce = bounce

    def set_mass(self, mass: float) -> None:
        self.material.mass = mass
