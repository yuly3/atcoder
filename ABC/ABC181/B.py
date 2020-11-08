import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    ans = 0
    for _ in range(N):
        a, b = map(int, rl().split())
        ans += (b - a + 1) * (a + b) // 2
    print(ans)


if __name__ == '__main__':
    solve()
