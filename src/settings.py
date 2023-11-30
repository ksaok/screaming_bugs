from pydantic import BaseSettings


class Settings(BaseSettings):
    AGENT_SIZE: int = 2
    AGENT_COLOR: str = "Red"
    AGENTS_COUNT: int = 1000
    MAX_AGENT_SPEED: float = 3.0
    SCREAM_RADIUS: float = 50.0

    LOCATION_COLOR: str = "Blue"
    LOCATION_RADIUS: int = 10

    SCREEN_WIDTH: int = 1600
    SCREEN_HEIGHT: int = 1000
    RANDOM_ANGEL_DEVIATION: float = 0.05

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


CONFIG = Settings()