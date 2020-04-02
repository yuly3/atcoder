import strutils, sequtils, math

proc popcount[T: int64|int](a: T): cint {. importc: "__builtin_popcountl", nodecl, nosideeffect.}


proc solve() =
    const MOD = 10^9 + 7
    var
        N = stdin.readLine.parseInt
        a = newSeqWith(N, stdin.readLine.split.map(parseInt))
        dp: array[1 shl 21, int]
    
    dp[0] = 1
    for S in 0..<(1 shl N):
        var i = S.popcount
        for j in 0..<N:
            if (S shr j and 1) == 0 and a[i][j] == 1:
                dp[S or (1 shl j)] = (dp[S or (1 shl j)] + dp[S]) mod MOD
    echo dp[(1 shl N) - 1]


when is_main_module:
    solve()
