def right_arrow_pattern(n):
    # Upper part
    for i in range(n):
        # Print leading spaces
        for j in range(i):
            print(" ", end="")
        # Print stars
        print("*")
    # Lower part
    for i in range(n - 2, -1, -1):
        # Print leading spaces
        for j in range(i):
            print(" ", end="")
        # Print stars
        print("*")


def main():
    n = int(input("Please give me a integer: "))
    right_arrow_pattern(n)

if __name__ == '__main__':
    main()