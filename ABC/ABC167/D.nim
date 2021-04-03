import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when isMainModule:
  var N, K: int
  (N, K) = inputInts()
  var A = inputInts()
  A.applyIt(it - 1)

  var lv = 1
  while 2^lv <= K:
    inc lv
  
  var doubling: array[64, array[200010, int]]
  for i in 0..<N:
    doubling[0][i] = A[i]
  for k in 0..<lv - 1:
    for i in 0..<N:
      doubling[k + 1][i] = doubling[k][doubling[k][i]]
  
  var cur, k: int
  while 0 < K:
    if bitand(K, 1) == 1:
      cur = doubling[k][cur]
    inc k
    K = K shr 1
  echo cur + 1
