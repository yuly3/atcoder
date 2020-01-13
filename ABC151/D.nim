import sequtils, strutils, deques

proc solve() =
    # Nim ver1.1.1
    var H, W: int
    (H, W) = stdin.readLine.split.map(parseInt)
    var
        maze = newSeqWith(H, repeat(-2, W))
        s_point = initDeque[(int, int)]()
    for i in 0..<H:
        var line = stdin.readLine
        for j in 0..<W:
            if line[j] == '#':
                maze[i][j] = -1
            else:
                s_point.addLast((i, j))
    
    let dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    var
        ans = 0
        N = s_point.len
    for _ in 0..<N:
        var
            ans_tmp = 0
            maze_tmp = deepCopy(maze)
            (sy, sx) = s_point.popFirst
            que = initDeque[(int, int)]()
        que.addLast((sy, sx))
        maze_tmp[sy][sx] = 0
        while que.len != 0:
            let (cy, cx) = que.popFirst
            for i in 0..3:
                var
                    ny = cy + dyx[i][0]
                    nx = cx + dyx[i][1]
                if 0 <= ny and ny < H and 0 <= nx and nx < W:
                    if maze_tmp[ny][nx] == -2:
                        maze_tmp[ny][nx] = maze_tmp[cy][cx] + 1
                        ans_tmp = max(ans_tmp, maze_tmp[ny][nx])
                        que.addLast((ny, nx))
        ans = max(ans, ans_tmp)
    echo ans

when is_main_module:
    solve()
