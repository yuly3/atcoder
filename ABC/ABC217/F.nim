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

when not declared ATCODER_BINOMIAL_COEFFICIENTS_HPP:
  const ATCODER_BINOMIAL_COEFFICIENTS_HPP* = 1
  
  type BinomialCoefficients*[N, M: static int] = object
    fact, factInv, inv: array[0..N - 1, int]
  
  proc initBinomialCoefficients*(N, M: static int): BinomialCoefficients[N, M] =
    return BinomialCoefficients[N, M]()
  
  proc preprocess*[N, M: static int](self: var BinomialCoefficients[N, M]) =
    self.fact[0] = 1; self.fact[1] = 1
    self.factInv[0] = 1; self.factInv[1] = 1
    self.inv[1] = 1
    for i in 2..<N:
      self.fact[i] = floorMod(self.fact[i - 1]*i, M)
      self.inv[i] = floorMod(-self.inv[M mod i]*(M div i), M)
      self.factInv[i] = floorMod(self.factInv[i - 1]*self.inv[i], M)
  
  proc nCr*[N, M: static int](self: var BinomialCoefficients[N, M], n, r: int): int =
    if r < 0 or n < r:
      return 0
    let r = min(r, n - r)
    return (self.fact[n]*self.factInv[r] mod M)*self.factInv[n - r] mod M
  
  proc nHr*[N, M: static int](self: var BinomialCoefficients[N, M], n, r: int): int =
    return self.nCr(n + r - 1, r)
  
  proc nPr*[N, M: static int](self: var BinomialCoefficients[N, M], n, r: int): int =
    if r < 0 or n < r:
      return 0
    return self.fact[n]*self.factInv[n - r] mod M

when isMainModule:
  const MOD = 998244353
  var N, M: int
  (N, M) = inputInts()
  var edges: array[401, array[401, bool]]
  var ai, bi: int
  for _ in 0..<M:
    (ai, bi) = inputInts().mapIt(it - 1)
    edges[ai][bi] = true
    edges[bi][ai] = true
  
  var dp: array[401, array[401, int]]
  var binom: BinomialCoefficients[410, MOD]
  binom.preprocess()
  
  for d in countup(0, 2*N, 2):
    for left in 0..2*N:
      let right = left + d
      if right > 2*N:
        break
      if left == right:
        dp[left][right] = 1
        continue
      for mid in countup(left + 1, right - 1, 2):
        if edges[left][mid]:
          var cnt = dp[left + 1][mid]*dp[mid + 1][right] mod MOD
          cnt *= binom.nCr((right - left) div 2, (mid - left + 1) div 2)
          dp[left][right] += cnt
          dp[left][right] %= MOD
  echo dp[0][2*N]
