import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
  return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
  num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
  num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
  num0 = num0 mod num1

var
  A, B: seq[int]
  dp: array[1010, array[1010, int]]

proc solve() =
  var N, M: int
  (N, M) = input().split.map(parseInt)
  A = input().split.map(parseInt)
  B = input().split.map(parseInt)

  for i in 0..N:
    for j in 0..M:
      if i == 0:
        dp[i][j] = j
        continue
      if j == 0:
        dp[i][j] = i
        continue
      if A[i - 1] != B[j - 1]:
        dp[i][j] = min([dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1])
      else:
        dp[i][j] = min([dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1]])
  echo dp[N][M]

when is_main_module:
  solve()
