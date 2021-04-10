import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](n: var T, m: T) {.inline.} = n = max(n, m)
proc chmin*[T: SomeNumber](n: var T, m: T) {.inline.} = n = min(n, m)
proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)

when isMainModule:
  import complex

  let N = inputInt()
  var
    points = newSeq[Complex64]()
    x, y: float
  for _ in 0..<N:
    (x, y) = inputs().map(parseFloat)
    points.add(complex(x, y))
  
  proc maxDist(center: Complex64): float =
    var res: float
    for point in points:
      res.chmax(abs(point - center))
    return res

  proc f(x: float): float =
    var (ok, ng) = (0.0, 1e4)
    for _ in 0..<100:
      let
        lower = (ok*2 + ng) / 3
        higher = (ok + ng*2) / 3
      if maxDist(complex(x, higher)) < maxDist(complex(x, lower)):
        ok = lower
      else:
        ng = higher
    return maxDist(complex(x, ok))

  var (ok, ng) = (0.0, 1e4)
  for _ in 0..<100:
    let
      left = (ok*2 + ng) / 3
      right = (ok + ng*2) / 3
    if f(right) < f(left):
      ok = left
    else:
      ng = right
  echo f(ok)
