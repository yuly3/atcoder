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
  let A = inputInts()

  const INF = 10^18
  var
    dp: array[101, array[101, array[100, int]]]
    ans = INF
  for cnt in 1..N:
    for i in 0..N:
      for j in 0..cnt:
        dp[i][j].fill(-INF)
    dp[0][0][0] = 0
    for i in 0..<N:
      for j in 0..cnt:
        for k in 0..<cnt:
          dp[i + 1][j][k].chmax(dp[i][j][k])
          if j != cnt:
            dp[i + 1][j + 1][(k + A[i]) mod cnt].chmax(dp[i][j][k] + A[i])
    let v = dp[N][cnt][X mod cnt]
    if v < 1:
      continue
    ans.chmin((X - v) div cnt)
  echo ans
