import sys
from math import factorial

rl = sys.stdin.readline


def mod_div(x, y, mod=10 ** 9 + 7):
    return x * pow(y, mod - 2, mod) % mod


def solve():
    N = int(rl())
    x = list(map(int, rl().split()))
    MOD = 10 ** 9 + 7
    
    acc = [0] * N
    k = factorial(N - 1)
    for i in range(1, N):
        acc[i] = (acc[i - 1] + k) % MOD
        k = k * mod_div(i, i + 1) % MOD
    
    ans = 0
    for i in range(N - 1):
        ans = (ans + (x[i + 1] - x[i]) * acc[i + 1]) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
