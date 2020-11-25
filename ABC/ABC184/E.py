import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    maze = [rl().rstrip() for _ in range(H)]
    
    ord_a = ord('a')
    sy, sx = 0, 0
    gy, gx = 0, 0
    telepoter = [[] for _ in range(26)]
    for i in range(H):
        for j in range(W):
            if maze[i][j].islower():
                telepoter[ord(maze[i][j]) - ord_a].append((i, j))
            elif maze[i][j] == 'S':
                sy, sx = i, j
            elif maze[i][j] == 'G':
                gy, gx = i, j
    
    INF = 10 ** 9
    cost = [[INF] * W for _ in range(H)]
    cost[sy][sx] = 0
    cost_alpha = [INF] * 26
    que = deque([(sy, sx, False)])
    while que:
        cy, cx, alpha = que.popleft()
        if alpha:
            ncost = cost_alpha[cx]
            for ny, nx in telepoter[cx]:
                if ncost < cost[ny][nx]:
                    cost[ny][nx] = ncost
                    que.appendleft((ny, nx, False))
            continue
        ncost = cost[cy][cx] + 1
        if maze[cy][cx].islower():
            nx = ord(maze[cy][cx]) - ord_a
            if ncost < cost_alpha[nx]:
                cost_alpha[nx] = ncost
                que.append((0, nx, True))
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < H and 0 <= nx < W and maze[ny][nx] != '#':
                if ncost < cost[ny][nx]:
                    cost[ny][nx] = ncost
                    que.append((ny, nx, False))
    print(cost[gy][gx] if cost[gy][gx] != INF else -1)


if __name__ == '__main__':
    solve()
