import strutils


proc solve() =
    var
        N = stdin.readLine.parseInt
        NG1 = stdin.readLine.parseInt
        NG2 = stdin.readLine.parseInt
        NG3 = stdin.readLine.parseInt
        dp: array[301, bool]
    
    dp[N] = true
    var cnt = 0
    while cnt < 100:
        inc cnt
        for i in 1..N:
            if dp[i] and i notin [NG1, NG2, NG3]:
                if 2 < i:
                    dp[i-3] = true
                if 1 < i:
                    dp[i-2] = true
                dp[i-1] = true
    
    if dp[0]:
        echo "YES"
    else:
        echo "NO"


when is_main_module:
    solve()
