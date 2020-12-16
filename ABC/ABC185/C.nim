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
  dp: array[210, array[12, int]]

proc solve() =
  var L = input().parseInt

  dp[0][0] = 1
  for i in 1..<L:
    dp[i][0] = dp[i - 1][0]
    for j in 1..11:
      dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
  echo dp[L - 1][11]

when is_main_module:
  solve()
