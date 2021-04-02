import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when isMainModule:
  var N, M, K: int
  (N, M, K) = inputInts()
  var A: seq[int]
  if K != 0:
    A = inputInts()

  var ban: array[100010, bool]
  for ai in A:
    ban[ai] = true
  for i in 0..N - M:
    if ban[i..<i + M].allIt(it):
      echo -1
      quit()
  
  var
    dp: array[200010, float]
    acc: float

  proc f(t: float): bool =
    acc = 0.0
    for i in countdown(N - 1, 0):
      acc -= dp[i + 1 + M]
      if ban[i]:
        dp[i] = t
      else:
        dp[i] = 1.0 + acc/float(M)
      acc += dp[i]
    return t < dp[0]

  var (ok, ng) = (1.0, 1e12)
  for _ in 0..<200:
    let mid = (ok + ng)/2.0
    if f(mid):
      ok = mid
    else:
      ng = mid
  echo ok
