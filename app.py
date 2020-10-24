import pygame
import json
from src.player import Player

pygame.init()
def load_configuration():
    with open("CONFIG.json") as f:
        return json.load(f)

def main():
    # constants
    WIDTH, HEIGHT = 600, 600
    SIZE = (WIDTH, HEIGHT)
    CLOCK = pygame.time.Clock()
    MAX_FPS = 120
    # load the configuration of the app
    CONFIGURATION = load_configuration()

    # screen configuration
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(CONFIGURATION['general']['title'])
    # sprites
    player = Player(CONFIGURATION["player"])

    # game loop of the app
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_w, pygame.K_UP]:
                    player.up_pressed = True
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    player.down_pressed = True
                elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                    player.right_pressed = True
                elif event.key in [pygame.K_a, pygame.K_LEFT]:
                    player.left_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_UP]:
                    player.up_pressed = False
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    player.down_pressed = False
                elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                    player.right_pressed = False
                elif event.key in [pygame.K_a, pygame.K_LEFT]:
                    player.left_pressed = False
        # update
        screen.fill(CONFIGURATION['general']['color'])
        player.draw(screen)
        player.check_borders(SIZE)
        player.update()
        pygame.display.flip()
        CLOCK.tick(MAX_FPS)

if __name__ == '__main__':
    main()
