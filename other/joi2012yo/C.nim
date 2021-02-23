import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string = stdin.readLine
proc inputs*(): seq[string] = stdin.readLine.split
proc inputInt*(): int = stdin.readLine.parseInt
proc inputInts*(): seq[int] = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) = num0 = floorMod(num0, num1)

var
  D: seq[int]
  dp: seq[seq[int]]

proc solve() =
  let N = inputInt()
  var A, B: int
  (A, B) = inputInts()
  let C = inputInt()
  D = newSeqWith(N, inputInt())

  const INF = 10^18
  dp = newSeqWith(N + 1, newSeqWith(N + 1, -INF))
  dp[0][0] = 0
  for i in 0..<N:
    for j in 0..<N:
      dp[i + 1][j].chmax(dp[i][j])
      dp[i + 1][j + 1].chmax(dp[i][j] + D[i])
  
  var ans = 0
  for i in 0..N:
    ans.chmax((C + dp[N][i]) div (A + i*B))
  echo ans

when is_main_module:
  solve()
