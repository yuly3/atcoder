import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
    num0 = num0 mod num1

proc solve() =
    var A, B, C, D: int
    (A, B, C, D) = input().split.map(parseInt)

    if B < C or D < A:
        echo "No"
    else:
        echo "Yes"

when is_main_module:
    solve()
