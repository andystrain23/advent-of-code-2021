def main():
    tests = [607, 618, 618, 617, 647, 716, 769, 792]
    numbers = []
    with open("input", "r") as f:
        numbers = [int(number) for number in f.readlines()]

    increases = 0
    for i in range(3, len(numbers)):
        if numbers[i] > numbers[i-3]:
            increases += 1

    print(increases)


if __name__ == "__main__":
    main()