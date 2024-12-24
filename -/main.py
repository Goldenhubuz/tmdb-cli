import argparse
from typing import Any

from colorama import Fore, Style, init

from enums import Type
from tmdbs import TmdbManager

# Initialize Colorama
init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--type",
    choices=[type.value for type in Type],
    help="The type to perform (add, delete, update, list)",
)
args = parser.parse_args()

tmdb_manager: TmdbManager = TmdbManager()

def main() -> str | list[Any] | tuple[str, dict]:
    if args.type == Type.PLAYING:
        tmdb = tmdb_manager.show_playing()
        return f"{Fore.GREEN}Tmdb successfully{Style.RESET_ALL}"
    elif args.type == Type.POPULAR:
        pass
    elif args.type == Type.TOP:
        pass
    elif args.type == Type.UPCOMING:
        pass
    else:
        pass


if __name__ == "__main__":
    print(main())
