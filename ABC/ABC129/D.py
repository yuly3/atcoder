def solve():
    H, W = map(int, input().split())
    maze = [[] for _ in range(H)]
    for i in range(H):
        maze[i] = list(input())

    u = [[0 for _ in range(W)] for _ in range(H)]
    r = [[0 for _ in range(W)] for _ in range(H)]
    d = [[0 for _ in range(W)] for _ in range(H)]
    l = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if maze[i][j] == '#':
                continue
            if i == 0:
                u[i][j] = 1
            else:
                u[i][j] = u[i-1][j] + 1
            if j == 0:
                l[i][j] = 1
            else:
                l[i][j] = l[i][j-1] + 1
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if maze[i][j] == '#':
                continue
            if i == H - 1:
                d[i][j] = 1
            else:
                d[i][j] = d[i+1][j] + 1
            if j == W - 1:
                r[i][j] = 1
            else:
                r[i][j] = r[i][j+1] + 1

    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, u[i][j] + r[i][j] + d[i][j] + l[i][j] - 3)
    print(ans)


if __name__ == '__main__':
    solve()
