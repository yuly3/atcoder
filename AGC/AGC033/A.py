import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    grid = [[] for _ in range(H)]
    que = deque()
    for i in range(H):
        grid[i] = list(rl().rstrip())
        for j in range(W):
            if grid[i][j] == '#':
                que.append((i, j))
    
    ans = -1
    while que:
        n = len(que)
        for _ in range(n):
            cy, cx = que.popleft()
            for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if 0 <= nx < W and 0 <= ny < H:
                    if grid[ny][nx] == '.':
                        grid[ny][nx] = '#'
                        que.append((ny, nx))
        ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
