from collections import deque
from copy import deepcopy


def solve():
    H, W = map(int, input().split())
    maze = [[-2 for _ in range(W)] for _ in range(H)]
    s_point = []
    for i in range(H):
        line = input()
        for j in range(W):
            if line[j] == '#':
                maze[i][j] = -1
            else:
                s_point.append((i, j))

    dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    N = len(s_point)
    ans = 0
    for i in range(N):
        ans_tmp = 0
        maze_tmp = deepcopy(maze)
        sy, sx = s_point[i]
        maze_tmp[sy][sx] = 0
        que = deque([[sy, sx]])
        while que:
            cy, cx = que.popleft()
            for j in range(4):
                ny, nx = cy + dyx[j][0], cx + dyx[j][1]
                if 0 <= ny <= H - 1 and 0 <= nx <= W - 1:
                    if maze_tmp[ny][nx] == -2:
                        maze_tmp[ny][nx] = maze_tmp[cy][cx] + 1
                        ans_tmp = max(ans_tmp, maze_tmp[ny][nx])
                        que.append([ny, nx])
        ans = max(ans, ans_tmp)
    print(ans)


if __name__ == '__main__':
    solve()
