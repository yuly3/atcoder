import deques, sequtils, strutils, math

var
    c: seq[string]
    costs: seq[seq[int]]
    que: Deque[(int, int)]


proc solve() =
    var H, W, K, sy, sx, gy, gx: int
    (H, W, K) = stdin.readLine.split.map(parseInt)
    (sy, sx, gy, gx) = stdin.readLine.split.mapIt(it.parseInt - 1)
    c = newSeqWith(H, stdin.readLine)

    const INF = 10^10
    costs = newSeqWith(H, newSeqWith(W, INF))
    costs[sy][sx] = 0
    que = initDeque[(int, int)]()
    que.addLast((sy, sx))

    var cy, cx, ny, nx: int
    while que.len != 0:
        (cy, cx) = que.popFirst()
        for (dy, dx) in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            for k in 1..K:
                (ny, nx) = (cy + k * dy, cx + k * dx)
                if 0 <= ny and ny < H and 0 <= nx and nx < W:
                    if c[ny][nx] == '@':
                        break
                    if costs[ny][nx] <= costs[cy][cx]:
                        break
                    if costs[cy][cx] + 1 < costs[ny][nx]:
                        costs[ny][nx] = costs[cy][cx] + 1
                        que.addLast((ny, nx))
    
    if costs[gy][gx] != INF:
        echo costs[gy][gx]
    else:
        echo -1


when is_main_module:
    solve()
