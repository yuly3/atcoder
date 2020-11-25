import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, X = map(int, rl().split())
    S = rl().rstrip()
    
    for si in S:
        if si == 'o':
            X += 1
        else:
            X = max(0, X - 1)
    print(X)


if __name__ == '__main__':
    solve()
