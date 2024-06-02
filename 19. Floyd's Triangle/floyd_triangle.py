def floyd_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()


def main():
    n = int(input("Please give me a integer: "))
    floyd_triangle(n)

if __name__ == '__main__':
    main()