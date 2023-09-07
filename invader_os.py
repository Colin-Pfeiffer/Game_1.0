import os
from time import sleep
import pygame


class Settings:
    WINDOW = pygame.rect.Rect(0, 0, 600, 400)
    FPS = 60
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(FILE_PATH, "images")

class Defender(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "defender01.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.WINDOW.centerx
        self.rect.bottom = Settings.WINDOW.bottom
        self.speed_x = 10
        self.speed_y = 0

    def update(self):
        self.rect.move_ip(self.speed_x, self.speed_y)
        if self.rect.right > Settings.WINDOW.right or self.rect.left <= 0:
            self.speed_x *= -1

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "alienbig0101.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.WINDOW.centerx
        self.rect.top = Settings.WINDOW.top
        self.speed_x = 10
        self.speed_y = 0

    def update(self):
        self.rect.move_ip(self.speed_x, self.speed_y)
        if self.rect.right > Settings.WINDOW.right or self.rect.left <= 0:
            self.speed_x *= -1
            self.rect.move_ip(0, self.rect.height)
            

def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
    pygame.init()

    screen = pygame.display.set_mode((Settings.WINDOW.size))
    pygame.display.set_caption("Bitmaps laden und ausgeben")
    clock = pygame.time.Clock()

    background_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "sunset.png")).convert_alpha()
    background_image = pygame.transform.scale(background_image, Settings.WINDOW.size)

    defender = Defender()

    alien = Alien()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        defender.update()        
        alien.update()

        screen.blit(background_image, (0, 0))
        screen.blit(defender.image, defender.rect)
        screen.blit(alien.image, alien.rect)

        pygame.display.flip()
        clock.tick(Settings.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()