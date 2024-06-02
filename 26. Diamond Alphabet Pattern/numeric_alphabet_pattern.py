def diamond_alphabet_pattern(n):
    alphabet = 65
    # Upper part
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print(chr(alphabet + j), end="")
        print()
    # Lower part
    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print(chr(alphabet + j), end="")
        print()

def main():
    n = int(input("Please give me a integer: "))
    diamond_alphabet_pattern(n)

if __name__ == '__main__':
    main()