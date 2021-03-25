import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when isMainModule:
  var
    _ = inputInt()
    a = inputInts()
  
  const INF = 10^9
  var lis: array[10^5 + 1, int]
  lis.fill(INF)
  for ai in a:
    let idx = lowerBound(lis, ai)
    lis[idx] = ai
  echo lowerBound(lis, INF)
