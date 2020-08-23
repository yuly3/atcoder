import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    ch, cw = map(lambda n: int(n) - 1, rl().split())
    dh, dw = map(lambda n: int(n) - 1, rl().split())
    S = [rl().rstrip() for _ in range(H)]
    
    INF = 10 ** 9
    costs = [[INF] * W for _ in range(H)]
    que = deque([(0, ch, cw)])
    while que:
        cost, cy, cx = que.popleft()
        if cy == dh and cx == dw:
            print(cost)
            return
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < H and 0 <= nx < W:
                if S[ny][nx] == '#':
                    continue
                if costs[ny][nx] <= cost:
                    continue
                que.appendleft((cost, ny, nx))
                costs[ny][nx] = cost
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < H and 0 <= nx < W:
                    if S[ny][nx] == '#':
                        continue
                    if costs[ny][nx] <= cost + 1:
                        continue
                    que.append((cost + 1, ny, nx))
                    costs[ny][nx] = cost + 1
    print(-1)


if __name__ == '__main__':
    solve()
