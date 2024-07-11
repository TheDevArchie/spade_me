from helpers import create_new_players
from src.game import Game


def main():
    names = ['Steve', 'Bob', 'Carl']

    players = create_new_players(names=names)

    new_game = Game(starting_cards_dealt=7, players=players)
    print(new_game._players)


if __name__ == '__main__':
    main()
