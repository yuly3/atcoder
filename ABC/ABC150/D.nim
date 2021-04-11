import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](n: var T, m: T) {.inline.} = n = max(n, m)
proc chmin*[T: SomeNumber](n: var T, m: T) {.inline.} = n = min(n, m)
proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)

when isMainModule:
  var N, M: int
  (N, M) = inputInts()
  var a = inputInts()

  proc lcm(ar: openArray[int]): int =
    result = 1
    for n in ar:
      result = (result*n) div gcd(result, n)
      if 10^9 < result:
        return 0
  
  a.applyIt(it div 2)
  let lcmA = lcm(a)
  if lcmA == 0:
    echo 0
    quit()
  
  for ai in a:
    if lcmA div ai mod 2 == 0:
      echo 0
      quit()
  
  echo floorDiv(M, lcmA) - floorDiv(M, 2*lcmA)
