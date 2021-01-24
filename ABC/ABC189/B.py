import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, X = map(int, rl().split())
    
    X *= 100
    s = 0
    for i in range(N):
        v, p = map(int, rl().split())
        s += v * p
        if X < s:
            print(i + 1)
            return
    print(-1)


if __name__ == '__main__':
    solve()
