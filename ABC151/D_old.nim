import sequtils, strutils, queues

proc solve() =
    # Nim ver0.13
    var H, W: int
    (H, W) = stdin.readLine.split.map(parseInt)
    type P = object
        y, x: int
    var
        maze = newSeqWith(H, repeat(-2, W))
        s_point = initQueue[P]()
    for i in 0..<H:
        var line = stdin.readLine
        for j in 0..<W:
            if line[j] == '#':
                maze[i][j] = -1
            else:
                s_point.enqueue(P(y: i, x: j))
    
    let dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    var
        ans = 0
        N = s_point.len
    for _ in 0..<N:
        var
            ans_tmp = 0
            maze_tmp = maze
            start = s_point.dequeue
            que = initQueue[P]()
        que.enqueue(P(y: start.y, x: start.x))
        maze_tmp[start.y][start.x] = 0
        while que.len != 0:
            let cur = que.dequeue
            for i in 0..3:
                var
                    ny = cur.y + dyx[i][0]
                    nx = cur.x + dyx[i][1]
                if 0 <= ny and ny < H and 0 <= nx and nx < W:
                    if maze_tmp[ny][nx] == -2:
                        maze_tmp[ny][nx] = maze_tmp[cur.y][cur.x] + 1
                        ans_tmp = max(ans_tmp, maze_tmp[ny][nx])
                        que.enqueue(P(y: ny, x: nx))
        ans = max(ans, ans_tmp)
    echo ans

when is_main_module:
    solve()
