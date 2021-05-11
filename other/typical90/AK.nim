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

when not declared ATCODER_DUALSEGTREE_HPP:
  const ATCODER_DUALSEGTREE_HPP* = 1
  
  type
    DualSegmentTree*[T] = ref object
      LV: Natural
      N0: Positive
      lazy_ide_ele: T
      lazy_data: seq[T]
      merge: (T, T) -> T

  proc initDualSegmentTree*[T](size: Positive, lazy_ide_ele: T, merge: (T, T) -> T): DualSegmentTree[T] =
    let
      LV = bitLength(size - 1)
      N0 = 1 shl LV
      lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    return DualSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: lazy_data, merge: merge)

  proc toDualSegmentTree*[T](init_value: openArray[T], lazy_ide_ele: T, merge: (T, T) -> T): DualSegmentTree[T] =
    let
      LV = bitLength(init_value.len - 1)
      N0 = 1 shl LV
    var lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    for i, x in init_value:
      lazy_data[i + N0 - 1] = x
    return DualSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: lazy_data, merge: merge)

  proc propagate*[T](self: var DualSegmentTree[T], k: Natural) =
    for i in countdown(self.LV, 1):
      let t = k shr i
      if self.lazy_data[t] != self.lazy_ide_ele:
        self.lazy_data[2*t + 1] = self.merge(self.lazy_data[2*t + 1], self.lazy_data[t])
        self.lazy_data[2*t + 2] = self.merge(self.lazy_data[2*t + 2], self.lazy_data[t])
        self.lazy_data[t] = self.lazy_ide_ele

  proc update*[T](self: var DualSegmentTree[T], left, right: Natural, x: T) =
    var
      L = left + self.N0
      R = right + self.N0
    
    while L < R:
      if (L and 1) == 1:
        self.lazy_data[L - 1] = self.merge(self.lazy_data[L - 1], x)
        inc L
      if (R and 1) == 1:
        dec R
        self.lazy_data[R - 1] = self.merge(self.lazy_data[R - 1], x)
      L = L shr 1
      R = R shr 1

  proc `[]`*[T](self: var DualSegmentTree[T], k: Natural): T =
    self.propagate(k + self.N0)
    return self.lazy_data[k + self.N0 - 1]

when isMainModule:
  var W, N: int
  (W, N) = inputInts()
  var L, R, V: array[501, int]
  for i in 0..<N:
    (L[i], R[i], V[i]) = inputInts()

  var
    dp: array[10001, int]
    dualSegTree = initDualSegmentTree(W + 1, -1, (a, b) => max(a, b))
    li, ri, vi: int
  dp.fill(-1)
  dp[0] = 0
  for i in 0..<N:
    (li, ri, vi) = (L[i], R[i], V[i])
    dualSegTree.lazy_data.fill(-1)
    for j in 0..W - li:
      if dp[j] < 0:
        continue
      dualSegTree.update(j + li, min(j + ri, W) + 1, dp[j] + vi)
    for j in 0..W:
      dp[j].chmax(dualSegTree[j])
  echo dp[W]
