"""Background"""
import random
import pygame

class Background(pygame.sprite.Group):
    """Background image"""
    image = None

    _IMAGE_PATH = r"res\background.png"
    _BOX_PATH = r"res\box.png"

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(self._IMAGE_PATH).convert()

        box_count = random.randint(0, 4)
        for i in range(box_count):
            box = BackgroundObject(self._BOX_PATH, True)
            box.rect.x = i * 100
            box.rect.y = i * 70
            super().add(box)

    def draw(self, window):
        """Draws the background image to the window screen"""
        super().draw(self.image)
        window.blit(self.image, (0, 0))

class BackgroundObject(pygame.sprite.Sprite):
    """Background Object as sprite"""
    solid = False

    def __init__(self, image_path, solid):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.solid = solid
