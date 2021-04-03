import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when isMainModule:
  var N, X: int
  (N, X) = inputInts()
  var A = inputInts()

  var dp: array[100, Table[int, int]]
  for i in 0..N:
    dp[i] = initTable[int, int]()
  
  proc f(cur, d: int): int =
    if cur == N - 1:
      return 1
    if d in dp[cur]:
      return dp[cur][d]
    
    let p = A[cur + 1] div A[cur]
    if floorMod(d, p) == 0:
      dp[cur][d] = f(cur + 1, floorDiv(d, p))
    else:
      dp[cur][d] = f(cur + 1, floorDiv(d, p)) + f(cur + 1, -floorDiv(-d, p))
    return dp[cur][d]
  
  echo f(0, X)
