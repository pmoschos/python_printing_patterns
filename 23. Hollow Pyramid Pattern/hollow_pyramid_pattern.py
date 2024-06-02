def hollow_pyramid_pattern(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def main():
    n = int(input("Please give me a integer: "))
    hollow_pyramid_pattern(n)

if __name__ == '__main__':
    main()