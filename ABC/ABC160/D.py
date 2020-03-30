import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, X, Y = map(int, rl().split())
    X -= 1
    Y -= 1
    
    ans = [0] * N
    for i in range(N - 1):
        for j in range(i + 1, N):
            ans[min(j - i, abs(X - i) + 1 + abs(j - Y), abs(Y - i) + 1 + abs(j - X))] += 1
    print('\n'.join(map(str, ans[1:])))


if __name__ == '__main__':
    solve()
