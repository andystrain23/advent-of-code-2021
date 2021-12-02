def main():
    instructions = []
    with open("input", "r") as f:
        raw = [string.strip('\n') for string in f.readlines()]

    instructions = [string.split() for string in raw]

    position, depth = 0, 0

    for instruction in instructions:
        if instruction[0] == 'forward':
            position += int(instruction[1])
        if instruction[0] == 'up':
            depth -= int(instruction[1])
        if instruction[0] == 'down':
            depth += int(instruction[1])

    print(f"Position: {position}, Depth: {depth}")
    print(f"Multiplied = {position * depth}")

    

if __name__ == "__main__":
    main()