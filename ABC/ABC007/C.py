from collections import deque


def solve():
    R, C = map(int, input().split())
    sy, sx = map(lambda x: int(x)-1, input().split())
    gy, gx = map(lambda x: int(x)-1, input().split())
    maze = [[3000 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        line = input()
        for j in range(C):
            if line[j] == '#':
                maze[i][j] = -1
    
    maze[sy][sx] = 0
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    que = deque([[sy, sx]])
    while que:
        cy, cx = que.popleft()
        if cy == gy and cx == gx:
            print(maze[gy][gx])
            exit()
        
        for i in range(4):
            if 0<=cy+move[i][0]<=R-1 and 0<=cx+move[i][1]<=C-1:
                if maze[cy+move[i][0]][cx+move[i][1]] != -1:
                    if maze[cy+move[i][0]][cx+move[i][1]] == 3000:
                        maze[cy+move[i][0]][cx+move[i][1]] = maze[cy][cx] + 1
                        que.append([cy+move[i][0], cx+move[i][1]])


if __name__ == '__main__':
    solve()
