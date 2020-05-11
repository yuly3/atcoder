import sequtils, strutils

var
    acc_o: array[3000, array[3001, int]]
    acc_i: array[3000, array[3001, int]]


proc solve() =
    var H, W: int
    (H, W) = stdin.readLine.split.map(parseInt)
    let S = newSeqWith(H, stdin.readline)
    
    var j_pos = newSeq[(int, int)]()
    for i in 0..<H:
        for j in 0..<W:
            acc_o[i][j + 1] = if S[i][j] == 'O': acc_o[i][j] + 1 else: acc_o[i][j]
            if S[i][j] == 'J':
                j_pos.add((i, j))
    for i in 0..<W:
        for j in 0..<H:
            acc_i[i][j + 1] = if S[j][i] == 'I': acc_i[i][j] + 1 else: acc_i[i][j]
    
    var ans = 0
    for idx in 0..<j_pos.len:
        let (i, j) = j_pos[idx]
        ans += (acc_o[i][W] - acc_o[i][j]) * (acc_i[j][H] - acc_i[j][i])
    echo ans


when is_main_module:
    solve()
