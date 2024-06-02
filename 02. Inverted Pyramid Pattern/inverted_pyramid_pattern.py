def inverted_pyramid_pattern(n):
    for i in range(n, 0, -1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print stars
        for j in range(2 * i - 1):
            print("*", end="")
        print()


def main():
    n = int(input("Please give me a integer: "))
    inverted_pyramid_pattern(n)

if __name__ == '__main__':
    main()