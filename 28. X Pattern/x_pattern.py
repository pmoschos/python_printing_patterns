def x_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def main():
    n = int(input("Please give me a integer: "))
    x_pattern(n)

if __name__ == '__main__':
    main()