import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when is_main_module:
  var N, T, S: int
  (N, T, S) = inputInts()
  var A, B: array[3010, int]
  for i in 0..<N:
    (A[i], B[i]) = inputInts()
  
  var dp1: array[3010, array[3010, int]]
  for i in 0..<N:
    for j in 0..S:
      dp1[i + 1][j].chmax(dp1[i][j])
      if S < j + B[i]:
        continue
      dp1[i + 1][j + B[i]].chmax(dp1[i][j] + A[i])
  
  var dp2: array[3010, array[3010, int]]
  for i in countdown(N, 1):
    for j in 0..T - S:
      dp2[i - 1][j].chmax(dp2[i][j])
      if T - S < j + B[i - 1]:
        continue
      dp2[i - 1][j + B[i - 1]].chmax(dp2[i][j] + A[i - 1])
  
  var ans = 0
  for i in 0..<N:
    ans.chmax(dp1[i][S] + dp2[i][T - S])
  echo ans
