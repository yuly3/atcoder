import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    MOD = 10 ** 9 + 7
    
    a = [0]
    for d in range(1, K + 1):
        a.append(pow(K // d, N, MOD))
    
    for i in range(K, 0, -1):
        j = 2 * i
        while j <= K:
            a[i] = (a[i] - a[j]) % MOD
            j += i
    
    ans = 0
    for i in range(1, K + 1):
        ans = (ans + i * a[i]) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
