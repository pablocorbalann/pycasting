import pygame
from numpy import array, linalg, cos, sin

class Limits:
    """
    The limit class manages all the limits (or walls)
    for the app
    """
    def __init__(self, start, end, color, width):
        """
        This is the constructor method, from here all the attributes
        of the class are created.

        Parameters:
            start => The start position
            end => The end position
            color => The color  of the line
            width => The width of the line
        """
        self.start = start
        self.end = end
        self.color = color
        self.width = width

    def display(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end,  self.width)


class Ray:
    """
    THis class manages the Rays of the player to then
    display them and check the cordenates.
    """
    def __init__(self, x, y,radius):
        """
        This is the constructor method for the Ray class. It uses 
        parameters for creating the attributes.

        Parameters.
            x => The x position of the ray
            y => The y position of the ray
            radius => The radius for the ray
        """
        self.position = [x, y]
        # get the direction of the ray
        self.direction = array([cos(radius), sin(radius)])

    def display(self, screen):
        """
        This method displays the ray itself in a given pygame surface

        Parameters:
            screen => The screen to draw in
        """
        pygame.draw.line(screen, (255, 255, 255), self.position, self.position + self.direction , 1)

    def cast(self, wall):
        """
        This method uses mathematical formulas for 
        casting the rays in a given wall.

        Parameters:
            wall => The wall to cast in (Limit)

        Returns: The casted coordenates of the ray and the wall
        """
        # Get the points of the wall (start and end)
        x1 = wall.start[0]
        y1 = wall.start[1]
        x2 = wall.end[0]
        y2 = wall.end[1]
        # Position of the ray
        x3 = self.position[0]
        y3 = self.position[1]
        x4 = self.position[0] + self.direction[0]
        y4 = self.position[1] + self.direction[1]
        
        # knowing the form of 
        #   t = numerator / denominator
        #   u = -[(x1-x2) * (y3-y4) - (y1-y2) * (x1-x3)] / denominator
        # calculate the values of ~t and ~u
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        numerator = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        if denominator == 0:
            # The numerator was null
            return None  
        t = numerator / denominator
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator
        # Check the condition for updating x 
        #   (t > 0) ∧ (t < 1) ∧ (u > 0)
        if (t > 0) and (t < 1) and (u > 0):
            # If 1, get the x coordenate and the y cordenate
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            # convert (x, y) to an array and then return it
            coordenates = array([x,y])
            return coordenates
