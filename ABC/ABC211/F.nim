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
      propagatesWhenUpdating: bool

  proc initDualSegmentTree*[T](size: Positive, lazy_ide_ele: T, merge: (T, T) -> T, propagatesWhenUpdating=false): DualSegmentTree[T] =
    let
      LV = bitLength(size - 1)
      N0 = 1 shl LV
      lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    return DualSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: lazy_data, merge: merge, propagatesWhenUpdating: propagatesWhenUpdating)

  proc toDualSegmentTree*[T](init_value: openArray[T], lazy_ide_ele: T, merge: (T, T) -> T, propagatesWhenUpdating=false): DualSegmentTree[T] =
    let
      LV = bitLength(init_value.len - 1)
      N0 = 1 shl LV
    var lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    for i, x in init_value:
      lazy_data[i + N0 - 1] = x
    return DualSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: lazy_data, merge: merge, propagatesWhenUpdating: propagatesWhenUpdating)
  
  proc propagate*[T](self: var DualSegmentTree[T], k: Natural) =
    for i in countdown(self.LV, 1):
      let t = (k shr i) - 1
      if self.lazy_data[t] != self.lazy_ide_ele:
        self.lazy_data[2*t + 1] = self.merge(self.lazy_data[2*t + 1], self.lazy_data[t])
        self.lazy_data[2*t + 2] = self.merge(self.lazy_data[2*t + 2], self.lazy_data[t])
        self.lazy_data[t] = self.lazy_ide_ele
  
  proc update*[T](self: var DualSegmentTree[T], left, right: Natural, x: T) =
    if self.propagatesWhenUpdating:
      self.propagate(left + self.N0)
      self.propagate(right + self.N0 - 1)
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
  var
    N = inputInt()
    vertexes = newSeq[seq[(int, int)]]()
  for _ in 0..<N:
    let
      mi = inputInt()
      xys = inputInts()
    var vs = collect(newSeq):
      for j in 0..<mi:
        (xys[j*2], xys[j*2 + 1])
    vertexes.add(vs)
  var
    Q = inputInt()
    XY = collect(newSeq):
      for _ in 0..<Q:
        let xy = inputInts()
        (xy[0], xy[1])
  
  var events = newSeq[int]()
  for xys in vertexes:
    var
      lines = newSeq[int]()
      uniY = initHashSet[int]()
    for i in countup(0, xys.len - 1, 2):
      var
        (xi, yi) = xys[i]
        (_, yj) = xys[i + 1]
      if yi > yj:
        swap(yi, yj)
      lines.add((xi shl 43) or (yi shl 22) or (yj shl 2))
      uniY.incl(yi)
      uniY.incl(yj)
    lines.sort()
    let yToIdx = collect(initTable):
      for i, yi in sorted(toSeq(uniY)): {yi: i}
    
    var dseg = initDualSegmentTree(uniY.len, 0, (a: int, b: int) => a + b)
    for line in lines:
      let
        yi = bitand(line shr 22, 0xfffff)
        yj = bitand(line shr 2, 0xfffff)
      if dseg[yToIdx[yi]] == 1:
        events.add(line)
        dseg.update(yToIdx[yi], yToIdx[yj], -1)
      else:
        events.add(line or 2)
        dseg.update(yToIdx[yi], yToIdx[yj], 1)
  
  for i, (xi, yi) in XY:
    events.add((xi shl 43) or (1 shl 42) or (yi shl 22) or (i shl 2))
  events.sort()
  
  var
    dseg = initDualSegmentTree(100010, 0, (a: int, b: int) => a + b)
    ans = newSeq[int](Q)
  for num in events:
    if bitand(num, 1 shl 42) == 0:
      dseg.update(bitand(num shr 22, 0xfffff), bitand(num shr 2, 0xfffff), bitand(num, 2) - 1)
    else:
      ans[bitand(num shr 2, 0xfffff)] = dseg[bitand(num shr 22, 0xfffff)]
  echo ans.join("\n")
