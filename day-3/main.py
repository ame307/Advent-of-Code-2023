from pathlib import Path

def get_input():
    with open(f"{Path(__file__).parent.resolve()}/resources/input.txt") as r:
        input = r.readlines()
    return input

def main():
    input = get_input()
    print(input)
 
if __name__ == '__main__':
    main()