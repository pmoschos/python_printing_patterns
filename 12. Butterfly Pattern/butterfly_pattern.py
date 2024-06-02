def butterfly_pattern(n):
    # Upper part
    for i in range(1, n + 1):
        # Print stars on the left wing
        for j in range(i):
            print("*", end="")
        # Print spaces between wings
        for j in range(2 * (n - i)):
            print(" ", end="")
        # Print stars on the right wing
        for j in range(i):
            print("*", end="")
        print()
    # Lower part
    for i in range(n, 0, -1):
        # Print stars on the left wing
        for j in range(i):
            print("*", end="")
        # Print spaces between wings
        for j in range(2 * (n - i)):
            print(" ", end="")
        # Print stars on the right wing
        for j in range(i):
            print("*", end="")
        print()


def main():
    n = int(input("Please give me a integer: "))
    butterfly_pattern(n)

if __name__ == '__main__':
    main()