from color import Color

POSSIBLE_VALUES_BY_COLOR = {
    Color.RED: 12,
    Color.GREEN: 13,
    Color.BLUE: 14,
}

class Record():
    def __init__(
        self,
        count: int,
        color: Color
    ) -> None:
        self.__count = int(count)
        self.__color = color

    @property
    def count(self) -> int:
        return self.__count
    
    @property
    def color(self) -> Color:
        return self.__color
    
    def is_valid(self) -> bool:
        return self.count <= POSSIBLE_VALUES_BY_COLOR[self.color]