import
  algorithm, bitops, deques, heapqueue, math, macros, sets, sequtils,
  strformat, strutils, sugar, tables

proc transLastStmt(n, res, bracketExpr: NimNode): (NimNode, NimNode, NimNode) =
  # Looks for the last statement of the last statement, etc...
  case n.kind
  of nnkIfExpr, nnkIfStmt, nnkTryStmt, nnkCaseStmt:
    result[0] = copyNimTree(n)
    result[1] = copyNimTree(n)
    result[2] = copyNimTree(n)
    for i in ord(n.kind == nnkCaseStmt)..<n.len:
      (result[0][i], result[1][^1], result[2][^1]) = transLastStmt(n[i], res, bracketExpr)
  of nnkStmtList, nnkStmtListExpr, nnkBlockStmt, nnkBlockExpr, nnkWhileStmt,
      nnkForStmt, nnkElifBranch, nnkElse, nnkElifExpr, nnkOfBranch, nnkExceptBranch:
    result[0] = copyNimTree(n)
    result[1] = copyNimTree(n)
    result[2] = copyNimTree(n)
    if n.len >= 1:
      (result[0][^1], result[1][^1], result[2][^1]) = transLastStmt(n[^1], res, bracketExpr)
  of nnkTableConstr:
    result[1] = n[0][0]
    result[2] = n[0][1]
    if bracketExpr.len == 1:
      bracketExpr.add([newCall(bindSym"typeof", newEmptyNode()), newCall(
          bindSym"typeof", newEmptyNode())])
    template adder(res, k, v) = res[k] = v
    result[0] = getAst(adder(res, n[0][0], n[0][1]))
  of nnkCurly:
    result[2] = n[0]
    if bracketExpr.len == 1:
      bracketExpr.add(newCall(bindSym"typeof", newEmptyNode()))
    template adder(res, v) = res.incl(v)
    result[0] = getAst(adder(res, n[0]))
  else:
    result[2] = n
    if bracketExpr.len == 1:
      bracketExpr.add(newCall(bindSym"typeof", newEmptyNode()))
    template adder(res, v) = res.add(v)
    result[0] = getAst(adder(res, n))

macro collect*(init, body: untyped): untyped =
  runnableExamples:
    import sets, tables
    let data = @["bird", "word"]
    ## seq:
    let k = collect(newSeq):
      for i, d in data.pairs:
        if i mod 2 == 0: d
    assert k == @["bird"]
    ## seq with initialSize:
    let x = collect(newSeqOfCap(4)):
      for i, d in data.pairs:
        if i mod 2 == 0: d
    assert x == @["bird"]
    ## HashSet:
    let y = initHashSet.collect:
      for d in data.items: {d}
    assert y == data.toHashSet
    ## Table:
    let z = collect(initTable(2)):
      for i, d in data.pairs: {i: d}
    assert z == {0: "bird", 1: "word"}.toTable
  
  let res = genSym(nskVar, "collectResult")
  expectKind init, {nnkCall, nnkIdent, nnkSym}
  let bracketExpr = newTree(nnkBracketExpr,
    if init.kind == nnkCall: init[0] else: init)
  let (resBody, keyType, valueType) = transLastStmt(body, res, bracketExpr)
  if bracketExpr.len == 3:
    bracketExpr[1][1] = keyType
    bracketExpr[2][1] = valueType
  else:
    bracketExpr[1][1] = valueType
  let call = newTree(nnkCall, bracketExpr)
  if init.kind == nnkCall:
    for i in 1 ..< init.len:
      call.add init[i]
  result = newTree(nnkStmtListExpr, newVarStmt(res, call), resBody, res)

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](n: var T, m: T) {.inline.} = n = max(n, m)
proc chmin*[T: SomeNumber](n: var T, m: T) {.inline.} = n = min(n, m)
proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)

when not declared ATCODER_UNIONFIND_HPP:
  const ATCODER_UNIONFIND_HPP* = 1

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

  proc groupCount*(self: var UnionFind): Positive =
    return self.roots.len

when not declared ATCODER_HLDECOMPOSITION_HPP:
  const ATCODER_HLDECOMPOSITION_HPP* = 1

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

when not declared ATCODER_INTERNAL_BITOP_HPP:
  const ATCODER_INTERNAL_BITOP_HPP* = 1

  proc ceil_pow2*(n:SomeInteger):int =
    var x = 0
    while (1.uint shl x) < n.uint: x.inc
    return x
  
  proc bsf*(n:SomeInteger):int =
    return countTrailingZeroBits(n)

when not declared ATCODER_SEGTREE_HPP:
  const ATCODER_SEGTREE_HPP* = 1

  type SegTree*[S; p:static[tuple]] = object
    n, size, log:int
    d: seq[S]

  template calc_op[ST:SegTree](self:typedesc[ST], a, b:ST.S):auto =
    block:
      let op = ST.p.op
      op(a, b)
  template calc_e[ST:SegTree](self:typedesc[ST]):auto =
    block:
      let e = ST.p.e
      e()
  proc update[ST:SegTree](self: var ST, k:int) {.inline.} =
    self.d[k] = ST.calc_op(self.d[2 * k], self.d[2 * k + 1])

  proc init*[ST:SegTree](self: var ST, v:seq[ST.S]) =
    let
      n = v.len
      log = ceil_pow2(n)
      size = 1 shl log
    (self.n, self.size, self.log) = (n, size, log)
    if self.d.len < 2 * size:
      self.d = newSeqWith(2 * size, ST.calc_e())
    else:
      self.d.fill(0, 2 * size - 1, ST.calc_e())
    for i in 0..<n: self.d[size + i] = v[i]
    for i in countdown(size - 1, 1): self.update(i)
  proc init*[ST:SegTree](self: var ST, n:int) =
    self.init(newSeqWith(n, ST.calc_e()))
  proc init*[ST:SegTree](self: typedesc[ST], v:seq[ST.S]):auto =
    result = ST()
    result.init(v)
  proc init*[ST:SegTree](self: typedesc[ST], n:int):auto =
    self.init(newSeqWith(n, ST.calc_e()))
  template getType*(ST:typedesc[SegTree], S:typedesc, op0:static[(S,S)->S], e0:static[()->S]):typedesc[SegTree] =
    SegTree[S, (op:op0, e:e0)]
  template SegTreeType*(S:typedesc, op0:static[(S,S)->S], e0:static[()->S]):typedesc[SegTree] =
    SegTree[S, (op:op0, e:e0)]
  proc initSegTree*[S](v:seq[S], op:static[(S,S)->S], e:static[()->S]):auto =
    SegTreeType(S, op, e).init(v)
  proc initSegTree*[S](n:int, op:static[(S,S)->S], e:static[()->S]):auto =
    result = SegTreeType(S, op, e)()
    result.init(newSeqWith(n, result.type.calc_e()))

  proc set*[ST:SegTree](self:var ST, p:int, x:ST.S) {.inline.} =
    assert p in 0..<self.n
    var p = p + self.size
    self.d[p] = x
    for i in 1..self.log: self.update(p shr i)

  proc get*[ST:SegTree](self:ST, p:int):ST.S {.inline.} =
    assert p in 0..<self.n
    return self.d[p + self.size]

  proc prod*[ST:SegTree](self:ST, p:Slice[int]):ST.S {.inline.} =
    var (l, r) = (p.a, p.b + 1)
    assert 0 <= l and l <= r and r <= self.n
    var
      sml, smr = ST.calc_e()
    l += self.size; r += self.size
    while l < r:
      if (l and 1) != 0: sml = ST.calc_op(sml, self.d[l]);l.inc
      if (r and 1) != 0: r.dec;smr = ST.calc_op(self.d[r], smr)
      l = l shr 1
      r = r shr 1
    return ST.calc_op(sml, smr)
  proc `[]`*[ST:SegTree](self:ST, p:int):auto {.inline.} = self.get(p)
  proc `[]`*[ST:SegTree](self:ST, p:Slice[int]):auto {.inline.} = self.prod(p)
  proc `[]=`*[ST:SegTree](self:var ST, p:int, x:ST.S) {.inline.} = self.set(p, x)

  proc all_prod*[ST:SegTree](self:ST):ST.S = self.d[1]

  proc max_right*[ST:SegTree](self:ST, l:int, f:proc(s:ST.S):bool):int =
    assert l in 0..self.n
    assert f(ST.calc_e())
    if l == self.n: return self.n
    var
      l = l + self.size
      sm = ST.calc_e()
    while true:
      while l mod 2 == 0: l = l shr 1
      if not f(ST.calc_op(sm, self.d[l])):
        while l < self.size:
          l = (2 * l)
          if f(ST.calc_op(sm, self.d[l])):
            sm = ST.calc_op(sm, self.d[l])
            l.inc
        return l - self.size
      sm = ST.calc_op(sm, self.d[l])
      l.inc
      if not ((l and -l) != l): break
    return self.n

  proc min_left*[ST:SegTree](self:ST, r:int, f:proc(s:ST.S):bool):int =
    assert r in 0..self.n
    assert f(ST.calc_e())
    if r == 0: return 0
    var
      r = r + self.size
      sm = ST.calc_e()
    while true:
      r.dec
      while r > 1 and (r mod 2 != 0): r = r shr 1
      if not f(ST.calc_op(self.d[r], sm)):
        while r < self.size:
          r = (2 * r + 1)
          if f(ST.calc_op(self.d[r], sm)):
            sm = ST.calc_op(self.d[r], sm)
            r.dec
        return r + 1 - self.size
      sm = ST.calc_op(self.d[r], sm)
      if not ((r and -r) != r): break
    return 0

when is_main_module:
  var N, M, ai, bi, ci: int
  (N, M) = inputInts()
  let edges = collect(newSeq):
    for i in 0..<M: (ai, bi, ci) = inputInts(); (ai - 1, bi - 1, ci, i)
  let sortedEdges = edges.sortedByIt(it[2])

  var
    uf = initUnionFind(N)
    usedEdge = initHashSet[int]()
    minCost, edgeCnt: int
  for (u, v, w, i) in sortedEdges:
    if not uf.same(u, v):
      uf.union(u, v)
      usedEdge.incl(i)
      minCost += w
      inc edgeCnt
      if edgeCnt == N - 1:
        break
  
  var hld = initHeavyLightDecomposition(N)
  for i in usedEdge:
    hld.addEdge(edges[i][0], edges[i][1])
  hld.build(0)
  
  var initVal = newSeq[int](N)
  for i in usedEdge:
    initVal[max(hld.id(edges[i][0]), hld.id(edges[i][1]))] = edges[i][2]
  
  var
    segTree = initSegTree(initVal, (a: int, b: int) => max(a, b), () => 0)
    ans = newSeq[int](M)
  for (u, v, w, i) in edges:
    if i in usedEdge:
      ans[i] = minCost
    else:
      var maxC = 0
      for (left, right) in hld.path(u, v, true):
        maxC.chmax(segTree[left..<right])
      ans[i] = minCost - maxC + w
  echo ans.join("\n")
