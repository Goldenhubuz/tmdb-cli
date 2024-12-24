from enum import Enum


class Type(str, Enum):
    """Enum for defining supported actions in the task manager."""
    PLAYING: str = "playing"
    POPULAR: str = "popular"
    TOP: str = "top"
    UPCOMING: str = "upcoming"

# if __name__ == "__main__":
#     print(Type.upcoming.upper())  # Output: playing