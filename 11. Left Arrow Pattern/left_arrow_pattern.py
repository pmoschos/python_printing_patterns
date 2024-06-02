def left_arrow_pattern(n):
    # Upper part
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars
        print("*")
    # Lower part
    for i in range(n - 1):
        # Print leading spaces
        for j in range(i + 1):
            print(" ", end="")
        # Print stars
        print("*")

def main():
    n = int(input("Please give me a integer: "))
    left_arrow_pattern(n)

if __name__ == '__main__':
    main()