_DEFAULT_ROW = "............................................................................................................................................"
_LEN_OF_ROW = 140

#TODO not the nicest solution

def get_sum_of_part_numbers(schematic: list) -> int:
    s = 0
    rows = dict(enumerate(schematic))
    for row_index, row in rows.items():
        column_index = 0
        while column_index < len(row):
            number, column_index = _get_complete_number_from_str(
                row=row,
                index=column_index
            )
            if number:
                s = s + _get_part_value(values=_get_adjacent_substrings(
                    rows=rows,
                    row_index=row_index,
                    column_index=column_index,
                    number=number
                ))
            else:
                column_index = column_index + 1
    return s


def _get_complete_number_from_str(
    row: str,
    index: int,
    number: str = ""
) -> tuple:
    if index < len(row) and row[index].isdigit():
        next_number, index = _get_complete_number_from_str(
            row=row,
            index=index+1,
            number=row[index]
        )
        number = number + next_number
    return number, index


def _get_adjacent_substrings(
    rows: dict,
    row_index: int,
    column_index: int,
    number: str
) -> list:
    end_index = column_index + 1
    start_index = end_index - len(number) - 2
    if start_index < 0:
        start_index = 0
    if end_index > _LEN_OF_ROW:
        end_index = _LEN_OF_ROW
    values = [
        rows.get(row_index-1, _DEFAULT_ROW)[start_index:end_index],
        rows[row_index][start_index:end_index],
        rows.get(row_index+1, _DEFAULT_ROW)[start_index:end_index],
    ]
    if start_index == 0 and values[1][0] != '.':
        values[0] = '.' + values[0]
        values[1] = '.' + values[1]
        values[2] = '.' + values[2]
    if end_index == _LEN_OF_ROW and values[1][-1] != '.':
        values[0] = values[0] + '.'
        values[1] = values[1] + '.'
        values[2] = values[2] + '.'
    return values


def _get_part_value(
    values: list,
):
    adjacent_values = values[0]
    adjacent_values = adjacent_values + values[2]
    adjacent_values = adjacent_values + values[1][0] + values[1][-1]
    if any(v for v in adjacent_values if v != '.'):
        return int(values[1][1:len(values[1])-1])
    return 0
    

