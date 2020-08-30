import deques, math, sequtils, strutils

var
    S: array[1010, string]
    costs: array[1010, array[1010, int]]
    que: Deque[(int, int, int)]


proc solve() =
    var H, W, ch, cw, dh, dw: int
    (H, W) = stdin.readLine.split.map(parseInt)
    (ch, cw) = stdin.readLine.split.map(parseInt)
    (dh, dw) = stdin.readLine.split.map(parseInt)
    dec ch; dec cw; dec dh; dec dw
    for i in 0..<H:
        S[i] = stdin.readLine
    
    for i in 0..<H:
        for j in 0..<W:
            costs[i][j] = 10 ^ 9
    que = initDeque[(int, int, int)]()
    que.addLast((0, ch, cw))

    var cost, cy, cx, ny, nx: int
    while len(que) != 0:
        (cost, cy, cx) = que.popFirst()
        if cy == dh and cx == dw:
            echo cost
            return
        for (dy, dx) in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            (ny, nx) = (cy + dy, cx + dx)
            if 0 <= ny and ny < H and 0 <= nx and nx < W:
                if S[ny][nx] == '#':
                    continue
                if costs[ny][nx] <= cost:
                    continue
                que.addFirst((cost, ny, nx))
                costs[ny][nx] = cost
        for dy in -2..2:
            for dx in -2..2:
                (ny, nx) = (cy + dy, cx + dx)
                if 0 <= ny and ny < H and 0 <= nx and nx < W:
                    if S[ny][nx] == '#':
                        continue
                    if costs[ny][nx] <= cost + 1:
                        continue
                    que.addLast((cost + 1, ny, nx))
                    costs[ny][nx] = cost + 1
    echo -1


when is_main_module:
    solve()
