when not declared ATCODER_YULY3HEADER_HPP:
  const ATCODER_YULY3HEADER_HPP* = 1

  import
    algorithm,
    bitops,
    deques,
    heapqueue,
    math,
    macros,
    sets,
    sequtils,
    strformat,
    strutils,
    sugar,
    tables

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
  proc `|=`*[T: SomeInteger or bool](n: var T, m: T) {.inline.} = n = n or m
  proc `&=`*[T: SomeInteger or bool](n: var T, m: T) {.inline.} = n = n and m
  proc `^=`*[T: SomeInteger or bool](n: var T, m: T) {.inline.} = n = n xor m
  proc `<<=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = n shl m
  proc `>>=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = n shr m

when not declared ATCODER_REROOTING_HPP:
  const ATCODER_REROOTING_HPP* = 1
  
  type RerootingTree[N: static int, T] = object
    tree: array[0..N - 1, seq[int]]
    sz, depth, parent, dp1, dp2, left, right: array[0..N - 1, int]
    order: seq[int]
    op: (T, int, int) -> T
    merge: (T, T) -> T
    ide: T
  
  proc initRerootingTree*[N: static int, T](op: (T, int, int) -> T, merge: (T, T) -> T, ide: T): RerootingTree[N, T] =
    return RerootingTree[N, T](order: newSeq[int](), op: op, merge: merge, ide: ide)
  
  proc addEdge*[N: static int, T](self: var RerootingTree[N, T], u, v: int) =
    self.tree[u].add(v)
    self.tree[v].add(u)
  
  proc topologicalSort*[N: static int, T](self: var RerootingTree[N, T], root: int) =
    self.sz.fill(1)
    self.depth.fill(-1)
    self.depth[root] = 0
    self.order.add(root)
    var stack = @[root]
    while stack.len > 0:
      let cur = stack.pop()
      for to in self.tree[cur]:
        if self.depth[to] != -1:
          continue
        self.parent[to] = cur
        self.depth[to] = self.depth[cur] + 1
        self.order.add(to)
        stack.add(to)
    for fr in reversed(self.order):
      for to in self.tree[fr]:
        if self.parent[fr] == to:
          continue
        self.sz[fr] += self.sz[to]
  
  proc solve*[N: static int, T](self: var RerootingTree[N, T], root=0): array[0..N - 1, T] =
    self.topologicalSort(root)
    self.dp1.fill(self.ide)
    self.dp2.fill(self.ide)
    self.left.fill(self.ide)
    self.right.fill(self.ide)
    
    for fr in reversed(self.order):
      var acc = self.ide
      for to in self.tree[fr]:
        if self.parent[fr] == to:
          continue
        self.left[to] = acc
        acc = self.merge(acc, self.op(self.dp1[to], fr, to))
      acc = self.ide
      for to in reversed(self.tree[fr]):
        if self.parent[fr] == to:
          continue
        self.right[to] = acc
        acc = merge(acc, self.op(self.dp1[to], fr, to))
      self.dp1[fr] = acc
    
    for to in self.order[1..^1]:
      self.dp2[to] = self.merge(self.left[to], self.right[to])
      self.dp2[to] = self.op(self.merge(self.dp2[to], self.dp2[self.parent[to]]), to, self.parent[to])
      self.dp1[to] = self.merge(self.dp1[to], self.dp2[to])
    return self.dp1

when isMainModule:
  var N, M: int
  (N, M) = inputInts()
  
  proc op(v, fr, to: int): int = v + 1
  proc merge(v1, v2: int): int = v1*v2 mod M
  var rerooting = initRerootingTree[100001, int](op, merge, 1)
  
  var xi, yi: int
  for _ in 0..<N - 1:
    (xi, yi) = inputInts().mapIt(it - 1)
    rerooting.addEdge(xi, yi)
  var dp = rerooting.solve()
  echo dp[0..<N].join("\n")
