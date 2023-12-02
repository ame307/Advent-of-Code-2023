from color import Color
from record import Record

class Game():
    def __init__(
        self,
        id: int,
        reveals: list
    ) -> None:
        self.__id = int(id)
        self.__reveals = reveals

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def reveals(self) -> int:
        return self.__reveals

    @staticmethod
    def get_games_from_txt(input: list) -> list:
        games = []
        for line in input:
            game_title, reveals = line.split(':')
            reveals = [[Record(record.split(' ')[1], Color(record.split(' ')[2].strip())) for record in reveal.split(',')] for reveal in reveals.split(';')]
            game = Game(
                id=game_title.split(' ')[1],
                reveals=reveals
            )
            games.append(game)
        return games

    def is_possible(self) -> bool:
        return all(all(record.is_valid() for record in reveal) for reveal in self.reveals)