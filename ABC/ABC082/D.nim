import strutils, sequtils


proc solve() =
    var
        s = stdin.readLine
        x, y: int
    (x, y) = stdin.readLine.split.map(parseInt)
    
    var move_x, move_y = newSeq[int]()
    move_y.add(0)
    var direction, cnt = 0
    for i in 0..<len(s):
        if s[i] == 'F':
            cnt += 1
        if s[i] == 'T' or i == len(s) - 1:
            if direction == 0:
                move_x.add(cnt)
            else:
                move_y.add(cnt)
            direction = direction xor 1
            cnt = 0
    
    var dp_x = newSeqWith(len(move_x), newSeq[bool](16001))
    dp_x[0][8000 + move_x[0]] = true
    for i in 1..<len(move_x):
        for j in 0..16000:
            if dp_x[i - 1][j]:
                dp_x[i][j + move_x[i]] = true
                dp_x[i][j - move_x[i]] = true
    
    var dp_y = newSeqWith(len(move_y), newSeq[bool](16001))
    dp_y[0][8000] = true
    for i in 1..<len(move_y):
        for j in 0..16000:
            if dp_y[i - 1][j]:
                dp_y[i][j + move_y[i]] = true
                dp_y[i][j - move_y[i]] = true
    
    if dp_x[^1][8000 + x] and dp_y[^1][8000 + y]:
        echo "Yes"
    else:
        echo "No"


when is_main_module:
    solve()
