import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when is_main_module:
  let
    N = inputInt()
    X = inputInts()
    M = inputInt()
    A = inputInts()
  
  var
    idToIdx = initTable[int, int]()
    filled = newSeq[bool](2020)
  for i, xi in X:
    idToIdx[i + 1] = xi
    filled[xi] = true
  
  for ai in A:
    if idToIdx[ai] == 2019 or filled[idToIdx[ai] + 1]:
      continue
    filled[idToIdx[ai]] = false
    idToIdx[ai] += 1
    filled[idToIdx[ai]] = true
  
  for i in 1..N:
    echo idToIdx[i]
