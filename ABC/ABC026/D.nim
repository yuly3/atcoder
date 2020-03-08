import sequtils, strutils, math

var
    A, B, C: float
(A, B, C) = stdin.readLine.split.map(parseFloat)

proc calc(t: float): bool =
    var f = A * t + B * sin(C * t * PI)
    if 100 <= f:
        return true
    else:
        return false

proc solve() =
    var
        left: float = 0
        right: float = float(10 ^ 7)
    for _ in 0..<100:
        var mid = (left + right) / 2
        if calc(mid):
            right = mid
        else:
            left = mid
    echo right

solve()
