import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when isMainModule:
  let
    N = inputInt()
    a = newSeqWith(N, inputInts())
  
  var score: array[2^16, int]
  for s in 1..<2^N:
    for i in 0..<N - 1:
      if bitand(s shr i, 1) == 0:
        continue
      for j in i + 1..<N:
        if bitand(s shr j, 1) == 1:
          score[s] += a[i][j]
  
  var
    dp: array[2^16, int]
    searched: array[2^16, bool]
  searched[0] = true

  proc f(S: int): int =
    if searched[S]:
      return dp[S]
    searched[S] = true

    var
      res = 0
      T = 2^N
    while 0 < T:
      T = bitand(T - 1, S)
      res.chmax(score[T] + f(bitxor(S, T)))
    dp[S] = res
    return res

  let ans = f(2^N - 1)
  echo ans
