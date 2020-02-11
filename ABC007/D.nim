import strutils, sequtils

var A, B: int


proc counter(n: int): int =
    var
        DP: array[20, array[2, int]]
        n_str = $n
        n_len = n_str.len
    
    DP[0][0] = 1
    for i in 0..<n_len:
        var
            c = parseInt($n_str[i])
            cnt = 0
        
        for j in 0..<c:
            if j != 4 and j != 9:
                inc cnt
        DP[i+1][1] = 8 * DP[i][1] + cnt * DP[i][0]
        if c != 4 and c != 9:
            DP[i+1][0] = DP[i][0]
        else:
            DP[i+1][0] = 0
    return n - DP[n_len][0] - DP[n_len][1]


proc solve() =
    (A, B) = stdin.readLine.split.map(parseInt)
    var ans = counter(B) - counter(A-1)
    echo ans


when is_main_module:
    solve()
