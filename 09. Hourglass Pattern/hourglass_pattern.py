def hourglass_pattern(n):
    # Upper part
    for i in range(n, 0, -1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print stars
        for j in range(2 * i - 1):
            print("*", end="")
        print()
    # Lower part
    for i in range(2, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print stars
        for j in range(2 * i - 1):
            print("*", end="")
        print()


def main():
    n = int(input("Please give me a integer: "))
    hourglass_pattern(n)

if __name__ == '__main__':
    main()