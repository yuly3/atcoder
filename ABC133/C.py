def solve():
    L, R = map(int, input().split())
    MOD = 2019

    if R - L >= MOD:
        print(0)
        exit()

    ans = 2018
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            if ans > (i * j) % MOD:
                ans = (i * j) % MOD
                if ans == 0:
                    print(0)
                    exit()
    print(ans)


if __name__ == '__main__':
    solve()