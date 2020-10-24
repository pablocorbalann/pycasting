import pygame
pygame.init()

# Player class
class Player:

    def __init__(self, player):
        self.x = int(player["x position"])
        self.y = int(player["y position"])
        self.radius = int(player["radius"])
        self.color = player["color"]
        self.vel_x = 0
        self.vel_y = 0
        # key pressed statements
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        # speed
        self.speed = int(player["speed"])

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def check_borders(self, size):
        # check x
        if self.x <= self.radius:
            self.x = self.radius + 2
        elif self.x >= size[0] - self.radius:
            self.x = size[0] - (self.radius + 2)
        # check y
        if self.y <= self.radius:
            self.y = self.radius + 2
        elif self.y >= size[1] - self.radius:
            self.y = size[1] - (self.radius + 2)

    def update(self):
        self.vel_x = 0
        self.vel_y = 0

        # update velocity
        if self.left_pressed and not self.right_pressed:
            self.vel_x = -self.speed
        elif self.right_pressed and not self.left_pressed:
            self.vel_x = self.speed
        elif self.up_pressed and not self.down_pressed:
            self.vel_y = -self.speed
        elif self.down_pressed and not self.up_pressed:
            self.vel_y = self.speed

        self.x += int(self.vel_x)
        self.y += int(self.vel_y)
