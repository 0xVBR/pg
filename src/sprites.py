"""Sprites"""
import pygame

class Spritesheet():
    """Spritesheet"""
    sheet = None

    def __init__(self, image_path):
        self.sheet = pygame.image.load(image_path).convert()

    def get_image(self, rect, colorkey=None):
        """returns one image from the spritesheet"""
        rect = pygame.Rect(rect)
        image = pygame.Surface(rect.size).convert()

        if colorkey is not None:
            image.fill(colorkey)
            image.set_colorkey(colorkey)

        image.blit(self.sheet, (0, 0), rect)
        return image

    def get_image_set(self, rect, count, colorkey=None):
        """returns one image set (row) from the spritesheet"""
        images = []
        rect = pygame.Rect(rect)

        for _ in range(0, count):
            image = self.get_image(rect, colorkey)
            images.append(image)
            rect.x += rect.width
        return images

    def get_images(self, images_dict, image_size, colorkey=None):
        """returns all image sets (rows) from the spritesheet"""
        images = {}
        rect = pygame.Rect((0, 0), image_size)

        for key in images_dict:
            images[key] = self.get_image_set(rect, images_dict[key], colorkey)
            rect.y += rect.height
        return images
