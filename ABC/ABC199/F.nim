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

proc modPow*(a, k: int, MOD=10^9 + 7): int =
  var
    a = a
    k = k
  result = 1
  while k > 0:
    if bitand(k, 1) == 1:
      result = floorMod(result*a, MOD)
    a = floorMod(a*a, MOD)
    k = k shr 1

proc modInv*(a: int, MOD=10^9 + 7): int =
  return modPow(a, MOD - 2, MOD)

proc matMul*(A, B: seq[seq[int]], MOD=10^9 + 7): seq[seq[int]] =
  let
    N0 = A.len
    N1 = B[0].len
    N2 = A[0].len
  result = newSeqWith(N0, newSeq[int](N1))
  for i in 0..<N0:
    for j in 0..<N1:
      for k in 0..<N2:
        result[i][j] = floorMod(result[i][j] + A[i][k]*B[k][j], MOD)

proc matVecMul*(A: seq[seq[int]], B: seq[int], MOD=10^9 + 7): seq[int] =
  let N = B.len
  result = newSeq[int](N)
  for i in 0..<N:
    for j in 0..<N:
      result[i] = floorMod(result[i] + floorMod(A[i][j]*B[j], MOD), MOD)

proc matPow*(A: seq[seq[int]], K: int, MOD=10^9 + 7): seq[seq[int]] =
  let N = len(A)
  var
    A = A
    K = K
  result = newSeqWith(N, newSeq[int](N))
  for i in 0..<N:
    result[i][i] = 1
  while K > 0:
    if bitand(K, 1) == 1:
      result = matMul(result, A, MOD)
    A = matMul(A, A, MOD)
    K = K shr 1

when isMainModule:
  const MOD = 10^9 + 7
  var N, M, K: int
  (N, M, K) = inputInts()
  let A = inputInts()
  var
    graph: array[100, seq[int]]
    xi, yi: int
  for _ in 0..<M:
    (xi, yi) = inputInts().mapIt(it - 1)
    graph[xi].add(yi)
    graph[yi].add(xi)
  
  var matA = newSeqWith(N, newSeq[int](N))
  for fr in 0..<N:
    matA[fr][fr] = floorMod(matA[fr][fr] + floorMod((M - graph[fr].len)*modInv(M), MOD), MOD)
    for to in graph[fr]:
      matA[fr][fr] = floorMod(matA[fr][fr] + floorMod(modInv(2)*modInv(M), MOD), MOD)
      matA[fr][to] = floorMod(matA[fr][to] + floorMod(modInv(2)*modInv(M), MOD), MOD)
  
  let
    matB = matPow(matA, K)
    ans = matVecMul(matB, A)
  echo ans.join("\n")
