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
  
when not declared ATCODER_LAZYSEGTREE_HPP:
  const ATCODER_LAZYSEGTREE_HPP* = 1
  
  type
    LazySegmentTree*[T, K] = ref object
      LV: Natural
      N0: Positive
      ide_ele: T
      lazy_ide_ele: K
      data: seq[T]
      lazy_data: seq[K]
      fold: (T, T) -> T
      eval: (T, K) -> T
      merge: (K, K) -> K
      propagatesWhenUpdating: bool
  
  proc initLazySegmentTree*[T, K](size: Positive, ide_ele: T, lazy_ide_ele: K, fold: (T, T) -> T, eval: (T, K) -> T, merge: (K, K) -> K, propagatesWhenUpdating=false): LazySegmentTree[T, K] =
    let
      LV = bitLength(size - 1)
      N0 = 1 shl LV
      data = newSeqWith(2*N0, ide_ele)
      lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    return LazySegmentTree[T, K](LV: LV, N0: N0, ide_ele: ide_ele, lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data, fold: fold, eval: eval, merge: merge, propagatesWhenUpdating: propagatesWhenUpdating)
  
  proc toLazySegmentTree*[T, K](init_value: openArray[T], ide_ele: T, lazy_ide_ele: K, fold: (T, T) -> T, eval: (T, K) -> T, merge: (K, K) -> K, propagatesWhenUpdating=false): LazySegmentTree[T, K] =
    let
      LV = bitLength(init_value.len - 1)
      N0 = 1 shl LV
      lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    var data = newSeqWith(2*N0, ide_ele)
    for i, x in init_value:
      data[i + N0 - 1] = x
    for i in countdown(N0 - 2, 0):
      data[i] = fold(data[2*i + 1], data[2*i + 2])
    return LazySegmentTree[T, K](LV: LV, N0: N0, ide_ele: ide_ele, lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data, fold: fold, eval: eval, merge: merge, propagatesWhenUpdating: propagatesWhenUpdating)
  
  iterator gindex*[T, K](self: var LazySegmentTree[T, K], left, right: Natural): Natural =
    var
      L = (left + self.N0) shr 1
      R = (right + self.N0) shr 1
      lc = if (left and 1) == 1: 0 else: bitLength(L and -L)
      rc = if (right and 1) == 1: 0 else: bitLength(R and -R)
    for i in 0..<self.LV:
      if rc <= i:
        yield R
      if L < R and lc <= i:
        yield L
      L = L shr 1
      R = R shr 1
  
  proc propagates*[T, K](self: var LazySegmentTree[T, K], ids: seq[Natural]) =
    var
      idx: Natural
      v: K
    for id in reversed(ids):
      idx = id - 1
      v = self.lazy_data[idx]
      if v == self.lazy_ide_ele:
        continue
      self.data[2*idx + 1] = self.eval(self.data[2*idx + 1], v)
      self.data[2*idx + 2] = self.eval(self.data[2*idx + 2], v)
      self.lazy_data[2*idx + 1] = self.merge(self.lazy_data[2*idx + 1], v)
      self.lazy_data[2*idx + 2] = self.merge(self.lazy_data[2*idx + 2], v)
      self.lazy_data[idx] = self.lazy_ide_ele
  
  proc update*[T, K](self: var LazySegmentTree[T, K], left, right: Natural, x: K) =
    let ids = toSeq(self.gindex(left, right))
    if self.propagatesWhenUpdating:
      self.propagates(ids)
    var
      L = left + self.N0
      R = right + self.N0
    
    while L < R:
      if (L and 1) == 1:
        self.lazy_data[L - 1] = self.merge(self.lazy_data[L - 1], x)
        self.data[L - 1] = self.eval(self.data[L - 1], x)
        inc L
      if (R and 1) == 1:
        dec R
        self.lazy_data[R - 1] = self.merge(self.lazy_data[R - 1], x)
        self.data[R - 1] = self.eval(self.data[R - 1], x)
      L = L shr 1
      R = R shr 1
    
    var idx: Natural
    for id in ids:
      idx = id - 1
      self.data[idx] = self.fold(self.data[2*idx + 1], self.data[2*idx + 2])
      if self.lazy_data[idx] != self.lazy_ide_ele:
        self.data[idx] = self.eval(self.data[idx], self.lazy_data[idx])
  
  proc query*[T, K](self: var LazySegmentTree[T, K], left, right: Natural): T =
    self.propagates(toSeq(self.gindex(left, right)))
    var
      L = left + self.N0
      R = right + self.N0
    result = self.ide_ele
    
    while L < R:
      if (L and 1) == 1:
        result = self.fold(result, self.data[L - 1])
        inc L
      if (R and 1) == 1:
        dec R
        result = self.fold(result, self.data[R - 1])
      L = L shr 1
      R = R shr 1

when isMainModule:
  var W, N: int
  (W, N) = inputInts()

  var
    lazySegTree = initLazySegmentTree(W + 1, 0, 0, (a, b) => max(a, b), (a, b: int) => b, (a, b: int) => b)
    li, ri: int
    ans: seq[int]
  for _ in 0..<N:
    (li, ri) = inputInts()
    let h = lazySegTree.query(li, ri + 1)
    lazySegTree.update(li, ri + 1, h + 1)
    ans.add(h + 1)
  echo ans.join("\n")
