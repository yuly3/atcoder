import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](n: var T, m: T) {.inline.} = n = max(n, m)
proc chmin*[T: SomeNumber](n: var T, m: T) {.inline.} = n = min(n, m)
proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)

proc bitLength(n: Natural): Natural =
  const BIT_SIZE = 24
  if n == 0:
    return 0
  let s = toBin(n, BIT_SIZE)
  return BIT_SIZE - s.find('1')


type
  SegmentTree*[T, K] = ref object
    N0: Positive
    ide_ele: T
    data: seq[T]
    fold: (T, T) -> T
    eval: (T, K) -> T

proc initSegmentTree*[T, K](size: Positive, ide_ele: T, fold: (T, T) -> T, eval: (T, K) -> T): SegmentTree[T, K] =
  let
    N0 = 1 shl bitLength(size - 1)
    data = newSeqWith(2*N0, ide_ele)
  return SegmentTree[T, K](N0: N0, ide_ele: ide_ele, data: data, fold: fold, eval: eval)

proc toSegmentTree*[T, K](init_value: openArray[T], ide_ele: T, fold: (T, T) -> T, eval: (T, K) -> T): SegmentTree[T, K] =
  let N0 = 1 shl bitLength(init_value.len - 1)
  var data = newSeqWith(2*N0, ide_ele)
  for i, x in init_value:
    data[i + N0 - 1] = x
  for i in countdown(N0 - 2, 0):
    data[i] = fold(data[2*i + 1], data[2*i + 2])
  return SegmentTree[T, K](N0: N0, ide_ele: ide_ele, data: data, fold: fold, eval: eval)

proc update*[T, K](self: var SegmentTree[T, K], idx: Natural, x: K) =
  var k = self.N0 - 1 + idx
  self.data[k] = self.eval(self.data[k], x)
  while k != 0:
    k = (k - 1) div 2
    self.data[k] = self.fold(self.data[2*k + 1], self.data[2*k + 2])

proc query*[T, K](self: var SegmentTree[T, K], left, right: Natural): T =
  var
    L = left + self.N0
    R = right + self.N0
    res = self.ide_ele
  
  while L < R:
    if (L and 1) == 1:
      res = self.fold(res, self.data[L - 1])
      inc L
    if (R and 1) == 1:
      dec R
      res = self.fold(res, self.data[R - 1])
    L = L shr 1
    R = R shr 1
  return res

proc `[]`*[T, K](self: var SegmentTree[T, K], k: int): T =
  return self.data[k + self.N0 - 1]

when isMainModule:
  var N, M, Q: int
  (N, M, Q) = inputInts()
  var
    TXY: seq[(int, int, int)]
    ti, xi, yi: int
  for _ in 0..<Q:
    (ti, xi, yi) = inputInts()
    TXY.add((ti, xi - 1, yi))

  var abSet = initHashSet[int]()
  abSet.incl(0)
  for (ti, xi, yi) in TXY:
    abSet.incl(yi)
  var ab = toSeq(abSet)
  ab.sort()

  var abToIdx = initTable[int, int]()
  for i, abi in ab:
    abToIdx[abi] = i
  
  var
    aCntInit = newSeq[int](ab.len)
    bCntInit = newSeq[int](ab.len)
  aCntInit[0] = N
  bCntInit[0] = M

  var
    aCntSegTree = toSegmentTree(aCntInit, 0, (a, b) => a + b, (a, b: int) => a + b)
    aSumSegTree = initSegmentTree(ab.len, 0, (a, b) => a + b, (a, b: int) => a + b)
    bCntSegTree = toSegmentTree(bCntInit, 0, (a, b) => a + b, (a, b: int) => a + b)
    bSumSegTree = initSegmentTree(ab.len, 0, (a, b) => a + b, (a, b: int) => a + b)
    A = newSeq[int](N)
    B = newSeq[int](M)
    ans: seq[int]
    prev_ans = 0
  for (ti, xi, yi) in TXY:
    if ti == 1:
      prev_ans -= bCntSegTree.query(0, abToIdx[A[xi]]) * A[xi]
      prev_ans -= bSumSegTree.query(abToIdx[A[xi]], ab.len)
      prev_ans += bCntSegTree.query(0, abToIdx[yi]) * yi
      prev_ans += bSumSegTree.query(abToIdx[yi], ab.len)
      ans.add(prev_ans)
      aCntSegTree.update(abToIdx[A[xi]], -1)
      aCntSegTree.update(abToIdx[yi], 1)
      aSumSegTree.update(abToIdx[A[xi]], -A[xi])
      aSumSegTree.update(abToIdx[yi], yi)
      A[xi] = yi
    else:
      prev_ans -= aCntSegTree.query(0, abToIdx[B[xi]]) * B[xi]
      prev_ans -= aSumSegTree.query(abToIdx[B[xi]], ab.len)
      prev_ans += aCntSegTree.query(0, abToIdx[yi]) * yi
      prev_ans += aSumSegTree.query(abToIdx[yi], ab.len)
      ans.add(prev_ans)
      bCntSegTree.update(abToIdx[B[xi]], -1)
      bCntSegTree.update(abToIdx[yi], 1)
      bSumSegTree.update(abToIdx[B[xi]], -B[xi])
      bSumSegTree.update(abToIdx[yi], yi)
      B[xi] = yi
  echo ans.join("\n")
