import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when is_main_module:
  var
    N = inputInt()
    A = concat(@[0], inputInts())
  A.add(0)
  
  var
    isSinking = newSeq[bool](N + 2)
    ans = 0
  for i, ai in A:
    if ai == 0:
      isSinking[i] = true
      if i != N + 1 and 0 < A[i + 1]:
        inc ans

  let sortedA = sortedByIt(toSeq(A.pairs), it[1])
  var cnt = ans
  for j, (idx, ai) in sortedA:
    if isSinking[idx]:
      continue
    
    if isSinking[idx - 1] and isSinking[idx + 1]:
      dec cnt
    elif not isSinking[idx - 1] and not isSinking[idx + 1]:
      inc cnt
    if j == N + 1 or sortedA[j + 1][1] != ai:
      ans.chmax(cnt)
    isSinking[idx] = true
  echo ans
