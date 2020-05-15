import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    R, G, B, N = map(int, rl().split())
    
    ans = 0
    for r in range(0, N + 1, R):
        for g in range(0, N + 1, G):
            if N < r + g:
                break
            if (N - r - g) % B == 0:
                ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
