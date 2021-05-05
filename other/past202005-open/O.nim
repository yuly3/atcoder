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

when not declared ATCODER_MINCOSTFLOW_HPP:
  const ATCODER_MINCOSTFLOW_HPP* = 1

  type Edge*[Cap, Cost] = object
    dst, rev: int
    cap: Cap
    cost: Cost
  
  type MCFGraph*[Cap, Cost] = object
    n: int
    pos: seq[(int, int)]
    g: seq[seq[Edge[Cap, Cost]]]
  
  type EdgeInfo*[Cap, Cost] = object
    src*, dst*: int
    cap*, flow*: Cap
    cost*: Cost
  
  proc initMCFGraph*[Cap, Cost](n: int): auto =
    MCFGraph[Cap, Cost](n: n, g: newSeq[seq[Edge[Cap, Cost]]](n))

  proc addEdge*[Cap, Cost](self: var MCFGraph[Cap, Cost], src, dst: int, cap: Cap, cost: Cost): int {.discardable.} =
    let m = self.pos.len
    self.pos.add((src, self.g[src].len))
    var
      srcId = self.g[src].len
      dstId = self.g[dst].len
    if src == dst: dstId.inc
    self.g[src].add(Edge[Cap, Cost](dst: dst, rev: dstId, cap: cap, cost: cost))
    self.g[dst].add(Edge[Cap, Cost](dst: src, rev: srcId, cap: Cap(0), cost: -cost))
    return m

  proc getEdge*[Cap, Cost](self: MCFGraph[Cap, Cost], i: int): EdgeInfo[Cap, Cost] =
    let
      e = self.g[self.pos[i][0]][self.pos[i][1]]
      re = self.g[e.dst][e.rev]
    return EdgeInfo[Cap, Cost](src: self.pos[i][0], dst: e.dst, cap: e.cap + re.cap, flow: re.cap, cost: e.cost)

  proc edges*[Cap, Cost](self: MCFGraph[Cap, Cost]): seq[EdgeInfo[Cap, Cost]] =
    let m = self.pos.len
    result = newSeq[EdgeInfo[Cap, Cost]](m)
    for i in 0..<m:
      result[i] = self.getEdge(i)
  
  proc slope*[Cap, Cost](self: var MCFGraph[Cap, Cost], s, t: int, flowLimit: Cap): seq[(Cap, Cost)] =
    var
      dual = newSeqWith(self.n, Cost(0))
      dist = newSeq[Cost](self.n)
      pv, pe = newSeq[int](self.n)
      vis = newSeq[bool](self.n)
    
    proc dualRef(self: var MCFGraph[Cap, Cost]): bool =
      dist.fill(Cost.high)
      pv.fill(-1)
      pe.fill(-1)
      vis.fill(false)

      type Q = tuple[key: Cost, dst: int]
      proc `<`(l, r: Q): bool = l.key < r.key

      var que = initHeapQueue[Q]()
      dist[s] = 0
      que.push((Cost(0), s))
      while que.len > 0:
        let v = que.pop().dst
        if vis[v]: continue
        vis[v] = true
        if v == t: break

        for i in 0..<self.g[v].len:
          let e = self.g[v][i]
          if vis[e.dst] or e.cap == 0: continue
          let cost = e.cost - dual[e.dst] + dual[v]
          if dist[e.dst] - dist[v] > cost:
            dist[e.dst] = dist[v] + cost
            pv[e.dst] = v
            pe[e.dst] = i
            que.push((dist[e.dst], e.dst))
      if not vis[t]:
        return false

      for v in 0..<self.n:
        if not vis[v]: continue
        dual[v] -= dist[t] - dist[v]
      return true

    var
      flow = Cap(0)
      cost = Cost(0)
      prevCostPerFlow = -1
    result = newSeq[(Cap, Cost)]()
    result.add((flow, cost))
    while flow < flowLimit:
      if not self.dualRef(): break
      var
        c = flowLimit - flow
        v = t
      while v != s:
        c = min(c, self.g[pv[v]][pe[v]].cap)
        v = pv[v]
      v = t
      while v != s:
        var e = self.g[pv[v]][pe[v]].addr
        e[].cap -= c
        self.g[v][e[].rev].cap += c
        v = pv[v]
      let d = -dual[s]
      flow += c
      cost += c*d
      if prevCostPerFlow == d:
        discard result.pop()
      result.add((flow, cost))
      prevCostPerFlow = cost
  
  proc flow*[Cap, Cost](self: var MCFGraph[Cap, Cost], s, t: int, flowLimit: Cap): (Cap, Cost) =
    self.slope(s, t, flowLimit)[^1]
  proc flow*[Cap, Cost](self: var MCFGraph[Cap, Cost], s, t: int): (Cap, Cost) =
    self.flow(s, t, Cap.high)
  proc slope*[Cap, Cost](self: var MCFGraph[Cap, Cost], s, t: int): seq[(Cap, Cost)] =
    self.slope(s, t, Cap.high)

when isMainModule:
  var N, M: int
  (N, M) = inputInts()
  var
    A = inputInts()
    B = inputInts()
    R = inputInts()
  
  let
    (r1, r2, r3) = (N, N + 1, N + 2)
    (S, T) = (N + 3, N + 4)
  var mcfg = initMCFGraph[int, int](N + 5)
  const BIG = 10^5
  
  mcfg.addEdge(S, r1, M, 0)
  mcfg.addEdge(S, r2, M, 0)
  mcfg.addEdge(S, r3, M, 0)
  for j in 0..<N:
    mcfg.addEdge(r1, j, 1, BIG - (A[j]*B[j] mod R[0]))
    mcfg.addEdge(r2, j, 1, BIG - (A[j]*B[j]^2 mod R[1]))
    mcfg.addEdge(r3, j, 1, BIG - (A[j]*B[j]^3 mod R[2]))

    mcfg.addEdge(j, T, 1, A[j]*B[j])
    mcfg.addEdge(j, T, 1, A[j]*B[j]^2 - A[j]*B[j])
    mcfg.addEdge(j, T, 1, A[j]*B[j]^3 - A[j]*B[j]^2)
  
  var (_, cost) = mcfg.flow(S, T, 3*M)
  echo 3*M*BIG - cost
