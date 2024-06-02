def binary_number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j % 2, end=" ")
        print()


def main():
    n = int(input("Please give me a integer: "))
    binary_number_triangle(n)

if __name__ == '__main__':
    main()