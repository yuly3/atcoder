import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    A = tuple(tuple(map(int, rl().split())) for _ in range(H))
    
    INF = 10 ** 18
    dist_max = H * W
    costs = [[[INF] * dist_max for _ in range(W)] for _ in range(H)]
    que = [(0, 0, 0, 0)]
    while que:
        cost, dist, cy, cx = heappop(que)
        if cy == H - 1 and cx == W - 1:
            print(cost)
            return
        if costs[cy][cx][dist] < cost:
            continue
        if dist == dist_max - 1:
            continue
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < H and 0 <= nx < W:
                ncost = cost + (dist * 2 + 1) * A[ny][nx]
                if costs[ny][nx][dist + 1] <= ncost:
                    continue
                costs[ny][nx][dist + 1] = ncost
                heappush(que, (ncost, dist + 1, ny, nx))


if __name__ == '__main__':
    solve()
