import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string = stdin.readLine
proc inputs*(): seq[string] = stdin.readLine.split
proc inputInt*(): int = stdin.readLine.parseInt
proc inputInts*(): seq[int] = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) = num0 = floorMod(num0, num1)

var
  accJ, accO, accI, subJO, subJI: seq[int]
  idxTable: Table[(int, int), seq[int]]

proc solve() =
  let
    N = inputInt()
    S = input()
  
  (accJ, accO, accI) = (newSeq[int](N + 1), newSeq[int](N + 1), newSeq[int](N + 1))
  for i, si in S:
    accJ[i + 1] = if si == 'J': accJ[i] + 1 else: accJ[i]
    accO[i + 1] = if si == 'O': accO[i] + 1 else: accO[i]
    accI[i + 1] = if si == 'I': accI[i] + 1 else: accI[i]
  
  (subJO, subJI) = (newSeq[int](N + 1), newSeq[int](N + 1))
  for i in 1..N:
    subJO[i] = accJ[i] - accO[i]
    subJI[i] = accJ[i] - accI[i]
  
  idxTable = initTable[(int, int), seq[int]]()
  for i in 0..N:
    if (subJO[i], subJI[i]) notin idxTable:
      idxTable[(subJO[i], subJI[i])] = newSeq[int]()
    idxTable[(subJO[i], subJI[i])].add(i)
  
  var ans = 0
  for idx in idxTable.values:
    let
      left = min(idx)
      right = max(idx)
    ans.chmax(right - left)
  echo ans

when is_main_module:
  solve()
