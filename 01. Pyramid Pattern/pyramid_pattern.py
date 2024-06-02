def pyramid_pattern(n):
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars
        for j in range(2 * i + 1):
            print("*", end="")
        print()

def main():
    n = int(input("Please give me a integer: "))
    pyramid_pattern(n)

if __name__ == '__main__':
    main()