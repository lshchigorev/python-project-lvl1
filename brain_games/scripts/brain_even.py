#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.even_game import even_game


def main():
    name = welcome_user()
    even_game()
    print('Goodbye, {}!' .format(name))


if __name__ == 'main':
    main()
