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

when isMainModule:
  echo "Hello, AtCoder!!"
