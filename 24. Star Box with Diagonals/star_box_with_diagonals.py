def star_box_with_diagonals(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def main():
    n = int(input("Please give me a integer: "))
    star_box_with_diagonals(n)

if __name__ == '__main__':
    main()