def heart_pattern(n):
    for i in range(n//2, n, 2):
        # Print leading spaces
        for j in range(1, n - i, 2):
            print(" ", end="")
        # Print stars
        for j in range(1, i + 1):
            print("*", end="")
        # Print middle spaces
        for j in range(1, n - i + 1):
            print(" ", end="")
        # Print stars
        for j in range(1, i + 1):
            print("*", end="")
        print()
    for i in range(n, 0, -1):
        # Print leading spaces
        for j in range(i, n):
            print(" ", end="")
        # Print stars
        for j in range(1, i * 2):
            print("*", end="")
        print()


def main():
    n = int(input("Please give me a integer: "))
    heart_pattern(n)

if __name__ == '__main__':
    main()