import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    r, c = map(lambda n: int(n) - 1, rl().split())
    s = [rl().rstrip() for _ in range(H)]
    
    ans = [['x'] * W for _ in range(H)]
    ans[r][c] = 'o'
    for i in range(H):
        for j in range(W):
            if s[i][j] == '#':
                ans[i][j] = '#'
    
    can_get = [[False] * W for _ in range(H)]
    can_get[r][c] = True
    dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
    que = deque([(r, c)])
    while que:
        cy, cx = que.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < H and 0 <= nx < W and not can_get[ny][nx] and s[ny][nx] != '#':
                if s[ny][nx] == 'v' and i != 0:
                    continue
                if s[ny][nx] == '<' and i != 1:
                    continue
                if s[ny][nx] == '^' and i != 2:
                    continue
                if s[ny][nx] == '>' and i != 3:
                    continue
                can_get[ny][nx] = True
                ans[ny][nx] = 'o'
                que.append((ny, nx))
    
    print('\n'.join(''.join(ans_i) for ans_i in ans))


if __name__ == '__main__':
    solve()
