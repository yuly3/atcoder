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

when isMainModule:
  var H, W: int
  (H, W) = inputInts()
  var Q = inputInt()

  var
    uf = initUnionFind(H*W)
    painted: array[4000000, bool]
    ans: seq[string]
    ri, ci, rai, cai, rbi, cbi: int
  for _ in 0..<Q:
    let qi = inputInts()
    if qi[0] == 1:
      (ri, ci) = qi[1..^1].mapIt(it - 1)
      let u = ri*W + ci
      painted[u] = true
      for (dy, dx) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        let (ny, nx) = (ri + dy, ci + dx)
        if 0 <= ny and ny < H and 0 <= nx and nx < W:
          let v = ny*W + nx
          if painted[v]:
            uf.union(u, v)
    else:
      (rai, cai, rbi, cbi) = qi[1..^1].mapIt(it - 1)
      let
        u = rai*W + cai
        v = rbi*W + cbi
      if uf.same(u, v) and painted[u] and painted[v]:
        ans.add("Yes")
      else:
        ans.add("No")
  echo ans.join("\n")
