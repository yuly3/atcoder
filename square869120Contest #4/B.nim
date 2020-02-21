import strutils, sequtils, math


proc solve() =
    var N, K: int
    (N, K) = stdin.readLine.split.map(parseInt)
    var a = stdin.readLine.split.map(parseInt)
    
    if K == 1:
        echo 0
        quit()
    
    var ans = 15 * 10^10
    for s in 0..<2^N:
        var cnt = 0
        for i in 1..<N:
            if ((s shr i) and 1) == 1:
                inc cnt
        if cnt < K - 1:
            continue
        
        var
            p_hight = 0
            cost = 0
            tmp = a
        for i in 1..<N:
            p_hight = max(p_hight, tmp[i - 1])
            if ((s shr i) and 1) == 1:
                cost += max(p_hight + 1, a[i]) - a[i]
                tmp[i] = max(p_hight + 1, a[i])
        ans = min(ans, cost)
    echo ans


when is_main_module:
    solve()
