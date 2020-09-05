import sequtils, strutils

proc input(): string =
    return stdin.readLine
proc chmax(num0: var SomeNumber, num1: SomeNumber) =
    num0 = max(num0, num1)

var dp0, dp1: array[30000000, int]

proc solve() =
    let N = input().parseInt
    var ga, sa, ba, gb, sb, bb: int
    (ga, sa, ba) = input().split.map(parseInt)
    (gb, sb, bb) = input().split.map(parseInt)

    dp0[0] = N
    var M = N
    for i in 0..N:
        dp0[i + ga].chmax(dp0[i] - ga + gb)
        dp0[i + sa].chmax(dp0[i] - sa + sb)
        dp0[i + ba].chmax(dp0[i] - ba + bb)
        M.chmax(dp0[i])
    
    dp1[0] = M
    var ans = M
    for i in 0..M:
        dp1[i + gb].chmax(dp1[i] - gb + ga)
        dp1[i + sb].chmax(dp1[i] - sb + sa)
        dp1[i + bb].chmax(dp1[i] - bb + ba)
        ans.chmax(dp1[i])
    echo ans


when is_main_module:
    solve()
