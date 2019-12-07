"""Player"""
import characters

class Player(characters.Character):
    """Player"""
    _SHEET_PATH = r"res\elsa.png"
    _IMAGE_SIZE = (48, 48)
    _IMAGES = {"down": 3, "left": 3, "right": 3, "up": 3}
    _COLORKEY = (255, 255, 255)

    velocity = 0.2

    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False

    def __init__(self, name):
        super().__init__(name)
        self.load_images(self._SHEET_PATH, self._IMAGES, self._IMAGE_SIZE, self._COLORKEY)
        self.set_image("left", 1)
        self.position_x = 100
        self.position_y = 50
        self.image_time_limit = 60

    def move_left(self):
        self.moving_left = True
    def move_right(self):
        self.moving_right = True
    def move_up(self):
        self.moving_up = True
    def move_down(self):
        self.moving_down = True

    def stop_left(self):
        self.moving_left = False
    def stop_right(self):
        self.moving_right = False
    def stop_up(self):
        self.moving_up = False
    def stop_down(self):
        self.moving_down = False

    def update_position(self, frame_time):
        """Move player character"""
        if self.moving_up:
            if self.moving_left or self.moving_right:
                self.position_y -= (self.velocity * frame_time * 0.707)
            else:
                self.position_y -= (self.velocity * frame_time)
        if self.moving_down:
            if self.moving_left or self.moving_right:
                self.position_y += (self.velocity * frame_time * 0.707)
            else:
                self.position_y += (self.velocity * frame_time)
        if self.moving_left:
            if self.moving_up or self.moving_down:
                self.position_x -= (self.velocity * frame_time * 0.707)
            else:
                self.position_x -= (self.velocity * frame_time)
        if self.moving_right:
            if self.moving_up or self.moving_down:
                self.position_x += (self.velocity * frame_time * 0.707)
            else:
                self.position_x += (self.velocity * frame_time)

    def update(self, frame_time):
        """update"""
        if self.moving_left:
            self.update_image("left", frame_time)
        elif self.moving_right:
            self.update_image("right", frame_time)
        elif self.moving_up:
            self.update_image("up", frame_time)
        elif self.moving_down:
            self.update_image("down", frame_time)

        self.update_position(frame_time)

