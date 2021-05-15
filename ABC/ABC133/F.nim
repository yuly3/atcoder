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

proc bitLength(n: Natural): Natural =
  const BIT_SIZE = 24
  if n == 0:
    return 0
  let s = toBin(n, BIT_SIZE)
  return BIT_SIZE - s.find('1')

when not declared ATCODER_LOWESTCOMMONANCESTOR_HPP:
  const ATCODER_LOWESTCOMMONANCESTOR_HPP* = 1

  type
    LowestCommonAncestor* = ref object
      size: Positive
      LV: Natural
      depth: seq[int]
      tree, parent: seq[seq[int]]

  proc initLowestCommonAncestor*(tree: var seq[seq[int]]): LowestCommonAncestor =
    let
      size = tree.len
      LV = bitLength(size)
      depth = newSeq[int](size)
      parent = newSeqWith(LV, newSeqWith(size, -1))
    return LowestCommonAncestor(size: size, LV: LV, depth: depth, tree: tree, parent: parent)

  proc build*(self: var LowestCommonAncestor, root: Natural) =
    var que = initDeque[(int, int, int)]()
    que.addLast((root, -1, 0))

    var cur, par, dist: int
    while que.len != 0:
      (cur, par, dist) = que.popFirst()
      self.parent[0][cur] = par
      self.depth[cur] = dist
      for child in self.tree[cur]:
        if child != par:
          self.depth[child] = dist + 1
          que.addLast((child, cur, dist + 1))
    
    for i in 1..<self.LV:
      for j in 0..<self.size:
        let k = self.parent[i - 1][j]
        if k != -1:
          self.parent[i][j] = self.parent[i - 1][k]

  proc query*(self: var LowestCommonAncestor, u, v: Natural): int =
    var (u, v) = (u, v)
    if self.depth[v] < self.depth[u]:
      (u, v) = (v, u)
    for i in 0..<self.LV:
      if (((self.depth[v] - self.depth[u]) shr i) and 1) == 1:
        v = self.parent[i][v]
    if u == v:
      return u
    
    for i in countdown(self.LV - 1, 0):
      if self.parent[i][u] != self.parent[i][v]:
        u = self.parent[i][u]
        v = self.parent[i][v]
    return self.parent[0][v]

  proc dist*(self: var LowestCommonAncestor, u, v: Natural): int =
    let ancestor = self.query(u, v)
    return self.depth[u] + self.depth[v] - 2*self.depth[ancestor]

when isMainModule:
  var N, Q: int
  (N, Q) = inputInts()
  var
    ai, bi, ci, di: int
    graph: array[100001, seq[(int, int, int)]]
    tree = newSeqWith(N, newSeq[int]())
  for _ in 0..<N - 1:
    (ai, bi, ci, di) = inputInts()
    ai.dec; bi.dec
    graph[ai].add((bi, ci, di))
    graph[bi].add((ai, ci, di))
    tree[ai].add(bi)
    tree[bi].add(ai)

  var
    distForColor, cntForColor: array[100001, int]
    queries: array[100001, seq[(int, int, int, int)]]
    ans = newSeq[int](Q)
  
  proc dfs(cur, par, distSum: int) =
    for (idx, color, length, coef) in queries[cur]:
      ans[idx] += coef*(distSum - distForColor[color] + cntForColor[color]*length)
    
    for (to, ci, di) in graph[cur]:
      if to == par:
        continue
      distForColor[ci] += di
      cntForColor[ci].inc
      dfs(to, cur, distSum + di)
      cntForColor[ci].dec
      distForColor[ci] -= di
  
  
  var lca = initLowestCommonAncestor(tree)
  lca.build(0)
  var xi, yi, ui, vi: int
  for i in 0..<Q:
    (xi, yi, ui, vi) = inputInts()
    ui.dec; vi.dec
    queries[ui].add((i, xi, yi, 1))
    queries[vi].add((i, xi, yi, 1))
    queries[lca.query(ui, vi)].add((i, xi, yi, -2))
  
  dfs(0, -1, 0)
  echo ans.join("\n")
