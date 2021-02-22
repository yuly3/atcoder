import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string = stdin.readLine
proc inputs*(): seq[string] = stdin.readLine.split
proc inputInt*(): int = stdin.readLine.parseInt
proc inputInts*(): seq[int] = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) = num0 = floorMod(num0, num1)

var
  A, B, L, R: seq[int]

proc solve() =
  let N = inputInt()
  A = inputInts()

  B = newSeq[int](N - 1)
  for i in 0..<N - 1:
    B[i] = A[i + 1] - A[i]
  
  L = newSeq[int](N)
  for i in 1..<N:
    L[i] = L[i - 1] + max(1 - B[i - 1], 0)
  R = newSeq[int](N + 1)
  for i in countdown(N - 1, 1):
    R[i] = R[i + 1] + max(1 + B[i - 1], 0)
  
  var ans = 10^18
  for i in 1..N:
    ans.chmin(max(L[i - 1], R[i]))
  echo ans

when is_main_module:
  solve()
