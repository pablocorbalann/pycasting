import pygame

from numpy import array
from numpy import deg2rad
from numpy import linalg


from ray import *


class Particle:
    def __init__(self, conf):
        self.pos = array([250, 250])
        self.color = conf['color']
        self.width = conf['width']

    def display(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, 1, self.width)

        for ray in self.rays:
            ray.display(screen)

    def look(self, screen, walls):
        self.rays = []
        for i in range(0, 360, 4):
            self.rays.append(Ray(self.pos[0], self.pos[1], deg2rad(i)))
        for ray in self.rays:
            closest = 10000000
            closestpt = None
            for wall in walls:
                pt = ray.cast(wall)

                if pt is not None:
                    dis = linalg.norm(pt - self.pos)
                    if (dis < closest):
                        closest = dis
                        closestpt = pt

            if closestpt is not None:
                pygame.draw.line(screen, self.color, self.pos, array(closestpt, int), self.width)
