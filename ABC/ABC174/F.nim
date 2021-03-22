import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)


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
    fold: proc (a, b: T): T
    eval: proc (a: T, b: K): T

proc initSegmentTree*[T, K](size: Positive, ide_ele: T, fold: proc (a, b: T): T, eval: proc (a: T, b: K): T): SegmentTree[T, K] =
  let
    N0 = 1 shl bitLength(size - 1)
    data = newSeqWith(2*N0, ide_ele)
  return SegmentTree[T, K](N0: N0, ide_ele: ide_ele, data: data, fold: fold, eval: eval)

proc toSegmentTree*[T, K](init_value: openArray[T], ide_ele: T, fold: proc (a, b: T): T, eval: proc (a: T, b: K): T): SegmentTree[T, K] =
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


when is_main_module:
  var N, Q: int
  (N, Q) = inputInts()
  var c = inputInts()
  c.applyIt(it - 1)
  
  var
    queries = newSeq[(int, int, int)]()
    left, right: int
  for i in 0..<Q:
    (left, right) = inputInts()
    queries.add((i, left - 1, right))
  queries.sort((a, b) => cmp(a[2], b[2]))

  var
    cToIdx: array[5*10^5, int]
    segTree = initSegmentTree(N, 0, (a, b) => a + b, (a, b: int) => b)
    ans = newSeq[int](Q)
    prevRight: int
  
  cToIdx.fill(-1)
  for (i, left, right) in queries:
    for j in prevRight..<right:
      if cToIdx[c[j]] != -1:
        segTree.update(cToIdx[c[j]], 0)
      cToIdx[c[j]] = j
      segTree.update(j, 1)
    ans[i] = segTree.query(left, right)
    prevRight = right
  echo ans.join("\n")
