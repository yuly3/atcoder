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
  
when not declared ATCODER_SEGMENTTREE_HPP:
  const ATCODER_SEGMENTTREE_HPP* = 1
  
  type
    SegmentTree*[T, K] = ref object
      N0: Positive
      ideEle: T
      data: seq[T]
      fold: (T, T) -> T
      eval: (T, K) -> T
  
  proc initSegmentTree*[T, K](size: Positive, ideEle: T, fold: (T, T) -> T, eval: (T, K) -> T): SegmentTree[T, K] =
    let
      N0 = 1 shl bitLength(size - 1)
      data = newSeqWith(2*N0, ideEle)
    return SegmentTree[T, K](N0: N0, ideEle: ideEle, data: data, fold: fold, eval: eval)
  
  proc toSegmentTree*[T, K](init_value: openArray[T], ideEle: T, fold: (T, T) -> T, eval: (T, K) -> T): SegmentTree[T, K] =
    let N0 = 1 shl bitLength(init_value.len - 1)
    var data = newSeqWith(2*N0, ideEle)
    for i, x in init_value:
      data[i + N0 - 1] = x
    for i in countdown(N0 - 2, 0):
      data[i] = fold(data[2*i + 1], data[2*i + 2])
    return SegmentTree[T, K](N0: N0, ideEle: ideEle, data: data, fold: fold, eval: eval)
  
  proc update*[T, K](self: var SegmentTree[T, K], idx: Natural, x: K) =
    var k = self.N0 - 1 + idx
    self.data[k] = self.eval(self.data[k], x)
    while k != 0:
      k = (k - 1) div 2
      self.data[k] = self.fold(self.data[2*k + 1], self.data[2*k + 2])
  
  proc query*[T, K](self: var SegmentTree[T, K], left, right: Natural): T =
    var
      L = left + self.N0
      R = right + self.N0
    result = self.ideEle
  
    while L < R:
      if (L and 1) == 1:
        result = self.fold(result, self.data[L - 1])
        inc L
      if (R and 1) == 1:
        dec R
        result = self.fold(result, self.data[R - 1])
      L = L shr 1
      R = R shr 1
  
  proc `[]`*[T, K](self: var SegmentTree[T, K], k: int): T =
    return self.data[k + self.N0 - 1]

type Seg* = tuple[l, r, x: int]

when isMainModule:
  var
    N = inputInt()
    A = inputInts()
    Q = inputInt()
    li, ri, xi: int
    queries: seq[Seg] = collect(newSeq):
      for _ in 0..<Q: (li, ri, xi) = inputInts(); (li - 1, ri - 1, xi)
  
  const ideEle: Seg = (200001, 200001, 0)
  var
    counter = initTable[int, int]()
    segTree = initSegmentTree(N, ideEle, (a, b) => (if a.l < b.l: a else: b), (a, b: Seg) => b)
  for i, ai in A:
    if counter.hasKeyOrPut(ai, 1):
      inc counter[ai]
    segTree.update(i, (i, i, ai))
  
  var prevAns: int
  for _, val in counter:
    prevAns += val*(val - 1) div 2
  
  var ans = newSeq[int](Q)
  for i, nxtSeg in queries:
    var
      deff = initTable[int, int]()
      seg = segTree.query(nxtSeg.l, N)
    segTree.update(seg.r, ideEle)
    deff[seg.x] = -(min(seg.r, nxtSeg.r) - nxtSeg.l + 1)
    if seg.l < nxtSeg.l:
      let newSeg = (seg.l, nxtSeg.l - 1, seg.x)
      segTree.update(nxtSeg.l - 1, newSeg)
    if seg.r > nxtSeg.r:
      let newSeg = (nxtSeg.r + 1, seg.r, seg.x)
      segTree.update(seg.r, newSeg)
    
    while true:
      seg = segTree.query(seg.r + 1, N)
      if seg.r >= nxtSeg.r:
        break
      segTree.update(seg.r, ideEle)
      if deff.hasKeyOrPut(seg.x, -(seg.r - seg.l + 1)):
        deff[seg.x] -= seg.r - seg.l + 1
    
    if seg.l <= nxtSeg.r:
      segTree.update(seg.r, ideEle)
      if deff.hasKeyOrPut(seg.x, -(nxtSeg.r - seg.l + 1)):
        deff[seg.x] -= nxtSeg.r - seg.l + 1
      if seg.r > nxtSeg.r:
        let newSeg = (nxtSeg.r + 1, seg.r, seg.x)
        segTree.update(seg.r, newSeg)
    
    segTree.update(nxtSeg.r, nxtSeg)
    if deff.hasKeyOrPut(nxtSeg.x, nxtSeg.r - nxtSeg.l + 1):
      deff[nxtSeg.x] += nxtSeg.r - nxtSeg.l + 1
    
    for key, val in deff:
      var cnt = counter.getOrDefault(key, 0)
      prevAns -= cnt*(cnt - 1) div 2
      cnt += val
      prevAns += cnt*(cnt - 1) div 2
      counter[key] = cnt
    ans[i] = prevAns
  echo ans.join("\n")
