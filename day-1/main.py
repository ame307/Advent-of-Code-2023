from pathlib import Path

def get_input():
    with open(f"{Path(__file__).parent.resolve()}/resources/input.txt") as r:
        input = r.readlines()
    return input

def get_correct_value(str_value):
    first_digit = next(c for c in str_value if c.isdigit())
    last_digit = next(c for c in reversed(str_value) if c.isdigit())
    return int(first_digit+last_digit) 

def main():
    wrong_calibration_values = get_input()
    print(sum([get_correct_value(v) for v in wrong_calibration_values]))

if __name__ == '__main__':
    main()