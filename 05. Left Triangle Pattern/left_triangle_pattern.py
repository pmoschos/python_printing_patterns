def left_triangle_pattern(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print stars
        for j in range(i):
            print("*", end="")
        print()


def main():
    n = int(input("Please give me a integer: "))
    left_triangle_pattern(n)

if __name__ == '__main__':
    main()