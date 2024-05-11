import pygame
import random

from physics.vector2d import Vector2D
from physics.particle import Particle
from physics.spring import Spring
from physics.material import Material
from physics.world import World

from physics.physics_settings import *

from graphics.graphics_settings import *

import math

class PhysicsEngine:
    """
    Simple physics engine, contains the objects to display on screen
    """
    __slots__ = ('particles', 'springs', 'world')

    def __init__(self):

        self.particles = {
            0: Particle(x=WIDTH//2, y=500),
            1: Particle(x=WIDTH//2, y=300),
            2: Particle(x=WIDTH//2 + 100 * math.cos(90 * 3.1415), y=200 + 100 * math.sin(90 * 3.1415))
        }
        self.springs = {
            0: Spring(self.particles[0], self.particles[1], length=200),
            1: Spring(self.particles[1], self.particles[2], length=100)
        }
        self.world = World(Vector2D(0, 0), WIDTH, HEIGHT)

        self.particles[0].set_color((255, 0, 0))
        self.particles[1].set_color((0, 255, 0))
        self.particles[2].set_color((0, 0, 255))

        self.particles[0].set_mass(0)

    def update(self) -> None:
        for pname, particle in self.particles.items():
            particle.update(self.world)

        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                self.particles[i].check_collision(self.particles[j])

        for spring in self.springs.values():
            spring.update()

    def draw(self, screen: pygame.Surface) -> None:
        for spring in self.springs.values():
            pygame.draw.line(screen,
                             (255, 255, 255),
                             (
                                 int(spring.particle1.position.x) + PARTICLE_RADIUS,
                                 screen.get_height() - int(spring.particle1.position.y) - PARTICLE_RADIUS
                             ),
                             (
                                 int(spring.particle2.position.x) + PARTICLE_RADIUS,
                                 screen.get_height() - int(spring.particle2.position.y) - PARTICLE_RADIUS
                             ),
                             SPRING_WIDTH)


        for particle in self.particles.values():
            pygame.draw.circle(screen,
                               particle.material.color,
                               (
                                   int(particle.position.x) + PARTICLE_RADIUS,
                                   screen.get_height() - int(particle.position.y) - PARTICLE_RADIUS
                               ),
                               PARTICLE_RADIUS)


