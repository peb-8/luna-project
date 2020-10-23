"""
Luna project entry point
"""
from game import Game


def main():
    """ Main method """
    game = Game()
    game.setup()
    game.run()


if __name__ == "__main__":
    main()
