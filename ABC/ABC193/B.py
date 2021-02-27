import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    APX = [list(map(int, rl().split())) for _ in range(N)]
    
    ans = 10 ** 10
    for ai, pi, xi in APX:
        if 0 < xi - ai:
            ans = min(ans, pi)
    print(ans if ans != 10 ** 10 else -1)


if __name__ == '__main__':
    solve()
