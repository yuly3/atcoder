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

when isMainModule:
  var H, W: int
  (H, W) = inputInts()
  var A, B: array[200001, int]
  for i in 0..<H:
    (A[i], B[i]) = inputInts()
  
  const INF = 10^9
  type S = (int, int)
  proc op(a, b: S): S =
    if a[1] - a[0] <= b[1] - b[0]: return a
    return b
  var
    initVal = collect(newSeq):
      for i in 0..<W: (i, i)
    st = initSegTree(initVal, op, () => (0, INF))
    endPoint = initSegTree(toSeq(0..<W), (a: int, b: int) => min(a, b), () => INF)
    ans = newSeqWith(H, -1)
    ai, bi: int
  for i in 0..<H:
    (ai, bi) = (A[i], B[i])
    dec ai
    
    var e = endPoint[ai..<bi]
    while e < bi:
      if bi != W and op(st[bi], st[e]) == st[e]:
        st[bi] = (st[e][0], bi)
        endPoint[bi] = bi
      st[e] = (0, INF)
      endPoint[e] = INF
      e = endPoint[e + 1..<bi]
    
    let (s, t) = st.all_prod
    if t - s == INF:
      break
    ans[i] = t - s + i + 1
  echo ans.join("\n")
