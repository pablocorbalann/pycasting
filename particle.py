import pygame
from numpy import array, linalg, deg2rad
from ray import *

class Particle:
    """
    This class is used to manage all the Particles that the player generates
    and cast them
    """
    def __init__(self, conf):
        """
        This is the constructor method for the Particle class. 
        From here all the attributes of the instance are created.

        Parameters:
            self => The Particle class
            conf => The configuration dic for the particles
        """
        self.position = array([250, 250])
        self.color = conf['color']
        self.width = conf['width']

    def display(self, screen):
        """
        This function is used to draw the particle in a given
        pygame surface.

        Parameters:
            self => The Particle class
            screen => The surface to draw in
        """
        pygame.draw.circle(screen, self.color, self.position, 1, self.width)
        for ray in self.rays:
            # iter the rays and display them
            ray.display(screen)

    def look(self, screen, walls):
        """
        This function is used to find the walls of the game in a given 
        pygame surface and store them in a list.

        Parameters:
            self => The Particle class
            screen => The surface to draw in
            walls => The walls to look for
        """
        self.rays = []
        for i in range(0, 360, 7):
            # generate (360/n) rays arround the player
            self.rays.append(Ray(self.position[0], self.position[1], deg2rad(i)))
        # cast those rays and look for walls
        for ray in self.rays:
            closest = 10000000
            closestpt = None
            # iter the walls to be casted
            for wall in walls:
                casted = ray.cast(wall)
                if casted is not None:
                    distance = linalg.norm(casted - self.position)
                    if (distance < closest):
                        # check the contact between the ray and the casted wall
                        closest = distance
                        closestpt = casted
            if closestpt is not None:
                # draw the line if the closest point is not none
                pygame.draw.line(screen, self.color, self.position, array(closestpt, int), self.width)
