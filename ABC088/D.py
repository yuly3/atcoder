from collections import deque


def solve():
    H, W = map(int, input().split())
    p_black = 0
    maze = [[3000 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        line = input()
        for j in range(W):
            if line[j] == '#':
                maze[i][j] = -1
                p_black += 1
    maze[0][0] = 0
    
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    que = deque([[0, 0]])
    white = 1
    while que:
        cy, cx = que.popleft()
        if cy == H - 1 and cx == W - 1:
            white += maze[H - 1][W - 1]
            break
        
        for i in range(4):
            ny = cy + move[i][0]
            nx = cx + move[i][1]
            if 0 <= ny <= H - 1 and 0 <= nx <= W - 1:
                if maze[ny][nx] == 3000:
                    maze[ny][nx] = maze[cy][cx] + 1
                    que.append([ny, nx])
    
    if white == 1:
        print(-1)
    else:
        ans = H * W - p_black - white
        print(ans)


if __name__ == '__main__':
    solve()
