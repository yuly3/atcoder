import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when isMainModule:
  var N, M: int
  (N, M) = inputInts()
  let
    A = inputInts()
    B = inputInts()
  
  var dp: array[1010, array[1010, int]]
  for i in 1..N:
    dp[i][0] = i
  for j in 1..M:
    dp[0][j] = j
  
  for i in 1..N:
    for j in 1..M:
      if A[i - 1] == B[j - 1]:
        dp[i][j] = min([dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1]])
      else:
        dp[i][j] = min([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]]) + 1
  echo dp[N][M]
