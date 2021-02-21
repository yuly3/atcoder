import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
  return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
  num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
  num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
  num0 = floorMod(num0, num1)

proc solve() =
  let K = input().parseInt

  var ans: int
  for a in 1..K:
    for b in 1..K:
      if K < a * b:
        break
      ans += K div (a * b)
  echo ans

when is_main_module:
  solve()
