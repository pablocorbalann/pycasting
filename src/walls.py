import pygame
pygame.init()

class Walls:
    def __init__(self, walls):
        self.width = int(walls["width"])
        self.color = walls["color"]
        self.walls = walls["walls"]

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.line(screen, self.color, wall[0], wall[1], self.width)
