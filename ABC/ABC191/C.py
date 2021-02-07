import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    S = [rl().rstrip() for _ in range(H)]
    
    ans = 0
    for i in range(H - 1):
        for j in range(W - 1):
            cnt = 0
            for y, x in ((i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)):
                cnt += S[y][x] == '#'
            ans += cnt == 1 or cnt == 3
    print(ans)


if __name__ == '__main__':
    solve()
