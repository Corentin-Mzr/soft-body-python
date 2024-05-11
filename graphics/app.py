import pygame
import sys

from graphics.graphics_settings import *
from physics.physics_engine import PhysicsEngine


class App:
    """
    Simple application class with Pygame
    """
    def __init__(self):
        """
        Initialize the application
        """
        # Initialize Pygame
        pygame.init()

        # Define window settings
        self.width = WIDTH
        self.height = HEIGHT
        self.title = TITLE

        # Create pygame variables
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.is_running = True

        # FPS counter
        self.fps = 0
        self.last_time = 0

        # Physics engine, objects to display on screen
        self.physics_engine = PhysicsEngine()

    def run(self) -> None:
        """
        Run the application
        """
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick()

        self.quit()

    def handle_events(self) -> None:
        """
        Handle events in app
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self) -> None:
        """
        Do updates here
        """
        # Update FPS Counter
        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= 1000:
            self.fps = self.clock.get_fps()
            self.last_time = current_time

        # Update physics engine
        self.physics_engine.update()

    def render(self) -> None:
        """
        Render on screen
        """
        # Clear screen
        self.screen.fill(BG_COLOR)

        # Draw
        self.physics_engine.draw(self.screen)

        # Render
        self.display_fps()
        pygame.display.flip()

    @staticmethod
    def quit() -> None:
        """
        Exit the application and destroy objects if necessary
        """
        pygame.quit()
        sys.exit()

    def display_fps(self) -> None:
        font = pygame.font.Font(None, 36)
        fps_text = font.render(f"FPS: {self.fps:.0f}", True, (255, 255, 255))
        self.screen.blit(fps_text, (10, 10))

