import pygame
import json

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


    # game loop of the app
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
        # update
        screen.fill(CONFIGURATION['general']['color'])
        pygame.display.flip()
        CLOCK.tick(MAX_FPS)

if __name__ == '__main__':
    main()
