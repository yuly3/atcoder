import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when is_main_module:
  var M, N: int
  (M, N) = inputInts()
  var
    P = newSeqWith(M, inputInt())
    CE = newSeqWith(N, inputInts())
  
  const INF = 10^9
  var dp = newSeqWith(N + 1, newSeqWith(M + 1, INF))
  for i in 0..<N:
    dp[i][0] = 0
    for j in 1..M:
      dp[i + 1][j].chmin(min(dp[i][max(0, j - CE[i][0])] + CE[i][1], dp[i][j]))
  
  P.sort(order=Descending)
  for i in 1..<M:
    P[i] += P[i - 1]
  
  var ans = 0
  for j in 0..<M:
    ans.chmax(P[j] - dp[N][j + 1])
  echo ans
