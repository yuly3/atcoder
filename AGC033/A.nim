import strutils, sequtils, queues

proc solve() =
    var H, W: int
    (H, W) = stdin.readLine.strip.split.map(parseInt)
    var grid = mapIt(0..<H, stdin.readLine)

    type P = object
        y, x: int
    var que = initQueue[P]()
    for i in 0..<H:
        for j in 0..<W:
            if grid[i][j] == '#':
                que.enqueue(P(y: i, x: j))
    
    let dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    var ans = 0
    while que.len != 0:
        var n = que.len
        for _ in 0..<n:
            let cur = que.dequeue
            for i in 0..3:
                var
                    ny = cur.y + dyx[i][0]
                    nx = cur.x + dyx[i][1]
                if 0 <= ny and ny < H and 0 <= nx and nx < W:
                    if grid[ny][nx] == '.':
                        grid[ny][nx] = '#'
                        que.enqueue(P(y: ny, x: nx))
        ans += 1
    echo ans-1

solve()