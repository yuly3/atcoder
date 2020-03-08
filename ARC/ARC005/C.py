from collections import deque


def solve():
    H, W = map(int, input().split())
    grid = [[3 for _ in range(W)] for _ in range(H)]
    grid_str = ['' for _ in range(H)]
    que = deque([])
    for i in range(H):
        grid_str[i] = input()
        for j in range(W):
            if grid_str[i][j] == 's':
                grid[i][j] = 0
                que.append([i, j])
    
    dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while que:
        cy, cx = que.popleft()
        for i in range(4):
            ny = cy + dyx[i][0]
            nx = cx + dyx[i][1]
            if 0 <= ny < H and 0 <= nx < W:
                if grid_str[ny][nx] == '#' and grid[cy][cx] + 1 < grid[ny][nx]:
                    grid[ny][nx] = grid[cy][cx] + 1
                    if grid[ny][nx] != 3:
                        que.append([ny, nx])
                elif grid_str[ny][nx] == '.' and grid[cy][cx] < grid[ny][nx]:
                    grid[ny][nx] = grid[cy][cx]
                    que.appendleft([ny, nx])
                elif grid_str[ny][nx] == 'g':
                    print('YES')
                    exit()
    print('NO')


if __name__ == '__main__':
    solve()
