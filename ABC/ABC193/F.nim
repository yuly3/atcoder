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

when not declared ATCODER_INTERNAL_QUEUE_HPP:
  const ATCODER_INTERNAL_QUEUE_HPP* = 1

  type simpleQueue[T] = object
    payload: seq[T]
    pos: int
  
  proc initSimpleQueue*[T](): auto = simpleQueue[T](payload: newSeq[T](), pos:0)
  proc len*[T](self: simpleQueue[T]): int = self.payload.len - self.pos
  proc empty*[T](self: simpleQueue[T]): bool = self.pos == self.payload.len
  proc push*[T](self: var simpleQueue[T], t: T) = self.payload.add(t)
  proc front*[T](self: simpleQueue[T]): T = self.payload[self.pos]
  proc clear*[T](self: var simpleQueue[T]) =
    self.payload.setLen(0)
    self.pos = 0
  proc pop*[T](self: var simpleQueue[T]) = self.pos.inc

when not declared ATCODER_MAXFLOW_HPP:
  const ATCODER_MAXFLOW_HPP* = 1

  type edge[Cap] = object
    dst, rev: int
    cap: Cap
  
  type MFGraph*[Cap] = object
    n: int
    pos: seq[(int, int)]
    g: seq[seq[edge[Cap]]]
  
  proc initMFGraph*[Cap](n: int): auto = MFGraph[Cap](n: n, g: newSeq[seq[edge[Cap]]](n))

  proc addEdge*[Cap](self: var MFGraph[Cap], src, dst: int, cap: Cap): int {.discardable.} =
    let m = self.pos.len
    self.pos.add((src, self.g[src].len))
    var
      srcId = self.g[src].len
      dstId = self.g[dst].len
    if src == dst: dstId.inc
    self.g[src].add(edge[Cap](dst: dst, rev: dstId, cap: cap))
    self.g[dst].add(edge[Cap](dst: src, rev: srcId, cap: 0))
    return m

  type EdgeInfo*[Cap] = object
    src*, dst*: int
    cap*, flow*: Cap
  
  proc getEdge*[Cap](self: MFGraph[Cap], i: int): EdgeInfo[Cap] =
    let
      m = self.pos.len
      e = self.g[self.pos[i][0]][self.pos[i][1]]
      re = self.g[e.dst][e.rev]
    return EdgeInfo[Cap](src: self.pos[i][0], dst: e.dst, cap: e.cap + re.cap, flow: re.cap)

  proc edges*[Cap](self: MFGraph[Cap]): seq[EdgeInfo[Cap]] =
    let m = self.pos.len
    result = newSeqOfCap[EdgeInfo[Cap]](m)
    for i in 0..<m:
      result.add(self.getEdge(i))
  
  proc changeEdge*[Cap](self: var MFGraph[Cap], i: int, newCap, newFlow: Cap) =
    var
      e = self.g[self.pos[i][0]][self.pos[i][1]].addr
      re = self.g[e[].dst][e[].rev].addr
    e[].cap = newCap - newFlow
    re[].cap = newFlow
  
  proc flow*[Cap](self: var MFGraph[Cap], s, t: int, flowLimit: Cap): Cap =
    var
      level, iter = newSeq[int](self.n)
      que = initSimpleQueue[int]()
    
    proc bfs(self: MFGraph[Cap]) =
      level.fill(-1)
      level[s] = 0
      que.clear()
      que.push(s)
      while not que.empty():
        let v = que.front()
        que.pop
        for e in self.g[v]:
          if e.cap == 0 or level[e.dst] >= 0: continue
          level[e.dst] = level[v] + 1
          if e.dst == t: return
          que.push(e.dst)
    
    proc dfs(self: var MFGraph[Cap], v: int, up: Cap): Cap =
      if v == s: return up
      result = Cap(0)
      let levelV = level[v]
      var i = iter[v].addr
      while i[] < self.g[v].len:
        let e = self.g[v][i[]].addr
        if levelV <= level[e[].dst] or self.g[e[].dst][e[].rev].cap == 0:
          i[].inc
          continue
        let d = self.dfs(e.dst, min(up - result, self.g[e[].dst][e[].rev].cap))
        if d <= 0:
          i[].inc
          continue
        self.g[v][i[]].cap += d
        self.g[e[].dst][e[].rev].cap -= d
        result += d
        if result == up: break
        i[].inc
    
    var flow = Cap(0)
    while flow < flowLimit:
      self.bfs()
      if level[t] == -1: break
      iter.fill(0)
      while flow < flowLimit:
        let f = self.dfs(t, flowLimit - flow)
        if f == Cap(0): break
        flow += f
    return flow

  proc flow*[Cap](self: var MFGraph[Cap], s, t: int): auto = self.flow(s, t, Cap.high)

  proc minCut*[Cap](self: MFGraph[Cap], s: int): seq[bool] =
    var
      visited = newSeq[bool](self.n)
      que = initSimpleQueue[int]()
    que.push(s)
    while not que.empty():
      let p = que.front()
      que.pop()
      visited[p] = true
      for e in self.g[p]:
        if e.cap != Cap(0) and not visited[e.dst]:
          visited[e.dst] = true
          que.push(e.dst)
    return visited

when isMainModule:
  var
    N = inputInt()
    c = newSeqWith(N, input())
  
  let
    S = N*N
    T = S + 1
  var mfg = initMFGraph[int](T + 1)
  
  for i in 0..<N:
    for j in 0..<N - 1:
      let x = i*N + j
      mfg.changeEdge(mfg.addEdge(x, x + 1, 2), 2, 1)
  for i in 0..<N - 1:
    for j in 0..<N:
      let x = i*N + j
      mfg.changeEdge(mfg.addEdge(x, x + N, 2), 2, 1)
  for i in 0..<N:
    for j in 0..<N:
      if c[i][j] == '?': continue
      let x = i*N + j
      if (i + j) mod 2 == 0:
        if c[i][j] == 'B':
          mfg.addEdge(S, x, 4)
        else:
          mfg.addEdge(x, T, 4)
      else:
        if c[i][j] == 'B':
          mfg.addEdge(x, T, 4)
        else:
          mfg.addEdge(S, x, 4)
  
  var ans = N*(N - 1)*2
  ans -= mfg.flow(S, T)
  echo ans
