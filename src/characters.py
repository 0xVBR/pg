"""Characters"""
import pygame
from sprites import Spritesheet

class Characters(pygame.sprite.Group):
    """Characters"""

class Character(pygame.sprite.Sprite):
    """Character"""
    name = ""
    image = None
    images = {}
    image_id = 0
    image_key = None
    image_time = 0
    image_time_limit = 0
    rect = None
    state = None
    position_x = 0.0
    position_y = 0.0

    def __init__(self, name):
        super().__init__()
        self.name = name

    def load_images(self, sheet_path, images, image_size, colorkey=None):
        """Load all images from the spritesheet"""
        sheet = Spritesheet(sheet_path)
        self.images = sheet.get_images(images, image_size, colorkey)

    def set_image(self, image_key, image_id):
        """Set the current image"""
        self.image = self.images[image_key][image_id]
        self.rect = self.image.get_rect()
        self.image_key = image_key
        self.image_id = image_id

    def update_image(self, image_key, frame_time):
        """Update the current image based on frame time"""
        if self.image_key == image_key:
            self.image_time += frame_time
            if self.image_time >= self.image_time_limit:
                self.image_id += 1
                self.image_id = self.image_id % len(self.images[image_key])
                self.image_time = 0
        else:
            self.image_key = image_key
            self.image_id = 0
            self.image_time = 0

        self.set_image(self.image_key, self.image_id)

    def clear(self, surface, background):
        """Clear the character from the surface"""
        surface.blit(background.image, self.rect, self.rect)

    def draw(self, surface):
        """Draw the character to the surface"""
        self.rect.x = int(self.position_x)
        self.rect.y = int(self.position_y)
        surface.blit(self.image, self.rect)
