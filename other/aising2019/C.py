import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    S = [rl().rstrip() for _ in range(H)]
    
    roots = []
    searched = [[False] * W for _ in range(H)]
    counter = defaultdict(int)
    for i in range(H):
        for j in range(W):
            if searched[i][j]:
                continue
            roots.append((i, j))
            searched[i][j] = True
            sij = S[i][j]
            counter[(i, j, sij == '.')] += 1
            que = deque([(i, j, sij)])
            while que:
                cy, cx, cc = que.popleft()
                for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < H and 0 <= nx < W:
                        if searched[ny][nx]:
                            continue
                        nc = S[ny][nx]
                        if cc == nc:
                            continue
                        searched[ny][nx] = True
                        counter[(i, j, nc == '.')] += 1
                        que.append((ny, nx, nc))
    
    ans = 0
    for i, j in roots:
        ans += counter[(i, j, 0)] * counter[(i, j, 1)]
    print(ans)


if __name__ == '__main__':
    solve()
