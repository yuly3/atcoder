import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    A = [list(map(int, rl().split())) for _ in range(H)]
    INF = 10 ** 18
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    
    def bfs(sy, sx):
        res = [[INF] * W for _ in range(H)]
        res[sy][sx] = 0
        que = deque([[sy, sx]])
        while que:
            cy, cx = que.popleft()
            for k in range(4):
                ny, nx = cy + dy[k], cx + dx[k]
                if 0 <= ny < H and 0 <= nx < W:
                    w = res[cy][cx] + A[ny][nx]
                    if w < res[ny][nx]:
                        res[ny][nx] = w
                        que.append([ny, nx])
        return res
    
    cost1 = bfs(H - 1, 0)
    cost2 = bfs(H - 1, W - 1)
    cost3 = bfs(0, W - 1)
    
    ans = INF
    for i in range(H):
        for j in range(W):
            ans = min(ans, cost1[i][j] + cost2[i][j] + cost3[i][j] - 2 * A[i][j])
    print(ans)


if __name__ == '__main__':
    solve()
