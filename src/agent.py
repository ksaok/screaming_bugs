import random
import math

from locations import Location
from settings import CONFIG


class Agent:
    def __init__(self, target: Location, source: Location) -> None:
        # self.color = CONFIG.AGENT_COLOR
        self.size = CONFIG.AGENT_SIZE

        self.angle = random.uniform(0, 2 * math.pi)
        # self.speed = random.randint(2, CONFIG.MAX_AGENT_SPEED)
        self.speed = CONFIG.MAX_AGENT_SPEED

        self.x = random.randint(0, CONFIG.SCREEN_WIDTH)
        self.y = random.randint(0, CONFIG.SCREEN_HEIGHT)

        self.target: Location = target
        self.source: Location = source

        self.color = self.target.color

        self.steps_to_target = 10000
        self.steps_to_source = 10000

        self.alive = True

    def _randomize_angle(self) -> None:
        # if random.choice([True, False]):
        self.angle += random.uniform(-CONFIG.RANDOM_ANGEL_DEVIATION, CONFIG.RANDOM_ANGEL_DEVIATION)

    def _die(self) -> None:
        self.alive = False
        self.color = 'Grey'

    def move(self) -> None:
        # self._randomize_angle()
        self.x += int(math.cos(self.angle) * self.speed)
        self.y += int(math.sin(self.angle) * self.speed)

        if self.x < 0 or self.x > CONFIG.SCREEN_WIDTH or self.y < 0 or self.y > CONFIG.SCREEN_HEIGHT:
            self.angle += math.pi
            # self._die()

        self.steps_to_target += 1
        self.steps_to_source += 1

    def can_hear(self, other) -> bool:
        if id(self) == id(other):
            return False
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2) <= CONFIG.SCREAM_RADIUS

    def scream(self):
        if random.choice([True, False]):
            return self.target.name, self.steps_to_target + CONFIG.SCREAM_RADIUS, self.x, self.y
        else:
            return self.source.name, self.steps_to_source + CONFIG.SCREAM_RADIUS, self.x, self.y

    def hear(self, location_name, steps, screamer_x, screamer_y):
        if location_name == self.target.name and steps < self.steps_to_target:
            self.steps_to_target = steps
            self.angle = math.atan2(screamer_y - self.y, screamer_x - self.x)
        elif location_name == self.source.name and steps < self.steps_to_source:
            self.steps_to_source = steps

    def touch_location(self):
        if math.sqrt((self.x - self.target.x) ** 2 + (self.y - self.target.y) ** 2) <= self.target.radius:
            self.steps_to_target = 0
            self.angle += math.pi
            self.target, self.source = self.source, self.target
            self.steps_to_target, self.steps_to_source = self.steps_to_source, self.steps_to_target
            self.color = self.target.color
        elif math.sqrt((self.x - self.source.x) ** 2 + (self.y - self.source.y) ** 2) <= self.source.radius:
            self.steps_to_source = 0
            # self.angle += math.pi

    @property
    def coordinates(self):
        return self.x, self.y
