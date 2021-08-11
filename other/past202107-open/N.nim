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
  proc `&=`*[string](s: var string, t: string) = s = s & t

when not declared ATCODER_INTERNAL_BITOP_HPP:
  const ATCODER_INTERNAL_BITOP_HPP* = 1

  proc ceil_pow2*(n:SomeInteger):int =
    var x = 0
    while (1.uint shl x) < n.uint: x.inc
    return x
  
  proc bsf*(n:SomeInteger):int =
    return countTrailingZeroBits(n)

when not declared ATCODER_LAZYSEGTREE_HPP:
  const ATCODER_LAZYSEGTREE_HPP* = 1
  
  type LazySegTree*[S,F;p:static[tuple]] = object
    n*, size*, log*:int
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
    (self.n, self.size, self.log) = (n, size, log)
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

  proc set*[ST:LazySegTree](self: var ST, p:int, x:ST.S) =
    assert p in 0..<self.n
    let p = p + self.size
    for i in countdown(self.log, 1): self.push(p shr i)
    self.d[p] = x
    for i in 1..self.log: self.update(p shr i)

  proc get*[ST:LazySegTree](self: var ST, p:int):ST.S =
    assert p in 0..<self.n
    let p = p + self.size
    for i in countdown(self.log, 1): self.push(p shr i)
    return self.d[p]

  proc `[]=`*[ST:LazySegTree](self: var ST, p:int, x:ST.S) = self.set(p, x)
  proc `[]`*[ST:LazySegTree](self: var ST, p:int):ST.S = self.get(p)

  proc prod*[ST:LazySegTree](self:var ST, p:Slice[int]):ST.S =
    var (l, r) = (p.a, p.b + 1)
    assert 0 <= l and l <= r and r <= self.n
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

  proc `[]`*[ST:LazySegTree](self: var ST, p:Slice[int]):ST.S = self.prod(p)

  proc all_prod*[ST:LazySegTree](self:ST):auto = self.d[1]

  proc apply*[ST:LazySegTree](self: var ST, p:int, f:ST.F) =
    assert p in 0..<self.n
    let p = p + self.size
    for i in countdown(self.log, 1): self.push(p shr i)
    self.d[p] = ST.calc_mapping(f, self.d[p])
    for i in 1..self.log: self.update(p shr i)
  proc apply*[ST:LazySegTree](self: var ST, p:Slice[int], f:ST.F) =
    var (l, r) = (p.a, p.b + 1)
    assert 0 <= l and l <= r and r <= self.n
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
  
  proc max_right*[ST:LazySegTree](self:var ST, l:int, g:(ST.S)->bool):int =
    assert l in 0..self.n
    assert g(ST.calc_e())
    if l == self.n: return self.n
    var l = l + self.size
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
    return self.n
  
  proc min_left*[ST:LazySegTree](self: var ST, r:int, g:(ST.S)->bool):int =
    assert r in 0..self.n
    assert(g(ST.calc_e()))
    if r == 0: return 0
    var r = r + self.size
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

when isMainModule:
  var
    Q = inputInt()
    A, B, C, D: array[100001, int]
  for i in 0..<Q:
    (A[i], B[i], C[i], D[i]) = inputInts()
  
  var xs: HashSet[int]
  for (bi, di) in zip(B, D)[0..<Q]:
    xs.incl(bi)
    xs.incl(di)
  
  var
    idx2x = sorted(toSeq(xs))
    x2idx: Table[int, int]
  for i, xi in idx2x:
    x2idx[xi] = i
  
  let
    xLen = collect(newSeq):
      for i in 1..<idx2x.len: idx2x[i] - idx2x[i - 1]
    initSeq = collect(newSeq):
      for length in xLen: (length, 0)
  proc op(a, b: (int, int)): (int, int) =
    return (a[0] + b[0], a[1] + b[1])
  proc mp(a: bool, b: (int, int)): (int, int) =
    if a:
      return (b[0], b[0] - b[1])
    return b
  proc cm(a, b: bool): bool =
    return a xor b
  var lsegt = initLazySegTree(initSeq, op, () => (0, 0), mp, cm, () => false)
  
  var queries: seq[(int, int, int)]
  for i in 0..<Q:
    queries.add((A[i], B[i], D[i]))
    queries.add((C[i], B[i], D[i]))
  queries.sort()
  
  var
    ans = 0
    py = queries[0][0]
  for i, (yi, bi, di) in queries:
    if py != yi:
      let sumX = lsegt.all_prod()[1]
      ans += (yi - py)*sumX
    lsegt.apply(x2idx[bi]..<x2idx[di], true)
    py = yi
  echo ans
