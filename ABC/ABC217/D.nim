when not declared ATCODER_YULY3HEADER_HPP:
  const ATCODER_YULY3HEADER_HPP* = 1

  import
    algorithm,
    bitops,
    complex,
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

  {.warning[UnusedImport]: off.}
  {.hint[XDeclaredButNotUsed]: off.}

  proc freshIdentNodes(ast: NimNode): NimNode =
    # Replace NimIdent and NimSym by a fresh ident node
    # see also https://github.com/nim-lang/Nim/pull/8531#issuecomment-410436458
    proc inspect(node: NimNode): NimNode =
      case node.kind:
      of nnkIdent, nnkSym:
        result = ident($node)
      of nnkEmpty, nnkLiterals:
        result = node
      else:
        result = node.kind.newTree()
        for child in node:
          result.add inspect(child)
    result = inspect(ast)

  proc trans(n, res, bracketExpr: NimNode): (NimNode, NimNode, NimNode) =
    # Looks for the last statement of the last statement, etc...
    case n.kind
    of nnkIfExpr, nnkIfStmt, nnkTryStmt, nnkCaseStmt, nnkWhenStmt:
      result[0] = copyNimTree(n)
      result[1] = copyNimTree(n)
      result[2] = copyNimTree(n)
      for i in ord(n.kind == nnkCaseStmt) ..< n.len:
        (result[0][i], result[1][^1], result[2][^1]) = trans(n[i], res, bracketExpr)
    of nnkStmtList, nnkStmtListExpr, nnkBlockStmt, nnkBlockExpr, nnkWhileStmt,
        nnkForStmt, nnkElifBranch, nnkElse, nnkElifExpr, nnkOfBranch, nnkExceptBranch:
      result[0] = copyNimTree(n)
      result[1] = copyNimTree(n)
      result[2] = copyNimTree(n)
      if n.len >= 1:
        (result[0][^1], result[1][^1], result[2][^1]) = trans(n[^1],
            res, bracketExpr)
    of nnkTableConstr:
      result[1] = n[0][0]
      result[2] = n[0][1]
      if bracketExpr.len == 0:
        bracketExpr.add(ident"initTable") # don't import tables
      if bracketExpr.len == 1:
        bracketExpr.add([newCall(bindSym"typeof",
            newEmptyNode()), newCall(bindSym"typeof", newEmptyNode())])
      template adder(res, k, v) = res[k] = v
      result[0] = getAst(adder(res, n[0][0], n[0][1]))
    of nnkCurly:
      result[2] = n[0]
      if bracketExpr.len == 0:
        bracketExpr.add(ident"initHashSet")
      if bracketExpr.len == 1:
        bracketExpr.add(newCall(bindSym"typeof", newEmptyNode()))
      template adder(res, v) = res.incl(v)
      result[0] = getAst(adder(res, n[0]))
    else:
      result[2] = n
      if bracketExpr.len == 0:
        bracketExpr.add(bindSym"newSeq")
      if bracketExpr.len == 1:
        bracketExpr.add(newCall(bindSym"typeof", newEmptyNode()))
      template adder(res, v) = res.add(v)
      result[0] = getAst(adder(res, n))

  proc collectImpl(init, body: NimNode): NimNode =
    let res = genSym(nskVar, "collectResult")
    var bracketExpr: NimNode
    if init != nil:
      expectKind init, {nnkCall, nnkIdent, nnkSym}
      bracketExpr = newTree(nnkBracketExpr,
        if init.kind == nnkCall: freshIdentNodes(init[0]) else: freshIdentNodes(init))
    else:
      bracketExpr = newTree(nnkBracketExpr)
    let (resBody, keyType, valueType) = trans(body, res, bracketExpr)
    if bracketExpr.len == 3:
      bracketExpr[1][1] = keyType
      bracketExpr[2][1] = valueType
    else:
      bracketExpr[1][1] = valueType
    let call = newTree(nnkCall, bracketExpr)
    if init != nil and init.kind == nnkCall:
      for i in 1 ..< init.len:
        call.add init[i]
    result = newTree(nnkStmtListExpr, newVarStmt(res, call), resBody, res)

  macro collect*(init, body: untyped): untyped =
    ## Comprehension for seqs/sets/tables.
    ##
    ## The last expression of `body` has special syntax that specifies
    ## the collection's add operation. Use `{e}` for set's `incl`,
    ## `{k: v}` for table's `[]=` and `e` for seq's `add`.
    # analyse the body, find the deepest expression 'it' and replace it via
    # 'result.add it'
    runnableExamples:
      import std/[sets, tables]

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
      let y = collect(initHashSet()):
        for d in data.items: {d}
      assert y == data.toHashSet

      ## Table:
      let z = collect(initTable(2)):
        for i, d in data.pairs: {i: d}
      assert z == {0: "bird", 1: "word"}.toTable

    result = collectImpl(init, body)

  macro collect*(body: untyped): untyped =
    ## Same as `collect` but without an `init` parameter.
    runnableExamples:
      import std/[sets, tables]
      let data = @["bird", "word"]

      # seq:
      let k = collect:
        for i, d in data.pairs:
          if i mod 2 == 0: d
      assert k == @["bird"]

      ## HashSet:
      let n = collect:
        for d in data.items: {d}
      assert n == data.toHashSet

      ## Table:
      let m = collect:
        for i, d in data.pairs: {i: d}
      assert m == {0: "bird", 1: "word"}.toTable

      # avoid `collect` when `sequtils.toSeq` suffices:
      assert collect(for i in 1..3: i*i) == @[1, 4, 9] # ok in this case
      assert collect(for i in 1..3: i) == @[1, 2, 3] # overkill in this case
      from std/sequtils import toSeq
      assert toSeq(1..3) == @[1, 2, 3] # simpler

    result = collectImpl(nil, body)

  proc nextString*(f: auto = stdin): string =
    var get = false
    result = ""
    while true:
      let c = f.readChar
      if c.int > ' '.int:
        get = true
        result.add(c)
      elif get: return
  proc nextInt*(f: auto = stdin): int = parseInt(f.nextString)
  proc nextFloat*(f: auto = stdin): float = parseFloat(f.nextString)

  proc chmax*[T](n: var T, m: T) {.inline.} = n = max(n, m)
  proc chmin*[T](n: var T, m: T) {.inline.} = n = min(n, m)
  proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)
  proc `|=`*[T: SomeInteger or bool](n: var T, m: T) {.inline.} = n = n or m
  proc `&=`*[T: SomeInteger or bool](n: var T, m: T) {.inline.} = n = n and m
  proc `^=`*[T: SomeInteger or bool](n: var T, m: T) {.inline.} = n = n xor m
  proc `<<=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = n shl m
  proc `>>=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = n shr m

when not declared ATCODER_SQUARELIST:
  const ATCODER_SQUARELIST* = 1

  type SquareList*[T] = object
    sz: int
    d: seq[seq[T]]
    idMin, idMax: () -> T

  const
    BUCKET_RATIO = 4
    REBUILD_RATIO = 12

  iterator items*[T](self: SquareList[T]): T =
    for i in 0..<self.d.len:
      for j in 0..<self.d[i].len:
        yield self.d[i][j]

  proc build[T](self: var SquareList[T]) =
    let
      a = toSeq(self.items)
      bucketCount = sqrt(self.sz.float/BUCKET_RATIO.float).ceil.int
    self.d = newSeqWith(bucketCount, newSeq[T]())
    for i in 0..<bucketCount:
      self.d[i] = a[self.sz*i div bucketCount..<self.sz*(i + 1) div bucketCount]

  proc initSquareList*[T](
    idMin, idMax: () -> T,
    a: seq[T] = @[]
  ): SquareList[T] =
    var a = a
    if not issorted(a):
      a.sort()
    var d: seq[seq[T]]
    if a.len > 0:
      d.add(a)
    result = SquareList[T](sz: a.len, d: d, idMin: idMin, idMax: idMax)
    result.build

  proc len*[T](self: SquareList[T]): int {.inline.} = self.sz

  proc findBucket[T](self: var SquareList, x: T): ptr seq[T] =
    for i in 0..<self.d.len:
      if x <= self.d[i][^1]:
        return self.d[i].addr
    return self.d[^1].addr

  proc contains*[T](self: var SquareList[T], x: T): bool =
    if self.sz == 0: return false
    var
      a = self.findBucket(x)
      i = a[].lowerBound(x)
    return i != a[].len and a[][i] == x

  proc index*[T](self: SquareList[T], x: T): int =
    for i in 0..<self.d.len:
      if self.d[i][^1] >= x:
        return result + self.d[i].lowerBound(x)
      result += self.d[i].len
  proc indexRight*[T](self: SquareList[T], x: T): int =
    for i in 0..<self.d.len:
      if self.d[i][^1] > x:
        return result + self.d[i].lowerBound(x)
      result += self.d[i].len

  proc count*[T](self: SquareList, x: T): int {.inline.} =
    self.indexRight(x) - self.index(x)

  proc incl*[T](self: var SquareList[T], x: T) =
    if self.sz == 0:
      self.d = @[@[x]]
      self.sz = 1
      return
    var
      a = self.findBucket(x)
      i = a[].lowerBound(x)
    a[].insert(@[x], i)
    self.sz.inc
    if a[].len > self.d.len*REBUILD_RATIO:
      self.build

  proc excl*[T](self: var SquareList[T], x: T): bool {.discardable.} =
    if self.sz == 0: return false
    var
      a = self.findBucket(x)
      i = a[].lowerBound(x)
    if i == a[].len or a[][i] != x: return false
    a[].del(i)
    self.sz.dec
    if a[].len == 0: self.build
    return true

  proc prev*[T](self: SquareList[T], x: T): T =
    for i in countdown(self.d.len - 1, 0):
      if self.d[i][0] < x:
        return self.d[i][self.d[i].lowerBound(x) - 1]
    return self.idMin()
  proc prevEqual*[T](self: SquareList[T], x: T): T =
    for i in countdown(self.d.len - 1, 0):
      if self.d[i][0] <= x:
        return self.d[i][self.d[i].upperBound(x) - 1]
    return self.idMin()
  proc next*[T](self: SquareList[T], x: T): T =
    for i in 0..<self.d.len:
      if self.d[i][^1] > x:
        return self.d[i][self.d[i].upperBound(x)]
    return self.idMax()
  proc nextEqual*[T](self: SquareList[T], x: T): T =
    for i in 0..<self.d.len:
      if self.d[i][^1] >= x:
        return self.d[i][self.d[i].lowerBound(x)]
    return self.idMax()

  proc `[]`*[T](self: SquareList[T], k: int): T =
    var k = k
    if k < 0: k += self.sz
    assert k >= 0
    for i in 0..<self.d.len:
      if k < self.d[i].len: return self.d[i][k]
      k -= self.d[i].len
    assert false

when isMainModule:
  var L, Q = nextInt()

  var
    sl = initSquareList(() => 0, () => L)
    ans: seq[int]
  for _ in 0..<Q:
    let ci, xi = nextInt()
    if ci == 1:
      sl.incl(xi)
    else:
      ans.add(sl.next(xi) - sl.prev(xi))
  echo ans.join("\n")
