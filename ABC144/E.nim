import strutils, sequtils, algorithm, math

var
    N, K: int
    A, F: seq[int]
    sum_A: int


proc calc(t: int): bool =
    var new_sum_A = 0
    for i in 0..<N:
        new_sum_A += min(A[i], t div F[i])
    
    if sum_A - new_sum_A <= K:
        return true
    else:
        return false


proc solve() =
    (N, K) = stdin.readLine.split.map(parseInt)
    A = stdin.readLine.split.map(parseInt).sortedByIt(it)
    F = stdin.readLine.split.map(parseInt).sortedByIt(it).reversed
    sum_A = sum(A)
    
    var (left, right) = (-1, 10^13)
    while 1 < right - left:
        let mid = (left + right) div 2
        if calc(mid):
            right = mid
        else:
            left = mid
    echo right


when is_main_module:
    solve()
