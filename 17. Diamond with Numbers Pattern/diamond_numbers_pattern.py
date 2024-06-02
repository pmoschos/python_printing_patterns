def diamond_with_numbers_pattern(n):
    # Upper part
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
        # Print decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()
    # Lower part
    for i in range(n - 1, 0, -1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
        # Print decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()


def main():
    n = int(input("Please give me a integer: "))
    diamond_with_numbers_pattern(n)

if __name__ == '__main__':
    main()