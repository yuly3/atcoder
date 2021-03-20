import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    a, b = map(int, rl().split())
    c, d = map(int, rl().split())
    
    ans = -1000
    for x in range(a, b + 1):
        for y in range(c, d + 1):
            ans = max(ans, x - y)
    print(ans)


if __name__ == '__main__':
    solve()
