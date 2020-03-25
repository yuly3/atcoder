def solve():
    N, M = map(int, input().split())
    MOD = 10 ** 9 + 7
    
    if N == M:
        ans = 1
        for i in range(2, N + 1):
            ans = ans * i % MOD
        ans = (ans ** 2 % MOD) * 2 % MOD
        print(ans)
    elif 1 < abs(N - M):
        print(0)
    else:
        ans = 1
        for i in range(2, N + 1):
            ans = ans * i % MOD
        for i in range(2, M + 1):
            ans = ans * i % MOD
        print(ans)


if __name__ == '__main__':
    solve()
