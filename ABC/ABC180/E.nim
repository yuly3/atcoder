import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
    num0 = num0 mod num1

var
    XYZ: seq[(int, int, int)]
    dp: array[17, array[1 shl 17, int]]

proc solve() =
    let N = input().parseInt
    var xi, yi, zi: int
    for _ in 0..<N:
        (xi, yi, zi) = input().split.map(parseInt)
        XYZ.add((xi, yi, zi))
    
    const INF = 10^18
    for i in 0..<N:
        dp[i].fill(INF)
    dp[0][0] = 0
    for s in 0..<1 shl N:
        for i in 0..<N:
            (xi, yi, zi) = XYZ[i]
            for j, (xj, yj, zj) in XYZ:
                if bitand((s shr j), 1) == 1:
                    continue
                let ns = bitor(s, (1 shl j))
                dp[j][ns].chmin(dp[i][s] + abs(xj - xi) + abs(yj - yi) + max(0, zj - zi))
    echo dp[0][(1 shl N) - 1]

when is_main_module:
    solve()
