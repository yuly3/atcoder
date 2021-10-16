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
  proc chmax*[T](n: var T, m: T) {.inline.} = n = max(n, m)
  proc chmin*[T](n: var T, m: T) {.inline.} = n = min(n, m)
  proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)
  proc `|=`*[T: SomeInteger or bool](n: var T, m: T) {.inline.} = n = n or m
  proc `&=`*[T: SomeInteger or bool](n: var T, m: T) {.inline.} = n = n and m
  proc `^=`*[T: SomeInteger or bool](n: var T, m: T) {.inline.} = n = n xor m
  proc `<<=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = n shl m
  proc `>>=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = n shr m

when isMainModule:
  const
    MAX_N = 100001
    INF = 10^18
  var N, M, S, T, U, V: int
  (N, M) = inputInts()
  (S, T) = inputInts().mapIt(it - 1)
  (U, V) = inputInts().mapIt(it - 1)
  var
    graph: array[MAX_N, seq[tuple[to, w: int]]]
    ai, bi, ci: int
  for _ in 0..<M:
    (ai, bi, ci) = inputInts()
    graph[ai - 1].add((bi - 1, ci))
    graph[bi - 1].add((ai - 1, ci))
  
  var hque: HeapQueue[tuple[c, v: int]]
  
  proc dijkstra(s: int, dist: ptr array[MAX_N, int]) =
    dist[].fill(INF)
    dist[][s] = 0
    hque = initHeapQueue[tuple[c, v: int]]()
    hque.push((0, s))
    while hque.len > 0:
      let (cc, cv) = hque.pop()
      if dist[][cv] < cc:
        continue
      for (nv, w) in graph[cv]:
        let nc = cc + w
        if dist[][nv] <= nc:
          continue
        dist[][nv] = nc
        hque.push((nc, nv))
  
  var distS, distU, distV: array[MAX_N, int]
  dijkstra(S, distS.addr)
  dijkstra(U, distU.addr)
  dijkstra(V, distV.addr)
  
  var dp: array[MAX_N, array[4, int]]
  for i in 0..<N:
    for j in 0..3:
      dp[i][j] = INF
  dp[S][0] = 0
  dp[S][1] = distU[S]
  dp[S][2] = distV[S]
  dp[S][3] = distU[S] + distV[S]

  var order = collect(newSeq):
    for i in 0..<N: (distS[i], i)
  order.sort()
  for (_, to) in order:
    for (fr, c) in graph[to]:
      if distS[to] != distS[fr] + c:
        continue
      for i in 0..3:
        for j in 0..3:
          var add = 0
          if bitand(j, 1) == 1:
            add += distU[to]
          if bitand(j shr 1, 1) == 1:
            add += distV[to]
          dp[to][i or j].chmin(dp[fr][i] + add)
  
  let ans = min(distU[V], dp[T][3])
  echo ans
