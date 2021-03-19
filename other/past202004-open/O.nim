import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)


type
  UnionFind* = ref object
    n: Positive
    parents: seq[int]

proc initUnionFind*(n: Positive): UnionFind =
  return UnionFind(n: n, parents: newSeqWith(n, -1))

proc find*(self: var UnionFind, x: Natural): Natural =
  if self.parents[x] < 0:
    return x
  else:
    self.parents[x] = self.find(self.parents[x])
    return self.parents[x]

proc union*(self: var UnionFind, x, y: Natural) =
  var
    root_x = self.find(x)
    root_y = self.find(y)
  
  if root_x == root_y:
    return
  if self.parents[root_y] < self.parents[root_x]:
    (root_x, root_y) = (root_y, root_x)
  self.parents[root_x] += self.parents[root_y]
  self.parents[root_y] = root_x

proc size*(self: var UnionFind, x: Natural): Positive =
  return -self.parents[self.find(x)]

proc same*(self: var UnionFind, x, y: Natural): bool =
  return self.find(x) == self.find(y)

proc members*(self: var UnionFind, x: Natural): seq[int] =
  let root = self.find(x)
  return toSeq(0..<int(self.n)).filterIt(self.find(it) == root)

proc roots*(self: var UnionFind): seq[int] =
  return toSeq(0..<int(self.n)).filterIt(self.parents[it] < 0)

proc group_count*(self: var UnionFind): Positive =
  return self.roots.len


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


when is_main_module:
  var N, M: int
  (N, M) = inputInts()
  var
    edges = newSeq[(int, int, int, int)]()
    ai, bi, ci: int
  for i in 0..<M:
    (ai, bi, ci) = inputInts()
    edges.add((ai - 1, bi - 1, ci, i))
  let sortedEdges = edges.sortedByIt(it[2])

  var
    uf = initUnionFind(N)
    usedEdge = initHashSet[(int, int, int, int)]()
    minCost, edgeCnt: int
  for (u, v, w, i) in sortedEdges:
    if not uf.same(u, v):
      uf.union(u, v)
      usedEdge.incl((u, v, w, i))
      minCost += w
      inc edgeCnt
      if edgeCnt == N - 1:
        break
  
  var hld = initHeavyLightDecomposition(N)
  for (u, v, w, i) in usedEdge.items:
    hld.addEdge(u, v)
  hld.build(0)
  
  var initVal = newSeq[int](N)
  for (u, v, w, i) in usedEdge.items:
    initVal[max(hld.id(u), hld.id(v))] = w
  
  var
    segTree = toSegmentTree(initVal, 0, (a, b) => max(a, b), (a, b: int) => b)
    ans = newSeq[int](M)
  for edge in edges:
    if edge in usedEdge:
      ans[edge[3]] = minCost
    else:
      let (u, v, w, i) = edge
      var maxC = 0
      for (left, right) in hld.path(u, v, true):
        maxC.chmax(segTree.query(left, right))
      ans[i] = minCost - maxC + w
  echo ans.join("\n")
