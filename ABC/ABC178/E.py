import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    xy = [list(map(int, rl().split())) for _ in range(N)]
    
    a = [xi + yi for xi, yi in xy]
    a.sort()
    b = [xi - yi for xi, yi in xy]
    b.sort()
    ans = max(a[-1] - a[0], b[-1] - b[0])
    print(ans)


if __name__ == '__main__':
    solve()
