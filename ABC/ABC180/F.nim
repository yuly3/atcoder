import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](n: var T, m: T) {.inline.} = n = max(n, m)
proc chmin*[T: SomeNumber](n: var T, m: T) {.inline.} = n = min(n, m)
proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)

when isMainModule:
  let N = inputInt()
  var S = newSeqWith(N, newSeq[bool]())
  for i in 0..<N:
    let si = input()
    for sij in si:
      S[i].add(sij == '(')
  
  var
    brackets: seq[tuple[idx: int, a: int, b: int]]
    left, right, a, b: int
  for i, si in S:
    (left, right, a) = (0, 0, 0)
    for sij in si:
      if sij:
        inc left
      else:
        inc right
      a.chmax(right - left)
    (left, right, b) = (0, 0, 0)
    for sij in reversed(si):
      if sij:
        inc left
      else:
        inc right
      b.chmax(left - right)
    brackets.add((i, a, b))
  
  let
    first = brackets.filterIt(it.a <= it.b).sortedByIt(it.a)
    latter = brackets.filterIt(it.a > it.b).sortedByIt(-it.b)
  (left, right) = (0, 0)
  for (idx, n, m) in concat(first, latter):
    let si = S[idx]
    for sij in si:
      if sij:
        inc left
      else:
        inc right
      if left < right:
        echo "No"
        quit()
  echo if left == right: "Yes" else: "No"
