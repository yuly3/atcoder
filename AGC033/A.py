from collections import deque


def solve():
    H, W = map(int, input().split())
    grid = [['' for _ in range(W)] for _ in range(H)]
    que = deque()
    for i in range(H):
        grid[i] = list(input())
        for j in range(W):
            if grid[i][j] == '#':
                que.append([i, j])
    
    xy = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    ans = 0
    while que:
        n = len(que)
        for _ in range(n):
            y, x = que.popleft()
            for i in range(4):
                xi = x - xy[i][0]
                yi = y - xy[i][1]
                if 0 <= xi <= W-1 and 0 <= yi <= H-1:
                    if grid[yi][xi] == '.':
                        grid[yi][xi] = '#'
                        que.append([yi, xi])
        ans += 1
    print(ans-1)


if __name__ == '__main__':
    solve()