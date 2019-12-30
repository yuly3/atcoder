import sequtils, strutils, math

var
    R, B: int
    x, y: int
(R, B) = stdin.readLine.split.map(parseInt)
(x, y) = stdin.readLine.split.map(parseInt)

proc calc(k: int): bool =
    var
        r = (R - k) div (x - 1)
        b = (B - k) div (y - 1)
    if k <= r + b:
        return true
    else:
        return false

proc solve() =
    var
        left = 0
        right = min(R, B) + 1
    while 1 < right - left:
        var mid = (left + right) div 2
        if calc(mid):
            left = mid
        else:
            right = mid
    echo left

solve()
