def inverted_right_triangle_pattern(n):
    for i in range(n, 0, -1):
        # Print stars
        for j in range(i):
            print("*", end="")
        print()


def main():
    n = int(input("Please give me a integer: "))
    inverted_right_triangle_pattern(n)

if __name__ == '__main__':
    main()