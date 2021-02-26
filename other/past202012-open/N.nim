import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

proc bit_length(n: Natural): Natural =
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
    N0 = 1 shl bit_length(size - 1)
    data = newSeqWith(2*N0, ide_ele)
  return SegmentTree[T, K](N0: N0, ide_ele: ide_ele, data: data, fold: fold, eval: eval)

proc toSegmentTree*[T, K](init_value: openArray[T], ide_ele: T, fold: proc (a, b: T): T, eval: proc (a: T, b: K): T): SegmentTree[T, K] =
  let N0 = 1 shl bit_length(init_value.len - 1)
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

proc binarySearchRight*[T, K](self: var SegmentTree[T, K], left, right: Natural, x: T): int =
  return self.binarySearchRightSub(left, right, x, 0, 0, self.N0)

proc binarySearchRightSub*[T, K](self: var SegmentTree[T, K], a, b: Natural, x: T, k, left, right: Natural): int =
  if x < self.data[k] or right <= a or b <= left:
    return a - 1
  if self.N0 - 1 <= k:
    return k - self.N0 + 1
  let vr = self.binarySearchRightSub(a, b, x, 2*k + 2, (left + right) div 2, right)
  if vr != a - 1:
    return vr
  return self.binarySearchRightSub(a, b, x, 2*k + 1, left, (left + right) div 2)

proc binarySearchLeft*[T, K](self: var SegmentTree[T, K], left, right: Natural, x: T): int =
  return self.binarySearchLeftSub(left, right, x, 0, 0, self.N0)

proc binarySearchLeftSub*[T, K](self: var SegmentTree[T, K], a, b: Natural, x: T, k, left, right: Natural): int =
  if x < self.data[k] or right <= a or b <= left:
    return b
  if self.N0 - 1 <= k:
    return k - self.N0 + 1
  let vl = self.binarySearchLeftSub(a, b, x, 2*k + 1, left, (left + right) div 2)
  if vl != b:
    return vl
  return self.binarySearchLeftSub(a, b, x, 2*k + 2, (left + right) div 2, right)


when is_main_module:
  var N, Q: int
  (N, Q) = inputInts()
  var
    events = newSeq[(int, int, int, int)]()
    L, R, A, B: int
  for i in 0..<N - 1:
    (L, R) = inputInts()
    events.add((L, 1, i + 1, 0))
    events.add((R + 1, 0, i + 1, 0))
  for i in 0..<Q:
    (A, B) = inputInts()
    events.add((A, 2, B, i))
  events.sort()

  var
    segTree = toSegmentTree(newSeq[int](N + 1), 1, (a, b) => min(a, b), (a, b: int) => b)
    ans = newSeqWith(Q, 1)
  for (age, cmd, pos, idx) in events:
    if cmd == 0:
      segTree.update(pos, 0)
    elif cmd == 1:
      segTree.update(pos, 1)
    else:
      if segTree[pos] != 0:
        let rightEnd = segTree.binarySearchLeft(pos, N, 0)
        ans[idx] += rightEnd - pos
      if segTree[pos - 1] != 0:
        let leftEnd = segTree.binarySearchRight(0, pos, 0) + 1
        ans[idx] += pos - leftEnd
  echo ans.join("\n")
