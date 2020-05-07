import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    sy, sx, gy, gx = 0, 0, 0, 0
    nums = set()
    A = [[] for _ in range(N)]
    for i in range(N):
        ai = list(rl().rstrip())
        for j in range(M):
            aij = ai[j]
            if aij == 'S':
                sy, sx = i, j
            elif aij == 'G':
                gy, gx = i, j
            else:
                aij = int(aij)
                ai[j] = aij
                nums.add(aij)
        A[i] = ai
    
    if len(nums) != 9:
        print(-1)
        return()
    
    INF = 10 ** 9
    maze = [[[INF] * 10 for _ in range(M)] for _ in range(N)]
    maze[sy][sx][0] = 0
    que = deque([(sy, sx, 0)])
    while que:
        cy, cx, cn = que.popleft()
        if (cy, cx, cn) == (gy, gx, 9):
            print(maze[gy][gx][9])
            return
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M:
                n_cost = maze[cy][cx][cn] + 1
                nn = cn + (A[ny][nx] == cn + 1)
                if n_cost < maze[ny][nx][nn]:
                    maze[ny][nx][nn] = n_cost
                    que.append((ny, nx, nn))


if __name__ == '__main__':
    solve()
