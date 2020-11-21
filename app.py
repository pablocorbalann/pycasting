# This is the main file for the 2d-raycasting Python project.
# Check it out at: https://github.com/pablocorbcon/2d-raycast

# imports needed
import numpy as np
import json
import pygame 
from src.ray import *
from src.particle import *

# Global constants
WIDTH = 600
HEIGHT = 600
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
        # load all the walls from the configuration file and store
        # them in the self.walls list using the Limits() class
        wall_color = self.conf['walls']['color']
        wall_width = self.conf['walls']['width']
        self.walls = []
        for wall in self.conf['walls']['walls']:
            self.walls.append(Limits(wall[0], wall[1], wall_color, wall_width))
        # walls for avoiding render of rays outsite the screen
        self.walls.append(Limits((0, 0), (WIDTH, 0), self.conf['general']['color'], wall_width))
        self.walls.append(Limits((0, 0), (0, HEIGHT), self.conf['general']['color'], wall_width))
        self.walls.append(Limits((0, HEIGHT), (WIDTH, HEIGHT), self.conf['general']['color'] , wall_width))
        self.walls.append(Limits((WIDTH, 0), (WIDTH, HEIGHT), self.conf['general']['color'], wall_width))
        self.particle = Particle(self.conf['ray'])
        # Flag variable used to stop the game
        self.running = True
        # clock for the pygame fps
        self.fps = 60 # max fps
        self.clock = pygame.time.Clock()
        self.player_position = [self.conf['player']['x position'], self.conf['player']['y position']]

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
        pygame.draw.circle(self.screen, self.conf['player']['color'], self.player_position, self.conf['player']['radius'])


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
                    self.running = False # stop the game
                elif event.type == pygame.MOUSEMOTION:
                    # get the mouse position and update the particle
                    self.player_position = event.pos
                    self.particle.position[0] = self.player_position[0]
                    self.particle.position[1] = self.player_position[1]
            # draw all the things needed
            self.particle.look(self.screen,self.walls)
            self.draw()
            self.clock.tick(self.fps)
            pygame.display.update()


if __name__ == '__main__':
    game = Game(load_configuration())
    game.run()
