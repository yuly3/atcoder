import algorithm, math, sequtils, strutils


proc solve() =
    var N, M: int
    (N, M) = stdin.readLine.split.map(parseInt)
    var A = stdin.readLine.split.map(parseInt)
    A.sort()

    proc calc(t: int): bool =
        var cnt = 0
        for ai in A:
            cnt += N - A.lowerBound(t - ai)
        return M <= cnt

    var ok, ng, mid: int
    (ok, ng) = (0, 2 * 10^5 + 1)
    while 1 < ng - ok:
        mid = (ok + ng) div 2
        if calc(mid):
            ok = mid
        else:
            ng = mid
    
    var acc_A = newSeq[int](N)
    acc_A[^1] = A[^1]
    for i in countdown(N - 2, 0):
        acc_A[i] = acc_A[i + 1] + A[i]
    
    var ans, add_cnt, idx: int
    for ai in A:
        idx = A.lowerBound(ok - ai)
        if idx == N:
            continue
        add_cnt += N - idx
        ans += (N - idx) * ai + acc_A[idx]
    ans -= ok * (add_cnt - M)
    echo ans


when is_main_module:
    solve()
