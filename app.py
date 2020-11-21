# This is the main file for the 2d-raycasting Python project.
# Check it out at: https://github.com/pablocorbcon/2d-raycast

# imports needed
import numpy as np
import json
import pygame 
from ray import *
from particle import *

# Global constants
WIDTH = 800
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)

def load_configuration():
    """
    This function loads the configuration from the
    config.json file and then returns it.

    Returns: The configuration
    """
    with open('CONFIG.json', 'r') as f:
        return json.load(f)

class Game:
    """
    This class manages the display and visual part of it.
    """
    def __init__(self, conf):
        """
        This is the constructor method for the Display class. From here all the attributes
        are created.

        Parameters:
            self => The Display class
            conf => The configuration of the game
        """
        # start pygame and create the screen
        pygame.init()
        # get the configuration
        self.conf = conf
        # create the screen for the game
        self.screen = pygame.display.set_mode(SIZE) 
        pygame.display.set_caption(self.conf['general']['title'])
        #Random walls
        self.walls = [] 
        for i in range(5):
            x1 = np.random.randint(0,WIDTH) 
            y1 = np.random.randint(0, HEIGHT)
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
        # Flag variable used to stop the game
        self.running = True
        self.clock = pygame.time.Clock()

    def draw(self):
        """
        This method draws the walls of the screen.

        Parameters:
            self => The Game class
        """
        for wall in self.walls:
            # iter the draws and then draw them
            wall.display(self.screen)
        self.particle.display(self.screen)


    def run(self):
        """
        This method runs the display and starts
        the game loop of pygame

        Parameters:
            self => The Game class
        """
        while self.running:
            self.screen.fill(self.conf['general']['color'])
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
    game = Game(load_configuration())
    game.run()
