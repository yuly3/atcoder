import sequtils, strutils, queues, algorithm

proc solve() =
    var H, W: int
    (H, W) = stdin.readLine.strip.split.map(parseInt)
    var grid = newSeqWith(H, newSeq[int](W))
    for i in 0..<H:
        grid[i].fill(3)
    var grid_str = mapIt(0..<H, stdin.readLine)
    type P = object
        y, x: int
    var que = initQueue[P]()
    for i in 0..<H:
        for j in 0..<W:
            if grid_str[i][j] == 's':
                grid[i][j] = 0
                que.enqueue(P(y: i, x: j))
    
    let dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while que.len != 0:
        let cur = que.dequeue
        for i in 0..3:
            var
                ny = cur.y + dyx[i][0]
                nx = cur.x + dyx[i][1]
            if 0 <= ny and ny < H and 0 <= nx and nx < W:
                if grid_str[ny][nx] == '#' and grid[cur.y][cur.x] + 1 < grid[ny][nx]:
                    grid[ny][nx] = grid[cur.y][cur.x] + 1
                    if grid[ny][nx] != 3:
                        que.enqueue(P(y: ny, x: nx))
                elif grid_str[ny][nx] == '.' and grid[cur.y][cur.x] < grid[ny][nx]:
                    grid[ny][nx] = grid[cur.y][cur.x]
                    que.enqueue(P(y: ny, x: nx))
                elif grid_str[ny][nx] == 'g':
                    echo "YES"
                    quit 0
    echo "NO"

solve()
