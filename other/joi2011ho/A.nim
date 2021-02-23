import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string = stdin.readLine
proc inputs*(): seq[string] = stdin.readLine.split
proc inputInt*(): int = stdin.readLine.parseInt
proc inputInts*(): seq[int] = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) = num0 = floorMod(num0, num1)

var
  S: seq[string]
  abcd, accJ, accO, accI: seq[seq[int]]
  ans: seq[string]

proc solve() =
  var M, N: int
  (M, N) = inputInts()
  let K = inputInt()
  S = newSeqWith(M, input())

  accJ = newSeqWith(M + 1, newSeq[int](N + 1))
  accO = newSeqWith(M + 1, newSeq[int](N + 1))
  accI = newSeqWith(M + 1, newSeq[int](N + 1))
  for i in 0..<M:
    for j in 0..<N:
      accJ[i + 1][j + 1] = accJ[i + 1][j]
      accO[i + 1][j + 1] = accO[i + 1][j]
      accI[i + 1][j + 1] = accI[i + 1][j]
      if S[i][j] == 'J':
        inc accJ[i + 1][j + 1]
      elif S[i][j] == 'O':
        inc accO[i + 1][j + 1]
      else:
        inc accI[i + 1][j + 1]
  for i in 0..<M:
    for j in 0..<N:
      accJ[i + 1][j + 1] += accJ[i][j + 1]
      accO[i + 1][j + 1] += accO[i][j + 1]
      accI[i + 1][j + 1] += accI[i][j + 1]
  
  ans = newSeq[string]()
  var a, b, c, d: int
  for _ in 0..<K:
    (a, b, c, d) = inputInts()
    let
      J = accJ[c][d] - accJ[a - 1][d] - accJ[c][b - 1] + accJ[a - 1][b - 1]
      O = accO[c][d] - accO[a - 1][d] - accO[c][b - 1] + accO[a - 1][b - 1]
      I = accI[c][d] - accI[a - 1][d] - accI[c][b - 1] + accI[a - 1][b - 1]
    ans.add(&"{J} {O} {I}")
  echo ans.join("\n")

when is_main_module:
  solve()
