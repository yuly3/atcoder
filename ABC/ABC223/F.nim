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

when not declared ATCODER_INTERNAL_BITOP_HPP:
  const ATCODER_INTERNAL_BITOP_HPP* = 1

  proc ceil_pow2*(n:SomeInteger):int =
    var x = 0
    while (1.uint shl x) < n.uint: x.inc
    return x
  
  proc bsf*(n:SomeInteger):int =
    return countTrailingZeroBits(n)

when not declared ATCODER_RANGEUTILS_HPP:
  const ATCODER_RANGEUTILS_HPP* = 1
  type RangeType* = Slice[int] | HSlice[int, BackwardsIndex]
  type IndexType* = int | BackwardsIndex
  template halfOpenEndpoints*(p:Slice[int]):(int,int) = (p.a, p.b + 1)
  template `^^`*(s, i: untyped): untyped =
    (when i is BackwardsIndex: s.len - int(i) else: int(i))
  template halfOpenEndpoints*[T](s:T, p:RangeType):(int,int) =
    (p.a, s^^p.b + 1)

when not declared ATCODER_LAZYSEGTREE_HPP:
  const ATCODER_LAZYSEGTREE_HPP* = 1
  
  {.push inline.}
  type LazySegTree*[S,F;p:static[tuple]] = object
    len*, size*, log*:int
    d:seq[S]
    lz:seq[F]
  
  template calc_op[ST:LazySegTree](self:typedesc[ST], a, b:ST.S):auto =
    block:
      let op = ST.p.op
      op(a, b)
  template calc_e[ST:LazySegTree](self:typedesc[ST]):auto =
    block:
      let e = ST.p.e
      e()
  template calc_mapping[ST:LazySegTree](self:typedesc[ST], a:ST.F, b:ST.S):auto =
    block:
      let mapping = ST.p.mapping
      mapping(a, b)
  template calc_composition[ST:LazySegTree](self:typedesc[ST], a, b:ST.F):auto =
    block:
      let composition = ST.p.composition
      composition(a, b)
  template calc_id[ST:LazySegTree](self:typedesc[ST]):auto =
    block:
      let id = ST.p.id
      id()
  
  proc update[ST:LazySegTree](self:var ST, k:int) =
    self.d[k] = ST.calc_op(self.d[2 * k], self.d[2 * k + 1])
  proc all_apply*[ST:LazySegTree](self:var ST, k:int, f:ST.F) =
    self.d[k] = ST.calc_mapping(f, self.d[k])
    if k < self.size: self.lz[k] = ST.calc_composition(f, self.lz[k])
  proc push*[ST:LazySegTree](self: var ST, k:int) =
    self.all_apply(2 * k, self.lz[k])
    self.all_apply(2 * k + 1, self.lz[k])
    self.lz[k] = ST.calc_id()
  
  proc init[ST:LazySegTree](self:var ST, v:seq[ST.S]) =
    let
      n = v.len
      log = ceil_pow2(n)
      size = 1 shl log
    (self.len, self.size, self.log) = (n, size, log)
    if self.d.len < 2 * size:
      self.d = newSeqWith(2 * size, ST.calc_e())
    else:
      self.d.fill(0, 2 * size - 1, ST.calc_e())
    for i in 0..<n:
      self.d[size + i] = v[i]
    if self.lz.len < size:
      self.lz = newSeqWith(size, ST.calc_id())
    else:
      self.lz.fill(0, size - 1, ST.calc_id())
    for i in countdown(size - 1, 1): self.update(i)
  proc init[ST:LazySegTree](self: var ST, n:int) =
    self.init(newSeqWith(n, ST.calc_e()))
  proc init[ST:LazySegTree](self: typedesc[ST], v:seq[ST.S]):ST = result.init(v)
  proc init[ST:LazySegTree](self: typedesc[ST], n:int):ST = result.init(n)

  template getType*(ST:typedesc[LazySegTree], S, F:typedesc, op0:static[(S,S)->S],e0:static[()->S],mapping0:static[(F,S)->S],composition0:static[(F,F)->F],id0:static[()->F]):typedesc[LazySegTree] =
    LazySegTree[S, F, (op:op0, e:e0, mapping:mapping0, composition:composition0, id:id0)]
  template LazySegTreeType*(S, F:typedesc, op0:static[(S,S)->S],e0:static[()->S],mapping0:static[(F,S)->S],composition0:static[(F,F)->F],id0:static[()->F]):typedesc[LazySegTree] =
    LazySegTree[S, F, (op:op0, e:e0, mapping:mapping0, composition:composition0, id:id0)]
  
  proc initLazySegTree*[S, F](v:seq[S], op:static[(S,S)->S],e:static[()->S],mapping:static[(F,S)->S],composition:static[(F,F)->F],id:static[()->F]):auto =
    LazySegTreeType(S, F, op, e, mapping, composition, id).init(v)
  proc initLazySegTree*[S, F](n:int, op:static[(S,S)->S],e:static[()->S],mapping:static[(F,S)->S],composition:static[(F,F)->F],id:static[()->F]):auto =
    LazySegTreeType(S, F, op, e, mapping, composition, id).init(n)
  
  proc set*[ST:LazySegTree](self: var ST, p:IndexType, x:ST.S) =
    var p = self^^p
    assert p in 0..<self.len
    p += self.size
    for i in countdown(self.log, 1): self.push(p shr i)
    self.d[p] = x
    for i in 1..self.log: self.update(p shr i)
  
  proc get*[ST:LazySegTree](self: var ST, p:IndexType):ST.S =
    var p = self^^p
    assert p in 0..<self.len
    p += self.size
    for i in countdown(self.log, 1): self.push(p shr i)
    return self.d[p]

  proc `[]=`*[ST:LazySegTree](self: var ST, p:IndexType, x:ST.S) = self.set(p, x)
  proc `[]`*[ST:LazySegTree](self: var ST, p:IndexType):ST.S = self.get(p)

  proc prod*[ST:LazySegTree](self:var ST, p:RangeType):ST.S =
    var (l, r) = self.halfOpenEndpoints(p)
    assert 0 <= l and l <= r and r <= self.len
    if l == r: return ST.calc_e()

    l += self.size
    r += self.size

    for i in countdown(self.log, 1):
      if ((l shr i) shl i) != l: self.push(l shr i)
      if ((r shr i) shl i) != r: self.push(r shr i)
    
    var sml, smr = ST.calc_e()
    while l < r:
      if (l and 1) != 0: sml = ST.calc_op(sml, self.d[l]);l.inc
      if (r and 1) != 0: r.dec;smr = ST.calc_op(self.d[r], smr)
      l = l shr 1
      r = r shr 1
    return ST.calc_op(sml, smr)

  proc `[]`*[ST:LazySegTree](self: var ST, p:RangeType):ST.S = self.prod(p)

  proc all_prod*[ST:LazySegTree](self:ST):auto = self.d[1]

  proc apply*[ST:LazySegTree](self: var ST, p:IndexType, f:ST.F) =
    var p = self^^p
    assert p in 0..<self.len
    p += self.size
    for i in countdown(self.log, 1): self.push(p shr i)
    self.d[p] = ST.calc_mapping(f, self.d[p])
    for i in 1..self.log: self.update(p shr i)
  proc apply*[ST:LazySegTree](self: var ST, p:RangeType, f:ST.F) =
    var (l, r) = self.halfOpenEndpoints(p)
    assert 0 <= l and l <= r and r <= self.len
    if l == r: return

    l += self.size
    r += self.size

    for i in countdown(self.log, 1):
      if ((l shr i) shl i) != l: self.push(l shr i)
      if ((r shr i) shl i) != r: self.push((r - 1) shr i)
    
    block:
      var (l, r) = (l, r)
      while l < r:
        if (l and 1) != 0: self.all_apply(l, f);l.inc
        if (r and 1) != 0: r.dec;self.all_apply(r, f)
        l = l shr 1
        r = r shr 1
    
    for i in 1..self.log:
      if ((l shr i) shl i) != l: self.update(l shr i)
      if ((r shr i) shl i) != r: self.update((r - 1) shr i)
  
  proc max_right*[ST:LazySegTree](self:var ST, l:IndexType, g:(ST.S)->bool):int =
    var l = self^^l
    assert l in 0..self.len
    assert g(ST.calc_e())
    if l == self.len: return self.len
    l += self.size
    for i in countdown(self.log, 1): self.push(l shr i)
    var sm = ST.calc_e()
    while true:
      while l mod 2 == 0: l = l shr 1
      if not g(ST.calc_op(sm, self.d[l])):
        while l < self.size:
          self.push(l)
          l = (2 * l)
          if g(ST.calc_op(sm, self.d[l])):
            sm = ST.calc_op(sm, self.d[l])
            l.inc
        return l - self.size
      sm = ST.calc_op(sm, self.d[l])
      l.inc
      if not((l and -l) != l): break
    return self.len
  
  proc min_left*[ST:LazySegTree](self: var ST, r:IndexType, g:(ST.S)->bool):int =
    var r = self^^r
    assert r in 0..self.len
    assert(g(ST.calc_e()))
    if r == 0: return 0
    r += self.size
    for i in countdown(self.log, 1): self.push((r - 1) shr i)
    var sm = ST.calc_e()
    while true:
      r.dec
      while r > 1 and r mod 2 == 1: r = r shr 1
      if not g(ST.calc_op(self.d[r], sm)):
        while r < self.size:
          self.push(r)
          r = (2 * r + 1)
          if g(ST.calc_op(self.d[r], sm)):
            sm = ST.calc_op(self.d[r], sm)
            r.dec
        return r + 1 - self.size
      sm = ST.calc_op(self.d[r], sm)
      if not ((r and -r) != r): break
    return 0
  {.pop.}

when isMainModule:
  var N, Q: int
  (N, Q) = inputInts()
  var S = input().toSeq()
  
  var acc = newSeq[int](N + 1)
  for i in 0..<N:
    if S[i] == '(':
      acc[i + 1] = acc[i] + 1
    else:
      acc[i + 1] = acc[i] - 1
  
  proc op(x, y: int): int = min(x, y)
  proc mapping(x, y: int): int = x + y
  proc composition(x, y: int): int = x + y
  const INF = 10^18
  var lsegt = initLazySegTree(acc, op, () => INF, mapping, composition, () => 0)
  
  var ans = newSeq[string]()
  var cmd, left, right: int
  for _ in 0..<Q:
    (cmd, left, right) = inputInts()
    if cmd == 1:
      if S[left - 1] == '(' and S[right - 1] == ')':
        lsegt.apply(left..<right, -2)
      elif S[left - 1] == ')' and S[right - 1] == '(':
        lsegt.apply(left..<right, 2)
      swap(S[left - 1], S[right - 1])
    else:
      if lsegt[left - 1..right] == lsegt[left - 1] and lsegt[left - 1] == lsegt[right]:
        ans.add("Yes")
      else:
        ans.add("No")
  echo ans.join("\n")
