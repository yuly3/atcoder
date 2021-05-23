when not declared ATCODER_YULY3HEADER_HPP:
  const ATCODER_YULY3HEADER_HPP* = 1

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

when not declared ATCODER_ROLLINGHASH_HPP:
  const ATCODER_ROLLINGHASH_HPP* = 1

  const
    mask30 = (1 shl 30) - 1
    mask31 = (1 shl 31) - 1
    mask61 = (1 shl 61) - 1
  
  proc calcMod(x, MOD: int): int =
    let
      xu = x shr 61
      xd = x and mask61
    result = xu + xd
    if result >= MOD:
      result -= MOD
  
  proc modMul(a, b, MOD: int): int =
    let
      au = a shr 31
      ad = a and mask31
      bu = b shr 31
      bd = b and mask31
      mid = ad*bu + au*bd
      midu = mid shr 30
      midd = mid and mask30
    calcMod(au*bu*2 + midu + (midd shl 31) + ad*bd, MOD)
  
  type RollingHash = ref object
    MOD: int
    pw, h: seq[int]
  
  proc initRollingHash*(s: openArray[int], base=10007, MOD=(1 shl 61) - 1): RollingHash =
    var
      pw, h = newSeq[int](s.len + 1)
    pw[0] = 1
    var v = 0
    for i in 0..<s.len:
      v = (modMul(v, base, MOD) + s[i]) mod MOD
      h[i + 1] = v
    v = 1
    for i in 0..<s.len:
      v = modMul(v, base, MOD)
      pw[i + 1] = v
    RollingHash(MOD: MOD, pw: pw, h: h)
  
  proc slice*(self: var RollingHash, left, right: int): int =
    return floorMod(self.h[right] - modMul(self.h[left], self.pw[right - left], self.MOD), self.MOD)

  proc concat*(self: var RollingHash, left1, right1, left2, right2: int): int =
    let
      s = self.slice(left1, right1)
      t = self.slice(left2, right2)
    return (modMul(s, self.pw[right2 - left2], self.MOD) + t) mod self.MOD

when isMainModule:
  var
    N = inputInt()
    S, T = input()
  
  let
    tr = {'R': 0, 'G': 1, 'B': 2}.toTable
    numS = collect(newSeq):
      for si in S: tr[si]
    numT = collect(newSeq):
      for ti in T: tr[ti]
  
  var t1, t2, t3: seq[int]
  for ti in numT:
    if ti == 0:
      t1.add(0)
      t2.add(2)
      t3.add(1)
    elif ti == 1:
      t1.add(2)
      t2.add(1)
      t3.add(0)
    else:
      t1.add(1)
      t2.add(0)
      t3.add(2)
  
  var
    rhs = initRollingHash(numS)
    rh1 = initRollingHash(t1)
    rh2 = initRollingHash(t2)
    rh3 = initRollingHash(t3)
  
  var ans = 0
  for i in 0..<N:
    let
      sls = rhs.slice(0, N - i)
      sl1 = rh1.slice(i, N)
      sl2 = rh2.slice(i, N)
      sl3 = rh3.slice(i, N)
    if sls in [sl1, sl2, sl3]:
      ans.inc
  for i in 1..<N:
    let
      sls = rhs.slice(i, N)
      sl1 = rh1.slice(0, N - i)
      sl2 = rh2.slice(0, N - i)
      sl3 = rh3.slice(0, N - i)
    if sls in [sl1, sl2, sl3]:
      ans.inc
  echo ans
