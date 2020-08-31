import sequtils, strutils


proc solve() =
    var
        N = stdin.readLine.parseInt
        A = stdin.readLine.split.map(parseInt)
    
    var
        left = 0
        right = 1
        ans = 1
    while right < N:
        if A[right - 1] <= A[right]:
            ans = max(ans, right - left + 1)
        else:
            left = right
        inc right
    echo ans


when is_main_module:
    solve()
