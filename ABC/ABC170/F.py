import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W, K = map(int, rl().split())
    sy, sx, gy, gx = map(lambda n: int(n) - 1, rl().split())
    c = [rl().rstrip() for _ in range(H)]
    
    INF = 10 ** 10
    cost = [[INF] * W for _ in range(H)]
    cost[sy][sx] = 0
    que = deque([(sy, sx)])
    while que:
        cy, cx = que.popleft()
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            for k in range(1, K + 1):
                ny, nx = cy + k * dy, cx + k * dx
                if 0 <= ny < H and 0 <= nx < W:
                    if c[ny][nx] == '@':
                        break
                    if cost[ny][nx] <= cost[cy][cx]:
                        break
                    ncost = cost[cy][cx] + 1
                    if ncost < cost[ny][nx]:
                        cost[ny][nx] = ncost
                        que.append((ny, nx))
    print(cost[gy][gx] if cost[gy][gx] != INF else -1)


if __name__ == '__main__':
    solve()
