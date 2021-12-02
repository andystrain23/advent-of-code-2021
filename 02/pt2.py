def main():
    instructions = []
    with open("input", "r") as f:
        instructions = [string.strip('\n') for string in f.readlines()]

    position, depth, aim = 0, 0, 0

    for instruction in instructions:
        move, val = instruction.split()
        val = int(val)

        if move == 'forward':
            position += val
            depth += (aim * val)
        if move == 'up':
            aim -= val
        if move == 'down':
            aim += val

    print(f"Position: {position}, Depth: {depth}")
    print(f"Multiplied = {position * depth}")

    

if __name__ == "__main__":
    main()