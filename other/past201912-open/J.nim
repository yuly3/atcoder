import strutils, sequtils, queues


proc solve() =
    var H, W: int
    (H, W) = stdin.readLine.split.map(parseInt)
    let A = mapIt(0..<H, stdin.readLine.split.map(parseInt))
    const
        INF = 1000000000
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
    
    proc bfs(sy, sx: int): int =
        var res: array[50, array[50, int]]
        for y in 0..<H:
            for x in 0..<W:
                res[y][x] = INF
        res[sy][sx] = A[sy][sx]
        var que = initQueue[(int, int)]()
        que.enqueue((sy, sx))
        while que.len != 0:
            let (cy, cx) = que.dequeue
            for k in 0..3:
                let
                    ny = cy + dy[k]
                    nx = cx + dx[k]
                if 0 <= ny and ny < H and 0 <= nx and nx < W:
                    let cost = res[cy][cx] + A[ny][nx]
                    if cost < res[ny][nx]:
                        res[ny][nx] = cost
                        que.enqueue((ny, nx))
        return res[H - 1][0] + res[H - 1][W - 1] + res[0][W - 1] - 2 * res[sy][sx]
    
    var ans = INF
    for i in 0..<H:
        for j in 0..<W:
            ans = min(ans, bfs(i, j))
    echo ans


when is_main_module:
    solve()
