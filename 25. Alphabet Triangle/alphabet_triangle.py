def alphabet_triangle(n):
    alphabet = 65  # ASCII value of 'A'
    for i in range(n):
        for j in range(i + 1):
            print(chr(alphabet + j), end=" ")
        print()


def main():
    n = int(input("Please give me a integer: "))
    alphabet_triangle(n)

if __name__ == '__main__':
    main()