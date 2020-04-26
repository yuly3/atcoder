import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, A, B = map(int, rl().split())
    X = list(map(int, rl().split()))
    
    ans = 0
    for i in range(N - 1):
        ans += min((X[i + 1] - X[i]) * A, B)
    print(ans)


if __name__ == '__main__':
    solve()
