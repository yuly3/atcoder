import sys
from collections import deque
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    S = [rl().rstrip() for _ in range(N)]
    
    maze = [[False] * M for _ in range(N)]
    wall = []
    for i in range(N):
        for j in range(M):
            if S[i][j] == '#':
                maze[i][j] = True
                wall.append((i, j))
    
    ans = 0
    for sy, sx in wall:
        n_maze = deepcopy(maze)
        que = deque([(sy, sx)])
        while que:
            cy, cx = que.popleft()
            for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < N and 0 <= nx < M and not n_maze[ny][nx]:
                    n_maze[ny][nx] = True
                    que.append((ny, nx))
        ans += all(False not in n_maze_i for n_maze_i in n_maze)
    print(ans)


if __name__ == '__main__':
    solve()
