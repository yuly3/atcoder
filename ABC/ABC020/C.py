import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W, T = map(int, rl().split())
    maze = [input() for _ in range(H)]
    sy, sx, gy, gx = 0, 0, 0, 0
    for i in range(H):
        idx = maze[i].find('S')
        if idx != -1:
            sy, sx = i, idx
        idx = maze[i].find('G')
        if idx != -1:
            gy, gx = i, idx
    
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    INF = 10 ** 18
    
    def check(t):
        cost = [[INF] * W for _ in range(H)]
        cost[sy][sx] = 0
        que = deque([[sy, sx]])
        while que:
            cy, cx = que.popleft()
            for k in range(4):
                ny, nx = cy + dy[k], cx + dx[k]
                if 0 <= ny < H and 0 <= nx < W:
                    n_cost = cost[cy][cx]
                    if maze[ny][nx] == '.' or maze[ny][nx] == 'G':
                        n_cost += 1
                    else:
                        n_cost += t
                    if n_cost < cost[ny][nx]:
                        cost[ny][nx] = n_cost
                        que.append([ny, nx])
        return cost[gy][gx] <= T
    
    ok, ng = 1, INF
    while 1 < ng - ok:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    solve()
