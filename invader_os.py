import os
from time import sleep
import pygame


class Settings:
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 400
    FPS = 60


def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
    pygame.init()

    screen = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
    pygame.display.set_caption("Bitmaps laden und ausgeben")
    clock = pygame.time.Clock()

    defender = pygame.image.load("images/defender01.png")
    defender = pygame.transform.scale(defender, (50, 50))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")
        screen.blit(defender, (100, 100))

        pygame.display.flip()
        clock.tick(Settings.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()