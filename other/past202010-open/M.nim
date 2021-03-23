import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)


type
  HeavyLightDecomposition* = ref object
    graph: seq[seq[Natural]]
    pathRoot, pathParent, left, right: seq[Natural]

proc initHeavyLightDecomposition*(size: Positive): HeavyLightDecomposition =
  var
    graph = newSeqWith(size, newSeq[Natural]())
    emptySeq = newSeq[Natural]()
  return HeavyLightDecomposition(graph: graph, pathRoot: emptySeq, pathParent: emptySeq, left: emptySeq, right: emptySeq)

proc addEdge*(self: var HeavyLightDecomposition, a, b: Natural) =
  self.graph[a].add(b)
  self.graph[b].add(a)

proc build*(self: var HeavyLightDecomposition, root: Natural) =
  var
    stack = @[(root, root)]
    q = newSeq[Natural]()
    v, p: Natural
  
  while stack.len != 0:
    (v, p) = stack.pop()
    q.add(v)
    for i, to in self.graph[v]:
      if to == p:
        self.graph[v][i] = self.graph[v][^1]
        let _ = self.graph[v].pop()
        break
    for to in self.graph[v]:
      stack.add((to, v))
  
  let n = self.graph.len
  var size = newSeqWith(n, 1)
  for v in reversed(q):
    for i, to in self.graph[v]:
      size[v] += size[to]
      if size[self.graph[v][0]] < size[to]:
        (self.graph[v][0], self.graph[v][i]) = (self.graph[v][i], self.graph[v][0])
  
  self.pathRoot = newSeqWith(n, root)
  self.pathParent = newSeqWith(n, root)
  self.left = newSeq[Natural](n)
  self.right = newSeq[Natural](n)
  var
    k = 0
    stack1 = @[(root, 0)]
    op: int
    to: Natural
  while stack1.len != 0:
    (v, op) = stack1.pop()
    if op == 1:
      self.right[v] = k
      continue
    self.left[v] = k
    inc k
    stack1.add((v, 1))
    if 1 < self.graph[v].len:
      for i, to in self.graph[v][1..^1]:
        self.pathRoot[to] = to
        self.pathParent[to] = v
        stack1.add((to, 0))
    if self.graph[v].len != 0:
      to = self.graph[v][0]
      self.pathRoot[to] = self.pathRoot[v]
      self.pathParent[to] = self.pathParent[v]
      stack1.add((to, 0))

proc subTree*(self: var HeavyLightDecomposition, v: Natural): (Natural, Natural) =
  return (self.left[v], self.right[v])

proc path*(self: var HeavyLightDecomposition, v, u: Natural, edgeFlg: bool=false): seq[(int, int)] =
  var
    x = v
    y = u
    res = newSeq[(int, int)]()
    p: Natural
  while self.pathRoot[x] != self.pathRoot[y]:
    if self.left[x] < self.left[y]:
      p = self.pathRoot[y]
      res.add((self.left[p], self.left[y] + 1))
      y = self.pathParent[y]
    else:
      p = self.pathRoot[x]
      res.add((self.left[p], self.left[x] + 1))
      x = self.pathParent[x]
  if edgeFlg:
    res.add((min(self.left[x], self.left[y]) + 1, max(self.left[x], self.left[y]) + 1))
  else:
    res.add((min(self.left[x], self.left[y]), max(self.left[x], self.left[y]) + 1))
  return res

proc id*(self: var HeavyLightDecomposition, v: Natural): Natural =
  return self.left[v]


proc bitLength(n: Natural): Natural =
  const BIT_SIZE = 24
  if n == 0:
    return 0
  let s = toBin(n, BIT_SIZE)
  return BIT_SIZE - s.find('1')


type
  DualSegmentTree*[T] = ref object
    LV: Natural
    N0: Positive
    lazy_ide_ele: T
    lazy_data: seq[T]
    merge: (T, T) -> T
    propagatesWhenUpdating: bool

proc initDualSegmentTree*[T](size: Positive, lazy_ide_ele: T, merge: (T, T) -> T, propagatesWhenUpdating=false): DualSegmentTree[T] =
  let
    LV = bitLength(size - 1)
    N0 = 1 shl LV
    lazy_data = newSeqWith(2*N0, lazy_ide_ele)
  return DualSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: lazy_data, merge: merge, propagatesWhenUpdating: propagatesWhenUpdating)

proc toDualSegmentTree*[T](init_value: openArray[T], lazy_ide_ele: T, merge: (T, T) -> T, propagatesWhenUpdating=false): DualSegmentTree[T] =
  let
    LV = bitLength(init_value.len - 1)
    N0 = 1 shl LV
  var lazy_data = newSeqWith(2*N0, lazy_ide_ele)
  for i, x in init_value:
    lazy_data[i + N0 - 1] = x
  return DualSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: lazy_data, merge: merge, propagatesWhenUpdating: propagatesWhenUpdating)

iterator gindex*[T](self: var DualSegmentTree[T], left, right: Natural): Natural =
  var
    L = (left + self.N0) shr 1
    R = (right + self.N0) shr 1
    lc = if (left and 1) == 1: 0 else: bitLength(L and -L)
    rc = if (right and 1) == 1: 0 else: bitLength(R and -R)
  for i in 0..<self.LV:
    if rc <= i:
      yield R
    if L < R and lc <= i:
      yield L
    L = L shr 1
    R = R shr 1

proc propagates*[T](self: var DualSegmentTree[T], ids: seq[Natural]) =
  var
    idx: Natural
    v: T
  for id in reversed(ids):
    idx = id - 1
    v = self.lazy_data[idx]
    if v == self.lazy_ide_ele:
        continue
    self.lazy_data[2*idx + 1] = self.merge(self.lazy_data[2*idx + 1], v)
    self.lazy_data[2*idx + 2] = self.merge(self.lazy_data[2*idx + 2], v)
    self.lazy_data[idx] = self.lazy_ide_ele

proc update*[T](self: var DualSegmentTree[T], left, right: Natural, x: T) =
  if self.propagatesWhenUpdating:
    self.propagates(toSeq(self.gindex(left, right)))
  var
    L = left + self.N0
    R = right + self.N0
  
  while L < R:
    if (L and 1) == 1:
      self.lazy_data[L - 1] = self.merge(self.lazy_data[L - 1], x)
      inc L
    if (R and 1) == 1:
      dec R
      self.lazy_data[R - 1] = self.merge(self.lazy_data[R - 1], x)
    L = L shr 1
    R = R shr 1

proc `[]`*[T](self: var DualSegmentTree[T], k: Natural): T =
  self.propagates(toSeq(self.gindex(k, k + 1)))
  return self.lazy_data[k + self.N0 - 1]


when is_main_module:
  var N, Q: int
  (N, Q) = inputInts()
  var
    edges = newSeq[(int, int)]()
    hld = initHeavyLightDecomposition(N)
    ai, bi: int
  for _ in 0..<N - 1:
    (ai, bi) = inputInts()
    dec ai; dec bi
    edges.add((ai, bi))
    hld.addEdge(ai, bi)
  hld.build(0)

  var
    colors = toDualSegmentTree(newSeq[int](N), -1, (a, b) => b, true)
    ui, vi, ci: int
  for _ in 0..<Q:
    (ui, vi, ci) = inputInts()
    dec ui; dec vi
    for (left, right) in hld.path(ui, vi, true):
      colors.update(left, right, ci)
  
  var ans = newSeq[int](N - 1)
  for i, (ai, bi) in edges:
    ans[i] = colors[max(hld.id(ai), hld.id(bi))]
  echo ans.join("\n")
