def checkerboard_pattern(n):
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def main():
    n = int(input("Please give me a integer: "))
    checkerboard_pattern(n)

if __name__ == '__main__':
    main()