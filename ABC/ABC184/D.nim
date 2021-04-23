import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](n: var T, m: T) {.inline.} = n = max(n, m)
proc chmin*[T: SomeNumber](n: var T, m: T) {.inline.} = n = min(n, m)
proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)

when isMainModule:
  var A, B, C: int
  (A, B, C) = inputInts()

  var dp: array[101, array[101, array[101, float]]]

  proc f(x, y, z: int): float =
    if 100 in [x, y, z]:
      return 0.0
    if dp[x][y][z] != 0.0:
      return dp[x][y][z]

    let
      incX = f(x + 1, y, z) + 1
      incY = f(x, y + 1, z) + 1
      incZ = f(x, y, z + 1) + 1
      den = float(x + y + z)
    result = (x.float*incX + y.float*incY + z.float*incZ) / den
    dp[x][y][z] = result

  echo f(A, B, C)
