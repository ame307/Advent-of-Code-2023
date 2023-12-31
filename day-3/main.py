from pathlib import Path
import schematic_solver

def get_input():
    with open(f"{Path(__file__).parent.resolve()}/resources/input.txt") as r:
        input = r.read().splitlines() 
    return input

def main():
    input = get_input()
    result = schematic_solver.get_sum_of_part_numbers(schematic=input)
    print(result)

if __name__ == '__main__':
    main()