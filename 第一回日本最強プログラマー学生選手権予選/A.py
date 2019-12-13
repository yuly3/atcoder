import sys


def solve():
    M, D = input().split()
    ans = 0

    if int(D) < 22:
        print(0)
        sys.exit()

    m, d_1, d_2 = int(M), int(D[0]), int(D[1])

    if int(M) < 4 or d_1 < 2 and d_2 < 2:
        print(0)
        sys.exit()

    for i in range(4, m+1):
        for j in range(2, d_1+1):
            for k in range(2, 10):
                if j == d_1 and k > d_2:
                    break
                if i == j * k:
                    ans += 1
    print(ans)


if __name__ == '__main__':
    solve()