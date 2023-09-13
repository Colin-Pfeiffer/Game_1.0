import os
from random import randint
from typing import Any
from time import sleep
import pygame


class Settings:
    WINDOW = pygame.rect.Rect(0, 0, 600, 400)
    FPS = 60
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(FILE_PATH, "images")
    NUM_ALIENS = 20

class Defender(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "defender01.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.WINDOW.centerx
        self.rect.bottom = Settings.WINDOW.bottom - 10
        self.speedx = 2
        self.speedy = 0

    def update(self):
        self.rect.move_ip(self.speedx, self.speedy)
        if self.rect.right > Settings.WINDOW.right or self.rect.left <= 0:
            self.speedx *= -1

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "alienbig0101.png")).convert()
        self.image.set_colorkey("black")
        self.image = pygame.transform.scale(self.image, (50, 45))
        self.rect = self.image.get_rect()
        self.rect.left = 10
        self.rect.top = 10
        self.speedx = randint(1, 5)
        self.speedy = randint(1, 5)

    def update(self) -> None:
        self.rect.move_ip(self.speedx, self.speedy)
        if self.rect.right > Settings.WINDOW.right or self.rect.left <= 0:
            self.speedx *= -1
        if self.rect.bottom > Settings.WINDOW.bottom or self.rect.top <= 0:
            self.speedy *= -1

class Game:
    def __init__(self) -> None:
        os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
        pygame.init()

        self.screen = pygame.display.set_mode((Settings.WINDOW.size))
        pygame.display.set_caption("Bitmaps laden und ausgeben")
        self.clock = pygame.time.Clock()


        self.all_mobs = pygame.sprite.Group()
        self.all_mobs.add(Defender())
        for _ in range(Settings.NUM_ALIENS):
            self.all_mobs.add(Alien())

        self.background_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "sunset.png")).convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, Settings.WINDOW.size)

        self.running = True

    def run(self) -> None:
        while self.running:
            self.watch_for_events()
            self.update()
            self.draw()
            self.clock.tick(Settings.FPS)

    def update(self) -> None:
        self.all_mobs.update()

    def draw(self) -> None:
        self.screen.blit(self.background_image, (0, 0))
        self.all_mobs.draw(self.screen)
        pygame.display.flip()

    def watch_for_events(self) -> None:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

def main():
    game = Game()
    game.run()
    

    pygame.quit()




if __name__ == "__main__":
    main()