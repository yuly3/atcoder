import strutils, sequtils

proc solve() =
    var H, W: int
    (H, W) = stdin.readLine.split.map(parseInt)
    var
        A = newSeqWith(H, stdin.readLine.split.map(parseInt))
        B = newSeqWith(H, stdin.readLine.split.map(parseInt))
    
    var d = newSeqWith(H+1, newSeq[int](W+1))
    for i in 0..<H:
        for j in 0..<W:
            d[i][j] = abs(A[i][j] - B[i][j])
    
    const N = 160 * 80
    var dp: array[0..81, array[0..81, array[0..N, bool]]]
    dp[0][0][d[0][0]] = true
    for i in 0..<H:
        for j in 0..<W:
            for k in 0..N:
                if not dp[i][j][k]:
                    continue
                dp[i+1][j][k+d[i+1][j]] = true
                dp[i][j+1][k+d[i][j+1]] = true
                dp[i+1][j][abs(k - d[i+1][j])] = true
                dp[i][j+1][abs(k - d[i][j+1])] = true
    
    for k in 0..N:
        if dp[H-1][W-1][k]:
            echo k
            quit()

when is_main_module:
    solve()
