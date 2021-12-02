def main():
    numbers = []
    prev = None
    increases = 0

    with open("input", "r") as f:
        numbers = [int(number) for number in f.readlines()]

    for i in range(len(numbers)):
        if prev == None: 
            pass
        elif numbers[i] > prev:
            increases += 1
        prev = numbers[i]

    print(increases)



if __name__ == "__main__":
    main()