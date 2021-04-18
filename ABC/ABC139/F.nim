import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](n: var T, m: T) {.inline.} = n = max(n, m)
proc chmin*[T: SomeNumber](n: var T, m: T) {.inline.} = n = min(n, m)
proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)

when isMainModule:
  let N = inputInt()
  var
    vertexes: seq[tuple[x: float, y: float]]
    xi, yi: float
  for _ in 0..<N:
    (xi, yi) = inputs().map(parseFloat)
    vertexes.add((xi, yi))
  vertexes.sort((u, v) => (if arctan2(v.y, v.x) < arctan2(u.y, u.x): 1 else: -1))

  var ans: float
  for left in 0..<N:
    var X, Y: float
    for right in 0..<N:
      let v = vertexes[(left + right) mod N]
      X += v.x
      Y += v.y
      ans.chmax(hypot(X, Y))
  echo ans
