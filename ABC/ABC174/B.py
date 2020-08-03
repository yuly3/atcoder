import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, D = map(int, rl().split())
    XY = [list(map(int, rl().split())) for _ in range(N)]
    
    ans = 0
    for x, y in XY:
        if (x ** 2 + y ** 2) ** 0.5 <= D:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
