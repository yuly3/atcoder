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
  proc `&=`*[string](s: var string, t: string) = s = s & t

when not declared ATCODER_STRING_HPP:
  const ATCODER_STRING_HPP* = 1
  
  import std/algorithm, std/sequtils
  
  proc sa_naive*(s:seq[int]):seq[int] =
    let n = s.len
    var sa = newSeq[int](n)
    for i in 0..<n:sa[i] = i
    sa.sort() do (l, r:int) -> int:
      if l == r: return 0
      var (l, r) = (l, r)
      while l < n and r < n:
        if s[l] != s[r]: return cmp[int](s[l], s[r])
        l.inc;r.inc
      return cmp[int](n, l)
    return sa
  
  proc sa_doubling*(s:seq[int]):seq[int] =
    let n = s.len
    var
      sa, tmp = newSeq[int](n)
      rnk = s
    for i in 0..<n:sa[i] = i
    var k = 1
    while k < n:
      proc cmp0(x, y:int):int =
        if rnk[x] != rnk[y]: return cmp[int](rnk[x], rnk[y])
        let
          rx = if x + k < n: rnk[x + k] else: -1
          ry = if y + k < n: rnk[y + k] else: -1
        return cmp[int](rx, ry)
      sa.sort(cmp0)
      tmp[sa[0]] = 0
      for i in 1..<n:
        tmp[sa[i]] = tmp[sa[i - 1]] + (if cmp0(sa[i - 1], sa[i]) < 0: 1 else: 0)
      swap(tmp, rnk)
      k = k shl 1
    return sa
  
  # SA-IS, linear-time suffix array construction
  # Reference:
  # G. Nong, S. Zhang, and W. H. Chan,
  # Two Efficient Algorithms for Linear Time Suffix Array Construction
  proc sa_is*(s:seq[int], upper:int, THRESHOLD_NAIVE:static[int] = 10, THRESHOLD_DOUBLING:static[int] = 40):seq[int] =
    let n = s.len
    if n == 0: return @[]
    if n == 1: return @[0]
    if n == 2:
      if s[0] < s[1]:
        return @[0, 1]
      else:
        return @[1, 0]
    if n < THRESHOLD_NAIVE:
      return sa_naive(s)
    if n < THRESHOLD_DOUBLING:
      return sa_doubling(s)
    
    var sa, ls = newSeq[int](n)
    for i in countdown(n - 2, 0):
      ls[i] = if s[i] == s[i + 1]: ls[i + 1] else: (s[i] < s[i + 1]).int
    var sum_l, sum_s = newSeq[int](upper + 1)
    for i in 0..<n:
      if ls[i] == 0:
        sum_s[s[i]].inc
      else:
        sum_l[s[i] + 1].inc
    for i in 0..upper:
      sum_s[i] += sum_l[i]
      if i < upper: sum_l[i + 1] += sum_s[i]
    
    proc induce(lms:seq[int]):auto =
      sa.fill(-1)
      var buf = sum_s
      for d in lms:
        if d == n: continue
        sa[buf[s[d]]] = d
        buf[s[d]].inc
      buf = sum_l
      sa[buf[s[n - 1]]] = n - 1
      buf[s[n - 1]].inc
      for i in 0..<n:
        let v = sa[i]
        if v >= 1 and ls[v - 1] == 0:
          sa[buf[s[v - 1]]] = v - 1
          buf[s[v - 1]].inc
      buf = sum_l
      for i in countdown(n - 1, 0):
        let v = sa[i]
        if v >= 1 and ls[v - 1] != 0:
          buf[s[v - 1] + 1].dec
          sa[buf[s[v - 1] + 1]] = v - 1
    
    var lms_map = newSeqWith(n + 1, -1)
    var m = 0
    for i in 1..<n:
      if ls[i - 1] == 0 and ls[i] != 0:
        lms_map[i] = m
        m.inc
    var lms = newSeqOfCap[int](m)
    for i in 1..<n:
      if ls[i - 1] == 0 and ls[i] != 0:
        lms.add(i)
    
    induce(lms)
    
    if m != 0:
      var sorted_lms = newSeqOfCap[int](m)
      for v in sa:
        if lms_map[v] != -1: sorted_lms.add(v)
      var
        rec_s = newSeq[int](m)
        rec_upper = 0;
      rec_s[lms_map[sorted_lms[0]]] = 0
      for i in 1..<m:
        var (l, r) = (sorted_lms[i - 1], sorted_lms[i])
        let
          end_l = if lms_map[l] + 1 < m: lms[lms_map[l] + 1] else: n
          end_r = if lms_map[r] + 1 < m: lms[lms_map[r] + 1] else: n
        var same = true
        if end_l - l != end_r - r:
          same = false
        else:
          while l < end_l:
            if s[l] != s[r]:
              break
            l.inc
            r.inc
          if l == n or s[l] != s[r]: same = false
        if not same: rec_upper.inc
        rec_s[lms_map[sorted_lms[i]]] = rec_upper
      
      let rec_sa =
        sa_is[THRESHOLD_NAIVE, THRESHOLD_DOUBLING](rec_s, rec_upper)
      
      for i in 0..<m:
        sorted_lms[i] = lms[rec_sa[i]]
      induce(sorted_lms)
    return sa
  
  proc suffix_array*(s:seq[int], upper:int):seq[int] =
    assert 0 <= upper
    for d in s:
      assert 0 <= d and d <= upper
    return sa_is(s, upper)
  
  proc suffix_array*[T](s:seq[T]):seq[int] =
    let n = s.len
    var idx = newSeq[int](n)
    for i in 0..<n: idx[i] = i
    idx.sort(proc(l,r:int):int = cmp[int](s[l], s[r]))
    var s2 = newSeq[int](n)
    var now = 0
    for i in 0..<n:
      if i != 0 and s[idx[i - 1]] != s[idx[i]]: now.inc
      s2[idx[i]] = now
    return sa_is(s2, now)
  
  proc suffix_array*(s:string):seq[int] =
    return sa_is(s.mapIt(it.int), 255);
  
  # Reference:
  # T. Kasai, G. Lee, H. Arimura, S. Arikawa, and K. Park,
  # Linear-Time Longest-Common-Prefix Computation in Suffix Arrays and Its
  # Applications
  proc lcp_array*[T](s:seq[T], sa:seq[int]):seq[int] =
    let n = s.len
    assert n >= 1
    var rnk = newSeq[int](n)
    for i in 0..<n:
      rnk[sa[i]] = i
    var lcp = newSeq[int](n - 1)
    var h = 0;
    for i in 0..<n:
      if h > 0: h.dec
      if rnk[i] == 0: continue
      let j = sa[rnk[i] - 1]
      while j + h < n and i + h < n:
        if s[j + h] != s[i + h]: break
        h.inc
      lcp[rnk[i] - 1] = h
    return lcp
  
  proc lcp_array*(s:string, sa:seq[int]):seq[int] = lcp_array(s.mapIt(it.int), sa)
  
  # Reference:
  # D. Gusfield,
  # Algorithms on Strings, Trees, and Sequences: Computer Science and
  # Computational Biology
  proc z_algorithm*[T](s:seq[T]):seq[T] =
    let n = s.len
    if n == 0: return @[]
    var z = newSeq[int](n)
    z[0] = 0
    var j = 0
    for i in 1..<n:
      var k = z[i].addr
      k[] = if j + z[j] <= i: 0 else: min(j + z[j] - i, z[i - j])
      while i + k[] < n and s[k[]] == s[i + k[]]: k[].inc
      if j + z[j] < i + z[i]: j = i
    z[0] = n
    return z
  
  proc z_algorithm*(s:string):auto = z_algorithm(s.mapIt(it.int))

iterator f(sa, lcpa: seq[int]): (int, int) =
  var stack: seq[(int, int)]
  var sm = 0
  for i, lcp in lcpa:
    var cnt = 1
    while stack.len > 0 and stack[^1][0] >= lcp:
      let (V, C) = stack.pop()
      cnt += C
      sm -= V*C
    stack.add((lcp, cnt))
    sm += lcp*cnt
    yield (sa[i + 1], sm)

when isMainModule:
  var
    N = inputInt()
    S = input()
  
  var
    sa = suffix_array(S)
    lcpa = lcp_array(S, sa)
    ans = toSeq(countdown(N, 1))
  
  for (i, cnt) in f(sa, lcpa):
    ans[i] += cnt
  sa.reverse()
  lcpa.reverse()
  for (i, cnt) in f(sa, lcpa):
    ans[i] += cnt
  echo ans.join("\n")
