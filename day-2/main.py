from pathlib import Path
from game import Game

def get_input():
    with open(f"{Path(__file__).parent.resolve()}/resources/input.txt") as r:
        input = r.readlines()
    return input

def main():
    input = get_input()
    games = Game.get_games_from_txt(input)
    sum_of_ids = sum(game.id for game in games if game.is_possible())
    print(sum_of_ids)
 
if __name__ == '__main__':
    main()