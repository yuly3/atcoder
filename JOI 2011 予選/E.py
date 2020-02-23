from collections import deque
from copy import deepcopy


def solve():
    H, W, N = map(int, input().split())
    maze = [[-1] * W for _ in range(H)]
    sy, sx = [0] * N, [0] * N
    gy, gx = [0] * N, [0] * N
    for i in range(H):
        line = list(input())
        for j in range(W):
            if line[j] == '.':
                continue
            elif line[j] == 'X':
                maze[i][j] = -2
            elif line[j] == 'S':
                sy[0], sx[0] = i, j
            else:
                n = int(line[j])
                if n != N:
                    sy[n], sx[n] = i, j
                gy[n - 1], gx[n - 1] = i, j
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    ans = 0
    for i in range(N):
        maze_tmp = deepcopy(maze)
        maze_tmp[sy[i]][sx[i]] = 0
        que = deque([[sy[i], sx[i]]])
        while que:
            cy, cx = que.popleft()
            for j in range(4):
                ny, nx = cy + dy[j], cx + dx[j]
                if 0 <= ny < H and 0 <= nx < W:
                    if ny == gy[i] and nx == gx[i]:
                        ans += maze_tmp[cy][cx] + 1
                        que.clear()
                        break
                    if maze_tmp[ny][nx] == -1:
                        maze_tmp[ny][nx] = maze_tmp[cy][cx] + 1
                        que.append([ny, nx])
    print(ans)


if __name__ == '__main__':
    solve()
