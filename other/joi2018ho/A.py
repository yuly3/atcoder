import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    T = [int(rl()) for _ in range(N)]
    
    d = []
    for i in range(1, N):
        d.append(T[i] - (T[i - 1] + 1))
    d.sort()
    
    ans = N + sum(d[:N - K])
    print(ans)


if __name__ == '__main__':
    solve()
