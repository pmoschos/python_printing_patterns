def pascal_triangle(n):
    for i in range(n):
        # Print leading spaces
        for j in range(n - i + 1):
            print(" ", end="")
        # Calculate and print binomial coefficients
        c = 1
        for j in range(1, i + 1):
            print(c, end=" ")
            c = c * (i - j) // j
        print()

def main():
    n = int(input("Please give me a integer: "))
    pascal_triangle(n)

if __name__ == '__main__':
    main()