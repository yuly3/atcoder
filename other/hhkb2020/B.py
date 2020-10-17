import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    S = [rl().rstrip() for _ in range(H)]
    
    ans = 0
    for i in range(H):
        for j in range(W - 1):
            ans += S[i][j] == '.' and S[i][j + 1] == '.'
    for i in range(H - 1):
        for j in range(W):
            ans += S[i][j] == '.' and S[i + 1][j] == '.'
    print(ans)


if __name__ == '__main__':
    solve()
