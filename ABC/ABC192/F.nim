import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
  return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
  num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
  num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
  num0 = floorMod(num0, num1)

var
  dp: seq[seq[seq[int]]]

proc solve() =
  var N, X: int
  (N, X) = input().split.map(parseInt)
  let A = input().split.map(parseInt)

  const INF = 10^18
  var ans = INF
  for cnt in 1..N:
    dp = newSeqWith(N + 1, newSeqWith(cnt + 1, newSeqWith(cnt, -INF)))
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

when is_main_module:
  solve()
