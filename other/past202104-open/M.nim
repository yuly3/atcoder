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

when not declared ATCODER_SQUARESKIPLIST_HPP:
  const ATCODER_SQUARESKIPLIST_HPP* = 1

  type
    SquareSkipList*[T] = ref object
      square: Natural
      rand_y: int
      layer1: seq[T]
      layer0: seq[seq[T]]
      cmpFunc: (T, T) -> int

  proc initSquareSkipList*[T](inf: T, cmpFunc: (T, T) -> int, square=1000, rand_y=42): SquareSkipList[T] =
    var
      layer1 = @[inf]
      layer0 = newSeqWith(1, newSeq[T]())
    return SquareSkipList[T](square: square, rand_y: rand_y, layer1: layer1, layer0: layer0, cmpFunc: cmpFunc)

  proc add*[T](self: var SquareSkipList[T], x: T) =
    var y = self.rand_y
    y = y xor ((y and 0x7ffff) shl 13)
    y = y xor (y shr 17)
    y = y xor ((y and 0x7ffffff) shl 5)
    self.rand_y = y

    if floorMod(y, self.square) == 0:
      let idx1 = self.layer1.upperBound(x, self.cmpFunc)
      self.layer1.insert(@[x], idx1)
      let idx0 = self.layer0[idx1].upperBound(x, self.cmpFunc)
      self.layer0.insert(self.layer0[idx1][idx0..^1], idx1 + 1)
      self.layer0[idx1].delete(idx0, self.layer0[idx1].len)
    else:
      let
        idx1 = self.layer1.upperBound(x, self.cmpFunc)
        idx0 = self.layer0[idx1].upperBound(x, self.cmpFunc)
      self.layer0[idx1].insert(@[x], idx0)

  proc remove*[T](self: var SquareSkipList[T], x: T) =
    let
      idx1 = self.layer1.lowerBound(x, self.cmpFunc)
      idx0 = self.layer0[idx1].lowerBound(x, self.cmpFunc)
    if idx0 == self.layer0[idx1].len:
      self.layer1.delete(idx1, idx1)
      self.layer0[idx1] = concat(self.layer0[idx1], self.layer0[idx1 + 1])
      self.layer0.delete(idx1 + 1, idx1 + 1)
    else:
      self.layer0[idx1].delete(idx0, idx0)

  proc nextEqual*[T](self: var SquareSkipList[T], x: T): T =
    let
      idx1 = self.layer1.lowerBound(x, self.cmpFunc)
      idx0 = self.layer0[idx1].lowerBound(x, self.cmpFunc)
    if idx0 == len(self.layer0[idx1]):
      return self.layer1[idx1]
    return self.layer0[idx1][idx0]

  proc next*[T](self: var SquareSkipList[T], x: T): T =
    let
      idx1 = self.layer1.upperBound(x, self.cmpFunc)
      idx0 = self.layer0[idx1].upperBound(x, self.cmpFunc)
    if idx0 == len(self.layer0[idx1]):
      return self.layer1[idx1]
    return self.layer0[idx1][idx0]

  proc prev*[T](self: var SquareSkipList[T], x: T): T =
    let
      idx1 = self.layer1.lowerBound(x, self.cmpFunc)
      idx0 = self.layer0[idx1].lowerBound(x, self.cmpFunc)
    if idx0 == 0:
      return self.layer1[idx1 - 1]
    return self.layer0[idx1][idx0 - 1]

  proc contains*[T](self: var SquareSkipList[T], x: T): bool =
    let
      idx1 = self.layer1.lowerBound(x, self.cmpFunc)
      idx0 = self.layer0[idx1].lowerBound(x, self.cmpFunc)
    if idx0 == self.layer0[idx1].len:
      return self.layer1[idx1] == x
    return self.layer0[idx1][idx0] == x

  proc pop*[T](self: var SquareSkipList[T], idx: Natural): T =
    var
      s = -1
      i: int
    for ii, l0 in self.layer0:
      s += l0.len + 1
      i = ii
      if idx <= s:
        break
    if s == idx:
      self.layer0[i] = concat(self.layer0[i], @[self.layer0[i + 1]])
      self.layer0.delete(i + 1, i + 1)
      let res = self.layer1[i]
      self.layer1.delete(i, i)
      return res
    else:
      let res = self.layer0[i][idx - s]
      self.layer0[i].delete(idx - s, idx - s)
      return res

  proc popMax*[T](self: var SquareSkipList[T]): T =
    if self.layer0[^1].len != 0:
      return self.layer0[^1].pop()
    elif 1 < self.layer1.len:
      self.layer0.delete(self.layer0.len - 1, self.layer0.len - 1)
      let res = self.layer1[^2]
      self.layer1.delete(self.layer1.len - 2, self.layer1.len - 2)
      return res
    else:
      assert(false, "This is empty")

  proc `[]`*[T](self: var SquareSkipList[T], k: Natural): T =
    var
      s = -1
      ii = 0
    for i, l0 in self.layer0:
      s += l0.len + 1
      ii = i
      if k <= s:
        break
    if s == k:
      return self.layer1[ii]
    return self.layer0[ii][k - s]

  proc min*[T](self: var SquareSkipList[T]): T =
    return if self.layer0[0].len != 0: self.layer0[0][0] else: self.layer1[0]

  proc max*[T](self: var SquareSkipList[T]): T =
    return if self.layer0[^1].len != 0: self.layer0[^1][^1] elif 1 < self.layer1.len: self.layer1[^2] else: self.layer1[^1]

type Seg* = tuple[l, r, x: int]
proc cmp*(x, y: Seg): int =
  if x.r > y.r: return 1
  elif x.r == y.r: return 0
  else: return -1

when isMainModule:
  var
    N = inputInt()
    A = inputInts()
    Q = inputInt()
    li, ri, xi: int
    query: seq[Seg] = collect(newSeq):
      for _ in 0..<Q: (li, ri, xi) = inputInts(); (li - 1, ri - 1, xi)
  
  var
    counter = initTable[int, int]()
    ssl = initSquareSkipList[Seg]((200001, 200001, 0), cmp, 450)
  for i, ai in A:
    if counter.hasKeyOrPut(ai, 1):
      inc counter[ai]
    ssl.add((i, i, ai))
  
  var prevAns: int
  for _, val in counter:
    prevAns += val*(val - 1) div 2
  
  var ans = newSeq[int](Q)
  for i, nxtSeg in query:
    var
      deff = initTable[int, int]()
      seg = ssl.nextEqual((0, nxtSeg.l, 0))
    ssl.remove(seg)
    deff[seg.x] = -(min(seg.r, nxtSeg.r) - nxtSeg.l + 1)
    if seg.l < nxtSeg.l:
      let newSeg = (seg.l, nxtSeg.l - 1, seg.x)
      ssl.add(newSeg)
    if seg.r > nxtSeg.r:
      let newSeg = (nxtSeg.r + 1, seg.r, seg.x)
      ssl.add(newSeg)
    
    while true:
      seg = ssl.next(seg)
      if seg.r >= nxtSeg.r:
        break
      ssl.remove(seg)
      if deff.hasKeyOrPut(seg.x, -(seg.r - seg.l + 1)):
        deff[seg.x] -= seg.r - seg.l + 1
    
    if seg.l <= nxtSeg.r:
      ssl.remove(seg)
      if deff.hasKeyOrPut(seg.x, -(nxtSeg.r - seg.l + 1)):
        deff[seg.x] -= nxtSeg.r - seg.l + 1
      if seg.r > nxtSeg.r:
        let newSeg = (nxtSeg.r + 1, seg.r, seg.x)
        ssl.add(newSeg)

    ssl.add(nxtSeg)
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
