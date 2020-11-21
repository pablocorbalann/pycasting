# This is the main file for the 2d-raycasting Python project.
# Check it out at: https://github.com/pablocorbcon/2d-raycast

# imports needed
import numpy as np
import pygame 
from ray import *
from particle import *

# Global constants
WIDTH = 800
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)


class Display:
    """
    This class manages the display and visual part of it.
    """
    def __init__(self):
        """
        This is the constructor method for the Display class. From here all the attributes
        are created.

        Parameters:
            self => The Display class
        """
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN)

        #Random walls
        self.walls = []
        for i in range(5):
            x1 = np.random.randint(0,WIDTH)
            y1  = np.random.randint(0, HEIGHT)
            x2 = np.random.randint(0, WIDTH)
            y2 = np.random.randint(0, HEIGHT)
            x3 = np.random.randint(0, WIDTH)
            y3 = np.random.randint(0, HEIGHT)
            self.walls.append(Limits(x1,y1,x2,y2))

        self.walls.append(Limits(0,0,WIDTH,0))
        self.walls.append(Limits(0, 0, 0, HEIGHT))
        self.walls.append(Limits(0, HEIGHT, WIDTH, HEIGHT))
        self.walls.append(Limits(WIDTH, 0, WIDTH, HEIGHT))
        self.particle = Particle()
        self.stopgame = False
        self.clock = pygame.time.Clock()

    def draw(self):
        for wall in self.walls:
            wall.display(self.screen)
        self.particle.display(self.screen)


    def run(self):
        while not self.stopgame:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stopgame = True
                #mouse position
                if event.type == pygame.MOUSEMOTION:
                    pos = event.pos
                    self.particle.pos[0] = pos[0]
                    self.particle.pos[1] = pos[1]

            self.particle.look(self.screen,self.walls)
            self.draw()
            self.clock.tick(100)
            pygame.display.update()


if __name__ == '__main__':
    D = Display()
    D.run()
