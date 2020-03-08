import strutils, sequtils, math


proc solve() =
    var
        N = stdin.readLine.parseInt
        s = mapIt(0..<N, stdin.readLine.parseInt)
        dp: array[10001, bool]
    
    dp[0] = true
    var s_sum = sum(s)
    for si in s:
        for i in countdown(s_sum, 0):
            if dp[i]:
                dp[i + si] = true
    
    var ans = 0
    for i in countdown(s_sum, 0):
        if dp[i] and i mod 10 != 0:
            ans = i
            break
    echo ans


when is_main_module:
    solve()
