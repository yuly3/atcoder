import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string = stdin.readLine
proc inputs*(): seq[string] = stdin.readLine.split
proc inputInt*(): int = stdin.readLine.parseInt()
proc inputInts*(): seq[int] = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) = num0 = floorMod(num0, num1)

proc solve() =
  echo "Hello, Atcoder!!"

when is_main_module:
  solve()
