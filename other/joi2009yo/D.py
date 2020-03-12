import sys
sys.setrecursionlimit(10 ** 7)

m = int(input())
n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]


def dfs(y, x, maze_tmp):
    res = 0
    maze_tmp[y][x] = 0
    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m:
            if maze_tmp[ny][nx] == 1:
                res = max(res, dfs(ny, nx, maze_tmp))
    maze_tmp[y][x] = 1
    return res + 1


def solve():
    ans = 0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                ans = max(ans, dfs(i, j, maze))
    print(ans)


if __name__ == '__main__':
    solve()
