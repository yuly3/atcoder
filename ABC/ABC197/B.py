import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W, X, Y = map(int, rl().split())
    S = [rl().rstrip() for _ in range(H)]
    Y, X = X - 1, Y - 1
    
    ans = 1
    for cy in range(Y - 1, -1, -1):
        if S[cy][X] == '.':
            ans += 1
        else:
            break
    for cx in range(X + 1, W):
        if S[Y][cx] == '.':
            ans += 1
        else:
            break
    for cy in range(Y + 1, H):
        if S[cy][X] == '.':
            ans += 1
        else:
            break
    for cx in range(X - 1, -1, -1):
        if S[Y][cx] == '.':
            ans += 1
        else:
            break
    print(ans)


if __name__ == '__main__':
    solve()
