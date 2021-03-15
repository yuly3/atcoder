import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when is_main_module:
  var N, Q: int
  (N, Q) = inputInts()
  let
    X = inputInts()
    W = newSeqWith(Q, inputInt())
  
  if N == 1:
    var left, right, d: int
    for i in 0..<Q:
      d += W[i]
      left.chmin(d)
      right.chmax(d)
    echo right - left
    quit()
  
  var section = newSeq[(int, int)](N - 1)
  for i in 1..<N:
    section[i - 1] = (X[i] - X[i - 1], i - 1)
  section.sort()
  
  var
    ans = newSeq[int](N)
    left, right, cur, i, d: int
  while cur < N - 1:
    while abs(left) + right < section[cur][0] and i < Q:
      d += W[i]
      left.chmin(d)
      right.chmax(d)
      inc i
    let j = section[cur][1]
    if section[cur][0] <= abs(left) + right:
      if W[i - 1] < 0:
        ans[j] += right
        ans[j + 1] += section[cur][0] - right
      else:
        ans[j] += section[cur][0] - abs(left)
        ans[j + 1] += abs(left)
    else:
      ans[j] += right
      ans[j + 1] += abs(left)
    inc cur
  
  for ii in i..<Q:
    d += W[ii]
    left.chmin(d)
    right.chmax(d)
  
  ans[0] += abs(left)
  ans[^1] += right
  echo ans.join("\n")
