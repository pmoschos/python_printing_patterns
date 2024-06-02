def hollow_diamond_in_rectangle(n):
    for i in range(n):
        for j in range(n):
            if i + j == n // 2 or i - j == n // 2 or j - i == n // 2 or i + j == n // 2 + n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def main():
    n = int(input("Please give me a integer: "))
    hollow_diamond_in_rectangle(n)

if __name__ == '__main__':
    main()