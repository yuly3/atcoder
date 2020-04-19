import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    MOD = 10 ** 9 + 7
    
    acc = [0] * (N + 1)
    for i in range(1, N + 1):
        acc[i] = (acc[i - 1] + i) % MOD
    
    ans = 1
    for i in range(K, N + 1):
        ans = (ans + acc[N] - acc[N - i] - acc[i - 1] + 1) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
