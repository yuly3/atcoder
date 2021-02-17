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

proc `[]`*[T, K](self: var SegmentTree[T, K], k: int): T =
  return self.data[k + self.N0 - 1]


var
  L, R, A, B, ans: seq[int]
  events: seq[(int, int, int, int)]
  seg_tree: SegmentTree[int, int]

proc solve() =
  var N, Q: int
  (N, Q) = input().split.map(parseInt)
  (L, R) = (newSeq[int](N - 1), newSeq[int](N - 1))
  for i in 0..<N - 1:
    (L[i], R[i]) = input().split.map(parseInt)
  (A, B) = (newSeq[int](Q), newSeq[int](Q))
  for i in 0..<Q:
    (A[i], B[i]) = input().split.map(parseInt)

  events = newSeq[(int, int, int, int)]()
  for i, li in L:
    events.add((li, 1, i + 1, 0))
  for i, ri in R:
    events.add((ri + 1, 0, i + 1, 0))
  for i, (ai, bi) in zip(A, B):
    events.add((ai, 2, bi, i))
  events.sort()
  
  seg_tree = toSegmentTree(newSeqWith(N + 1, 1), 0, (a, b) => max(a, b), (a, b: int) => b)
  ans = newSeq[int](Q)
  for (age, cmd, pos, idx) in events:
    if cmd == 0:
      seg_tree.update(pos, 1)
    elif cmd == 1:
      seg_tree.update(pos, 0)
    else:
      var right_end, left_end, ok, ng, mid: int
      if seg_tree[pos] == 1:
        right_end = -1
      else:
        (ok, ng) = (pos, N)
        while 1 < ng - ok:
          mid = (ok + ng) div 2
          if seg_tree.query(pos, mid + 1) == 0:
            ok = mid
          else:
            ng = mid
        right_end = ok
      if seg_tree[pos - 1] == 1:
        left_end = -1
      else:
        (ng, ok) = (0, pos - 1)
        while 1 < ok - ng:
          mid = (ok + ng) div 2
          if seg_tree.query(mid, pos) == 0:
            ok = mid
          else:
            ng = mid
        left_end = ok
      
      if right_end != -1:
        ans[idx] += right_end - pos + 1
      if left_end != -1:
        ans[idx] += pos - left_end
      inc ans[idx]
  echo ans.join("\n")

when is_main_module:
  solve()
