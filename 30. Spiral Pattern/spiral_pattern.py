def spiral_pattern(n):
    a = [[0] * n for _ in range(n)]
    val = 1
    k, l = 0, 0
    m, p = n, n
    
    while k < m and l < p:
        for i in range(l, p):
            a[k][i] = val
            val += 1
        k += 1
        for i in range(k, m):
            a[i][p - 1] = val
            val += 1
        p -= 1
        if k < m:
            for i in range(p - 1, l - 1, -1):
                a[m - 1][i] = val
                val += 1
            m -= 1
        if l < p:
            for i in range(m - 1, k - 1, -1):
                a[i][l] = val
                val += 1
            l += 1

    for row in a:
        for num in row:
            print(str(num).rjust(3), end=" ")
        print()


def main():
    n = int(input("Please give me a integer: "))
    spiral_pattern(n)

if __name__ == '__main__':
    main()