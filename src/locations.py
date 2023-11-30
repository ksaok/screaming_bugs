import random

from settings import CONFIG


class Location:
    def __init__(self, name: str, color: str, x: int, y: int):
        self.name = name
        # self.color = CONFIG.LOCATION_COLOR
        self.color = color
        # self.x = random.randint(0, CONFIG.SCREEN_WIDTH)
        # self.y = random.randint(0, CONFIG.SCREEN_HEIGHT)
        self.x = x
        self.y = y
        self.radius = CONFIG.LOCATION_RADIUS

    @property
    def coordinates(self):
        return self.x, self.y