import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, S, D = map(int, rl().split())
    XY = [list(map(int, rl().split())) for _ in range(N)]
    
    for xi, yi in XY:
        if xi < S and D < yi:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    solve()
