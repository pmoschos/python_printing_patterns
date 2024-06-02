def hollow_diamond_pattern(n):
    # Upper part
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    # Lower part
    for i in range(n - 2, -1, -1):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def main():
    n = int(input("Please give me a integer: "))
    hollow_diamond_pattern(n)

if __name__ == '__main__':
    main()