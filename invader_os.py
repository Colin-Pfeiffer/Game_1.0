import os
from time import sleep
import pygame


class Settings:
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 400
    FPS = 60
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(FILE_PATH, "images")


def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
    pygame.init()

    screen = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
    pygame.display.set_caption("Bitmaps laden und ausgeben")
    clock = pygame.time.Clock()

    defender = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "defender01.png")).convert_alpha()
    defender = pygame.transform.scale(defender, (50, 50))

    alien = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "alienbig0101.png")).convert_alpha()
    alien = pygame.transform.scale(alien, (110, 50))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")
        screen.blit(defender, (100, 100))
        screen.blit(alien, (400, 100))

        pygame.display.flip()
        clock.tick(Settings.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()