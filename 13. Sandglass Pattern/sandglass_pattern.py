def sandglass_pattern(n):
    # Upper part
    for i in range(n):
        # Print leading spaces
        for j in range(i):
            print(" ", end="")
        # Print stars
        for j in range(2 * (n - i) - 1):
            print("*", end="")
        print()
    # Lower part
    for i in range(n - 2, -1, -1):
        # Print leading spaces
        for j in range(i):
            print(" ", end="")
        # Print stars
        for j in range(2 * (n - i) - 1):
            print("*", end="")
        print()


def main():
    n = int(input("Please give me a integer: "))
    sandglass_pattern(n)

if __name__ == '__main__':
    main()