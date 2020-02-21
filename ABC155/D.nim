import strutils, sequtils, math, algorithm

var
    N, K: int
    A: seq[int]
    under, over: seq[int]
    len_under, len_over: int


proc calc(t: int): bool =
    var
        cnt = 0
        i: int
    
    if 0 <= t:
        i = len_over
        for ai in over:
            while 0 < i and t < over[i - 1] * ai:
                dec i
            cnt += i
            if ai^2 <= t:
                dec cnt
        i = len_under
        for ai in under:
            while 0 < i and t < under[i - 1] * ai:
                dec i
            cnt += i
            if ai^2 <= t:
                dec cnt
        cnt = cnt div 2 + len_over * len_under
    
    else:
        i = len_under
        for ai in over:
            while 0 < i and under[i - 1] * ai <= t:
                dec i
            cnt += len_under - i
    
    if K <= cnt:
        return true
    else:
        return false


proc solve() =
    (N, K) = stdin.readLine.split.map(parseInt)
    A = stdin.readLine.split.map(parseInt)
    A.sort(system.cmp)
    let idx = A.lowerbound(0, system.cmp)
    under = A[0..idx - 1]
    under.reverse()
    over = A[idx..N - 1]
    (len_under, len_over) = (len(under), len(over))
    
    var (ok, ng) = (10^18, -(10^18 + 1))
    while 1 < ok - ng:
        let mid = (ok + ng) div 2
        if calc(mid):
            ok = mid
        else:
            ng = mid
    echo ok


when is_main_module:
    solve()
