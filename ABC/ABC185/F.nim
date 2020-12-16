import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
  return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
  num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
  num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
  num0 = num0 mod num1

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


var
  A, ans: seq[int]
  seg_tree: SegmentTree[int, int]

proc solve() =
  var N, Q: int
  (N, Q) = input().split.map(parseInt)
  A = input().split.map(parseInt)

  seg_tree = toSegmentTree(A, 0, (a, b) => bitxor(a, b), (a, b: int) => b)

  var ti, xi, yi, ai: int
  for _ in 0..<Q:
    (ti, xi, yi) = input().split.map(parseInt)
    if ti == 1:
      dec xi
      ai = seg_tree.query(xi, xi + 1)
      seg_tree.update(xi, bitxor(ai, yi))
    else:
      dec xi
      ans.add(seg_tree.query(xi, yi))
  echo ans.join("\n")

when is_main_module:
  solve()
