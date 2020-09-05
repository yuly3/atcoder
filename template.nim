import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)


proc solve() =
    echo "Hello, Atcoder!!"


when is_main_module:
    solve()
