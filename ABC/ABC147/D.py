import numpy as np


def solve():
    MOD = 10**9+7
    N = int(input())
    a = np.array(input().split(), int)

    ans = 0
    for i in range(60):
        ones = np.count_nonzero((a >> i) & 1)
        zeros = N - ones
        ans += zeros * ones * 2 ** i
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    solve()