import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, X, Y = map(int, rl().split())
    obstacle = set()
    for _ in range(N):
        x, y = map(int, rl().split())
        x, y = x + 205, y + 205
        obstacle.add((x, y))
    
    H, W = 411, 411
    INF = 10 ** 18
    grid = [[INF] * W for _ in range(H)]
    grid[205][205] = 0
    que = deque([(205, 205)])
    
    while que:
        cy, cx = que.popleft()
        for dy, dx in ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 0)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < H and 0 <= nx < W:
                if (nx, ny) in obstacle:
                    continue
                ncost = grid[cy][cx] + 1
                if ncost < grid[ny][nx]:
                    grid[ny][nx] = ncost
                    que.append((ny, nx))
    print(grid[205 + Y][205 + X] if grid[205 + Y][205 + X] != INF else -1)


if __name__ == '__main__':
    solve()
