import datetime

import pygame

from locations import Location
from settings import CONFIG

from agent import Agent

# Определение размеров окна
WIDTH = 1600
HEIGHT = 1000
AGENT_SIZE = 5


pygame.init()
screen = pygame.display.set_mode((CONFIG.SCREEN_WIDTH, CONFIG.SCREEN_HEIGHT))
pygame.display.set_caption("Screaming Bugs")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

location_a = Location("A", color='Red', x=410, y=500)
location_b = Location("B", color='Green', x=1190, y=500)
agents = [Agent(target=location_a, source=location_b) for _ in range(CONFIG.AGENTS_COUNT)]

running = True
while running:

    # Очистка экрана
    screen.fill('Black')

    # Движение и отрисовка агентов
    start = datetime.datetime.now().timestamp()
    for agent in agents:
        # agent.move()
        # agent.touch_location()
        for near_agent in agents:
            pass
        #     if near_agent.can_hear(agent) and id(near_agent) != id(agent):
        #         near_agent.hear(*agent.scream())
    print(f"calculation: {datetime.datetime.now().timestamp() - start}")
    for agent in agents:
        pygame.draw.circle(screen, agent.color, agent.coordinates, agent.size)

    # Отрисовка локаций
    pygame.draw.circle(screen, location_a.color, location_a.coordinates, location_a.radius)
    pygame.draw.circle(screen, location_b.color, location_b.coordinates, location_b.radius)

    # Обновление экрана
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_q, pygame.K_ESCAPE):
                running = False
                pygame.quit()
