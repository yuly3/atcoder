import
  algorithm, bitops, deques, heapqueue, math, macros, sets, sequtils,
  strformat, strutils, sugar, tables

proc makeDivisors*(n: Positive): seq[int] =
  let limit = n.float.sqrt.ceil.int
  for i in 1..limit:
    if n mod i == 0:
      result.add(i)
      if i != n div i:
        result.add(n div i)

proc factorization*(n: Positive): seq[tuple[x: int, exp: int]] =
  var tmp = n
  let limit = n.float.sqrt.ceil.int
  for i in 2..limit:
    if floorMod(tmp, i) == 0:
      var exp: int
      while floorMod(tmp, i) == 0:
        inc exp
        tmp = floorDiv(tmp, i)
      result.add((i, exp))
  if tmp != 1:
    result.add((tmp, 1))
  if result.len == 0:
    result.add((n, 1))

proc eratosthenes*(n: Positive): seq[int] =
  var isPrime = newSeqWith(n + 1, true)
  isPrime[0] = false; isPrime[1] = false
  for p in 2..n:
    if not isPrime[p]:
      continue
    result.add(p)
    for i in countup(2*p, n, p):
      isPrime[i] = false

proc invGcd*(a, b: int): (int, int) =
  let a = floorMod(a, b)
  if a == 0:
    return (b, 0)

  var
    (s, t) = (b, a)
    (m0, m1) = (0, 1)
  while t != 0:
    let
      u = floorDiv(s, t)
    s -= t * u
    m0 -= m1 * u
    (s, t) = (t, s)
    (m0, m1) = (m1, m0)

  if m0 < 0:
    m0 += floorDiv(b, s)
  return (s, m0)

proc crt*(r, m: openArray[int]): (int, int) =
  var (r0, m0) = (0, 1)
  for i in 0..<r.len:
    var (r1, m1) = (floorMod(r[i], m[i]), m[i])
    if m0 < m1:
      (r0, r1) = (r1, r0)
      (m0, m1) = (m1, m0)
    if floorMod(m0, m1) == 0:
      if floorMod(r0, m1) != r1:
        return (0, 0)
      continue

    let (g, im) = invGcd(m0, m1)
    if floorMod(r1 - r0, g) != 0:
      return (0, 0)

    let u1 = floorDiv(m0*m1, g)
    r0 += floorMod(floorDiv(r1 - r0, g)*m0*im, u1)
    m0 = u1
  return (r0, m0)

proc modPow*(a: int, k: Natural, MOD = 10^9 + 7): int =
  var
    a = a
    k = k
  result = 1
  while k > 0:
    if bitand(k, 1) == 1:
      result = floorMod(result*a, MOD)
    a = floorMod(a*a, MOD)
    k = k shr 1

proc modInv*(a: int, MOD = 10^9 + 7): int =
  return modPow(a, MOD - 2, MOD)

proc modInv2*(a, m: int): int =
  if a == 1:
    return 1
  return m + (1 - m*modInv2(m mod a, a)) div a

proc babyStepGiantStep*(a, m: int): int =
  var a = a mod m
  if gcd(a, m) != 1:
    return -1

  let lim = floor(sqrt(m.float)).int
  var mp = initTable[int, int]()
  var s = a
  for i in 1..lim:
    if s notin mp:
      mp[s] = i
    s = s*a mod m

  let g = modInv2(modPow(a, lim, m), m)
  var x = 1
  for i in 0..<m:
    if x in mp:
      return lim*i + mp[x]
    x = x*g mod m

proc matVecMul*(A: seq[seq[int]], B: seq[int], MOD = 10^9 + 7): seq[int] =
  let N = B.len
  result = newSeq[int](N)
  for i in 0..<N:
    for j in 0..<N:
      result[i] = floorMod(result[i] + floorMod(A[i][j]*B[j], MOD), MOD)

proc matMul*(A, B: seq[seq[int]], M = 10^9 + 7): seq[seq[int]] =
  let
    N0 = A.len
    N1 = B[0].len
    N2 = A[0].len
  result = newSeqWith(N0, newSeq[int](N1))
  for i in 0..<N0:
    for j in 0..<N1:
      for k in 0..<N2:
        result[i][j] = floorMod(result[i][j] + A[i][k]*B[k][j], M)

proc matPow*(A: seq[seq[int]], K: Natural, M = 10^9 + 7): seq[seq[int]] =
  let N = len(A)
  var
    A = A
    K = K
  result = newSeqWith(N, newSeq[int](N))
  for i in 0..<N:
    result[i][i] = 1
  while K > 0:
    if bitand(K, 1) == 1:
      result = matMul(result, A, M)
    A = matMul(A, A, M)
    K = K shr 1

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

  proc initRollingHash*(s: openArray[int], base = 10007, MOD = (1 shl 61) -
      1): RollingHash =
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
    return floorMod(self.h[right] - modMul(self.h[left], self.pw[right - left],
        self.MOD), self.MOD)

  proc concat*(self: var RollingHash, left1, right1, left2, right2: int): int =
    let
      s = self.slice(left1, right1)
      t = self.slice(left2, right2)
    return (modMul(s, self.pw[right2 - left2], self.MOD) + t) mod self.MOD

when not declared ATCODER_UNIONFIND_HPP:
  const ATCODER_UNIONFIND_HPP* = 1

  type
    UnionFind* = ref object
      n: Positive
      cnt: int
      parents: seq[int]

  proc initUnionFind*(n: Positive): UnionFind =
    return UnionFind(n: n, cnt: n, parents: newSeqWith(n, -1))

  proc find*(self: var UnionFind, x: Natural): Natural =
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

  proc union*(self: var UnionFind, x, y: Natural) =
    var
      root_x = self.find(x)
      root_y = self.find(y)

    if root_x == root_y:
      return
    if self.parents[root_y] < self.parents[root_x]:
      (root_x, root_y) = (root_y, root_x)
    self.parents[root_x] += self.parents[root_y]
    self.parents[root_y] = root_x
    self.cnt.dec

  proc size*(self: var UnionFind, x: Natural): Positive =
    return -self.parents[self.find(x)]

  proc same*(self: var UnionFind, x, y: Natural): bool =
    return self.find(x) == self.find(y)

  proc members*(self: var UnionFind, x: Natural): seq[int] =
    let root = self.find(x)
    return toSeq(0..<int(self.n)).filterIt(self.find(it) == root)

  proc roots*(self: var UnionFind): seq[int] =
    return toSeq(0..<int(self.n)).filterIt(self.parents[it] < 0)

when not declared ATCODER_BINOMIAL_COEFFICIENTS_HPP:
  const ATCODER_BINOMIAL_COEFFICIENTS_HPP * = 1

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
      ide_ele: T
      data: seq[T]
      fold: (T, T) -> T
      eval: (T, K) -> T

  proc initSegmentTree*[T, K](size: Positive, ide_ele: T, fold: (T, T) -> T,
      eval: (T, K) -> T): SegmentTree[T, K] =
    let
      N0 = 1 shl bitLength(size - 1)
      data = newSeqWith(2*N0, ide_ele)
    return SegmentTree[T, K](N0: N0, ide_ele: ide_ele, data: data, fold: fold, eval: eval)

  proc toSegmentTree*[T, K](init_value: openArray[T], ide_ele: T, fold: (T,
      T) -> T, eval: (T, K) -> T): SegmentTree[T, K] =
    let N0 = 1 shl bitLength(init_value.len - 1)
    var data = newSeqWith(2*N0, ide_ele)
    for i, x in init_value:
      data[i + N0 - 1] = x
    for i in countdown(N0 - 2, 0):
      data[i] = fold(data[2*i + 1], data[2*i + 2])
    return SegmentTree[T, K](N0: N0, ide_ele: ide_ele, data: data, fold: fold, eval: eval)

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
    result = self.ide_ele

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

  proc binarySearchRight*[T, K](self: var SegmentTree[T, K], left,
      right: Natural, x: T): int =
    return self.binarySearchRightSub(left, right, x, 0, 0, self.N0)

  proc binarySearchRightSub*[T, K](self: var SegmentTree[T, K], a, b: Natural,
      x: T, k, left, right: Natural): int =
    if x < self.data[k] or right <= a or b <= left:
      return a - 1
    if self.N0 - 1 <= k:
      return k - self.N0 + 1
    let vr = self.binarySearchRightSub(a, b, x, 2*k + 2, (left + right) div 2, right)
    if vr != a - 1:
      return vr
    return self.binarySearchRightSub(a, b, x, 2*k + 1, left, (left + right) div 2)

  proc binarySearchLeft*[T, K](self: var SegmentTree[T, K], left,
      right: Natural, x: T): int =
    return self.binarySearchLeftSub(left, right, x, 0, 0, self.N0)

  proc binarySearchLeftSub*[T, K](self: var SegmentTree[T, K], a, b: Natural,
      x: T, k, left, right: Natural): int =
    if x < self.data[k] or right <= a or b <= left:
      return b
    if self.N0 - 1 <= k:
      return k - self.N0 + 1
    let vl = self.binarySearchLeftSub(a, b, x, 2*k + 1, left, (left + right) div 2)
    if vl != b:
      return vl
    return self.binarySearchLeftSub(a, b, x, 2*k + 2, (left + right) div 2, right)

when not declared ATCODER_LAZYSEGTREE_HPP:
  const ATCODER_LAZYSEGTREE_HPP* = 1

  type
    LazySegmentTree*[T, K] = ref object
      LV: Natural
      N0: Positive
      ide_ele: T
      lazy_ide_ele: K
      data: seq[T]
      lazy_data: seq[K]
      fold: (T, T) -> T
      eval: (T, K) -> T
      merge: (K, K) -> K
      propagatesWhenUpdating: bool

  proc initLazySegmentTree*[T, K](size: Positive, ide_ele: T, lazy_ide_ele: K,
      fold: (T, T) -> T, eval: (T, K) -> T, merge: (K, K) -> K,
      propagatesWhenUpdating = false): LazySegmentTree[T, K] =
    let
      LV = bitLength(size - 1)
      N0 = 1 shl LV
      data = newSeqWith(2*N0, ide_ele)
      lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    return LazySegmentTree[T, K](LV: LV, N0: N0, ide_ele: ide_ele,
        lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data,
        fold: fold, eval: eval, merge: merge,
        propagatesWhenUpdating: propagatesWhenUpdating)

  proc toLazySegmentTree*[T, K](init_value: openArray[T], ide_ele: T,
      lazy_ide_ele: K, fold: (T, T) -> T, eval: (T, K) -> T, merge: (K, K) -> K,
      propagatesWhenUpdating = false): LazySegmentTree[T, K] =
    let
      LV = bitLength(init_value.len - 1)
      N0 = 1 shl LV
      lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    var data = newSeqWith(2*N0, ide_ele)
    for i, x in init_value:
      data[i + N0 - 1] = x
    for i in countdown(N0 - 2, 0):
      data[i] = fold(data[2*i + 1], data[2*i + 2])
    return LazySegmentTree[T, K](LV: LV, N0: N0, ide_ele: ide_ele,
        lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data,
        fold: fold, eval: eval, merge: merge,
        propagatesWhenUpdating: propagatesWhenUpdating)

  iterator gindex*[T, K](self: var LazySegmentTree[T, K], left,
      right: Natural): Natural =
    var
      L = (left + self.N0) shr 1
      R = (right + self.N0) shr 1
      lc = if (left and 1) == 1: 0 else: bitLength(L and -L)
      rc = if (right and 1) == 1: 0 else: bitLength(R and -R)
    for i in 0..<self.LV:
      if rc <= i:
        yield R
      if L < R and lc <= i:
        yield L
      L = L shr 1
      R = R shr 1

  proc propagates*[T, K](self: var LazySegmentTree[T, K], ids: seq[Natural]) =
    var
      idx: Natural
      v: K
    for id in reversed(ids):
      idx = id - 1
      v = self.lazy_data[idx]
      if v == self.lazy_ide_ele:
        continue
      self.data[2*idx + 1] = self.eval(self.data[2*idx + 1], v)
      self.data[2*idx + 2] = self.eval(self.data[2*idx + 2], v)
      self.lazy_data[2*idx + 1] = self.merge(self.lazy_data[2*idx + 1], v)
      self.lazy_data[2*idx + 2] = self.merge(self.lazy_data[2*idx + 2], v)
      self.lazy_data[idx] = self.lazy_ide_ele

  proc update*[T, K](self: var LazySegmentTree[T, K], left, right: Natural, x: K) =
    let ids = toSeq(self.gindex(left, right))
    if self.propagatesWhenUpdating:
      self.propagates(ids)
    var
      L = left + self.N0
      R = right + self.N0

    while L < R:
      if (L and 1) == 1:
        self.lazy_data[L - 1] = self.merge(self.lazy_data[L - 1], x)
        self.data[L - 1] = self.eval(self.data[L - 1], x)
        inc L
      if (R and 1) == 1:
        dec R
        self.lazy_data[R - 1] = self.merge(self.lazy_data[R - 1], x)
        self.data[R - 1] = self.eval(self.data[R - 1], x)
      L = L shr 1
      R = R shr 1

    var idx: Natural
    for id in ids:
      idx = id - 1
      self.data[idx] = self.fold(self.data[2*idx + 1], self.data[2*idx + 2])
      if self.lazy_data[idx] != self.lazy_ide_ele:
        self.data[idx] = self.eval(self.data[idx], self.lazy_data[idx])

  proc query*[T, K](self: var LazySegmentTree[T, K], left, right: Natural): T =
    self.propagates(toSeq(self.gindex(left, right)))
    var
      L = left + self.N0
      R = right + self.N0
    result = self.ide_ele

    while L < R:
      if (L and 1) == 1:
        result = self.fold(result, self.data[L - 1])
        inc L
      if (R and 1) == 1:
        dec R
        result = self.fold(result, self.data[R - 1])
      L = L shr 1
      R = R shr 1

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

  proc initDualSegmentTree*[T](size: Positive, lazy_ide_ele: T, merge: (T, T) ->
      T, propagatesWhenUpdating = false): DualSegmentTree[T] =
    let
      LV = bitLength(size - 1)
      N0 = 1 shl LV
      lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    return DualSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele,
        lazy_data: lazy_data, merge: merge,
        propagatesWhenUpdating: propagatesWhenUpdating)

  proc toDualSegmentTree*[T](init_value: openArray[T], lazy_ide_ele: T, merge: (
      T, T) -> T, propagatesWhenUpdating = false): DualSegmentTree[T] =
    let
      LV = bitLength(init_value.len - 1)
      N0 = 1 shl LV
    var lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    for i, x in init_value:
      lazy_data[i + N0 - 1] = x
    return DualSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele,
        lazy_data: lazy_data, merge: merge,
        propagatesWhenUpdating: propagatesWhenUpdating)

  proc propagate*[T](self: var DualSegmentTree[T], k: Natural) =
    for i in countdown(self.LV, 1):
      let t = (k shr i) - 1
      if self.lazy_data[t] != self.lazy_ide_ele:
        self.lazy_data[2*t + 1] = self.merge(self.lazy_data[2*t + 1],
            self.lazy_data[t])
        self.lazy_data[2*t + 2] = self.merge(self.lazy_data[2*t + 2],
            self.lazy_data[t])
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

when not declared ATCODER_LOWESTCOMMONANCESTOR_HPP:
  const ATCODER_LOWESTCOMMONANCESTOR_HPP * = 1

  type
    LowestCommonAncestor* = ref object
      size: Positive
      LV: Natural
      depth: seq[int]
      tree, parent: seq[seq[int]]

  proc initLowestCommonAncestor*(tree: var seq[seq[
      int]]): LowestCommonAncestor =
    let
      size = tree.len
      LV = bitLength(size)
      depth = newSeq[int](size)
      parent = newSeqWith(LV, newSeqWith(size, -1))
    return LowestCommonAncestor(size: size, LV: LV, depth: depth, tree: tree,
        parent: parent)

  proc build*(self: var LowestCommonAncestor, root: Natural) =
    var que = initDeque[(int, int, int)]()
    que.addLast((root, -1, 0))

    var cur, par, dist: int
    while que.len != 0:
      (cur, par, dist) = que.popFirst()
      self.parent[0][cur] = par
      self.depth[cur] = dist
      for child in self.tree[cur]:
        if child != par:
          self.depth[child] = dist + 1
          que.addLast((child, cur, dist + 1))

    for i in 1..<self.LV:
      for j in 0..<self.size:
        let k = self.parent[i - 1][j]
        if k != -1:
          self.parent[i][j] = self.parent[i - 1][k]

  proc query*(self: var LowestCommonAncestor, u, v: Natural): int =
    var (u, v) = (u, v)
    if self.depth[v] < self.depth[u]:
      (u, v) = (v, u)
    for i in 0..<self.LV:
      if (((self.depth[v] - self.depth[u]) shr i) and 1) == 1:
        v = self.parent[i][v]
    if u == v:
      return u

    for i in countdown(self.LV - 1, 0):
      if self.parent[i][u] != self.parent[i][v]:
        u = self.parent[i][u]
        v = self.parent[i][v]
    return self.parent[0][v]

  proc dist*(self: var LowestCommonAncestor, u, v: Natural): int =
    let ancestor = self.query(u, v)
    return self.depth[u] + self.depth[v] - 2*self.depth[ancestor]

when not declared ATCODER_RAND_HPP:
  const ATCODER_RAND_HPP* = 1

  proc xor64(x: uint64): uint64 {.inline.} =
    result = x xor ((x shl 7) and 0xffffffff.uint64)
    result = result xor (result shr 9)

when not declared ATCODER_SQUARESKIPLIST_HPP:
  const ATCODER_SQUARESKIPLIST_HPP* = 1

  type
    SquareSkipList*[T] = ref object
      square: Natural
      rand_y: uint64
      layer1: seq[T]
      layer0: seq[seq[T]]
      cmpFunc: (T, T) -> int

  proc initSquareSkipList*[T](inf: T, cmpFunc: (T, T) -> int,
      square = 1000): SquareSkipList[T] =
    var
      layer1 = @[inf]
      layer0 = newSeqWith(1, newSeq[T]())
    return SquareSkipList[T](square: square, rand_y: 88172645463325252.uint64,
        layer1: layer1, layer0: layer0, cmpFunc: cmpFunc)

  proc add*[T](self: var SquareSkipList[T], x: T) =
    self.rand_y = xor64(self.rand_y)

    if self.rand_y.int mod self.square == 0:
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

  proc pop*[T](self: var SquareSkipList[T], k: Natural): T =
    var
      s = -1
      i: int
    for ii, l0 in self.layer0:
      s += l0.len + 1
      i = ii
      if k <= s:
        break
    if s == k:
      self.layer0[i] = concat(self.layer0[i], self.layer0[i + 1])
      self.layer0.delete(i + 1, i + 1)
      result = self.layer1[i]
      self.layer1.delete(i, i)
    else:
      let j = self.layer0[i].len + k - s
      result = self.layer0[i][j]
      self.layer0[i].delete(j, j)

  proc popMax*[T](self: var SquareSkipList[T]): T =
    if self.layer0[^1].len != 0:
      return self.layer0[^1].pop()
    elif 1 < self.layer1.len:
      self.layer0.delete(self.layer0.len - 1, self.layer0.len - 1)
      result = self.layer1[^2]
      self.layer1.delete(self.layer1.len - 2, self.layer1.len - 2)
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
    return self.layer0[ii][^(s - k)]

  proc min*[T](self: var SquareSkipList[T]): T =
    if self.layer0[0].len != 0:
      return self.layer0[0][0]
    return self.layer1[0]

  proc max*[T](self: var SquareSkipList[T]): T =
    if self.layer0[^1].len != 0:
      return self.layer0[^1][^1]
    elif 1 < self.layer1.len:
      return self.layer1[^2]
    return self.layer1[^1]

when not declared ATCODER_HLDECOMPOSITION_HPP:
  const ATCODER_HLDECOMPOSITION_HPP* = 1

  type
    HeavyLightDecomposition* = ref object
      graph: seq[seq[Natural]]
      pathRoot, pathParent, left, right: seq[Natural]

  proc initHeavyLightDecomposition*(size: Positive): HeavyLightDecomposition =
    var
      graph = newSeqWith(size, newSeq[Natural]())
      emptySeq = newSeq[Natural]()
    return HeavyLightDecomposition(graph: graph, pathRoot: emptySeq,
        pathParent: emptySeq, left: emptySeq, right: emptySeq)

  proc addEdge*(self: var HeavyLightDecomposition, a, b: Natural) =
    self.graph[a].add(b)
    self.graph[b].add(a)

  proc build*(self: var HeavyLightDecomposition, root: Natural) =
    var
      stack = @[(root, root)]
      q = newSeq[Natural]()
      v, p: Natural

    while stack.len != 0:
      (v, p) = stack.pop()
      q.add(v)
      for i, to in self.graph[v]:
        if to == p:
          self.graph[v][i] = self.graph[v][^1]
          let _ = self.graph[v].pop()
          break
      for to in self.graph[v]:
        stack.add((to, v))

    let n = self.graph.len
    var size = newSeqWith(n, 1)
    for v in reversed(q):
      for i, to in self.graph[v]:
        size[v] += size[to]
        if size[self.graph[v][0]] < size[to]:
          (self.graph[v][0], self.graph[v][i]) = (self.graph[v][i], self.graph[
              v][0])

    self.pathRoot = newSeqWith(n, root)
    self.pathParent = newSeqWith(n, root)
    self.left = newSeq[Natural](n)
    self.right = newSeq[Natural](n)
    var
      k = 0
      stack1 = @[(root, 0)]
      op: int
      to: Natural
    while stack1.len != 0:
      (v, op) = stack1.pop()
      if op == 1:
        self.right[v] = k
        continue
      self.left[v] = k
      inc k
      stack1.add((v, 1))
      if 1 < self.graph[v].len:
        for i, to in self.graph[v][1..^1]:
          self.pathRoot[to] = to
          self.pathParent[to] = v
          stack1.add((to, 0))
      if self.graph[v].len != 0:
        to = self.graph[v][0]
        self.pathRoot[to] = self.pathRoot[v]
        self.pathParent[to] = self.pathParent[v]
        stack1.add((to, 0))

  proc subTree*(self: var HeavyLightDecomposition, v: Natural): (Natural, Natural) =
    return (self.left[v], self.right[v])

  proc path*(self: var HeavyLightDecomposition, v, u: Natural,
      edgeFlg: bool = false): seq[(int, int)] =
    var
      x = v
      y = u
      res = newSeq[(int, int)]()
      p: Natural
    while self.pathRoot[x] != self.pathRoot[y]:
      if self.left[x] < self.left[y]:
        p = self.pathRoot[y]
        res.add((self.left[p], self.left[y] + 1))
        y = self.pathParent[y]
      else:
        p = self.pathRoot[x]
        res.add((self.left[p], self.left[x] + 1))
        x = self.pathParent[x]
    if edgeFlg:
      res.add((min(self.left[x], self.left[y]) + 1, max(self.left[x], self.left[
          y]) + 1))
    else:
      res.add((min(self.left[x], self.left[y]), max(self.left[x], self.left[
          y]) + 1))
    return res

  proc id*(self: var HeavyLightDecomposition, v: Natural): Natural =
    return self.left[v]

when not declared ATCODER_REROOTING_HPP:
  const ATCODER_REROOTING_HPP* = 1

  type RerootingTree[N: static int, T] = object
    tree: array[0..N - 1, seq[int]]
    sz, depth, parent: array[0..N - 1, int]
    dp1, dp2, left, right: array[0..N - 1, T]
    order: seq[int]
    op: (T, int, int) -> T
    merge: (T, T) -> T
    ide: T

  proc initRerootingTree*[N: static int, T](op: (T, int, int) -> T, merge: (T,
      T) -> T, ide: T): RerootingTree[N, T] =
    return RerootingTree[N, T](order: newSeq[int](), op: op, merge: merge, ide: ide)

  proc addEdge*[N: static int, T](self: var RerootingTree[N, T], u, v: int) =
    self.tree[u].add(v)
    self.tree[v].add(u)

  proc topologicalSort*[N: static int, T](self: var RerootingTree[N, T], root: int) =
    self.sz.fill(1)
    self.depth.fill(-1)
    self.depth[root] = 0
    self.order.add(root)
    var stack = @[root]
    while stack.len > 0:
      let cur = stack.pop()
      for to in self.tree[cur]:
        if self.depth[to] != -1:
          continue
        self.parent[to] = cur
        self.depth[to] = self.depth[cur] + 1
        self.order.add(to)
        stack.add(to)
    for fr in reversed(self.order):
      for to in self.tree[fr]:
        if self.parent[fr] == to:
          continue
        self.sz[fr] += self.sz[to]

  proc solve*[N: static int, T](self: var RerootingTree[N, T], root = 0): array[
      0..N - 1, T] =
    self.topologicalSort(root)
    self.dp1.fill(self.ide)
    self.dp2.fill(self.ide)
    self.left.fill(self.ide)
    self.right.fill(self.ide)

    for fr in reversed(self.order):
      var acc = self.ide
      for to in self.tree[fr]:
        if self.parent[fr] == to:
          continue
        self.left[to] = acc
        acc = self.merge(acc, self.op(self.dp1[to], fr, to))
      acc = self.ide
      for to in reversed(self.tree[fr]):
        if self.parent[fr] == to:
          continue
        self.right[to] = acc
        acc = merge(acc, self.op(self.dp1[to], fr, to))
      self.dp1[fr] = acc

    for to in self.order[1..^1]:
      self.dp2[to] = self.merge(self.left[to], self.right[to])
      self.dp2[to] = self.op(self.merge(self.dp2[to], self.dp2[self.parent[
          to]]), to, self.parent[to])
      self.dp1[to] = self.merge(self.dp1[to], self.dp2[to])
    return self.dp1

when not declared ATCODER_SLOPE_TRICK_HPP:
  const ATCODER_SLOPE_TRICK_HPP* = 1

  type SlopeTrick = object
    minf, al, ar: int
    leftQueue, rightQueue: HeapQueue[int]

  proc initSlopeTrick*(minimum: int): SlopeTrick =
    var leftQueue, rightQueue: HeapQueue[int]
    return SlopeTrick(minf: minimum, al: 0, ar: 0, leftQueue: leftQueue,
        rightQueue: rightQueue)

  proc min*(self: var SlopeTrick): int {.inline.} = self.minf
  proc addConst*(self: var SlopeTrick, a: int) {.inline.} = self.minf += a
  proc addLeft*(self: var SlopeTrick, a: int) {.inline.} = self.al += a
  proc addRight*(self: var SlopeTrick, a: int) {.inline.} = self.ar += a
  proc topLeft*(self: var SlopeTrick): int {.inline.} = -self.leftQueue[0] + self.al
  proc topRight*(self: var SlopeTrick): int {.inline.} = self.rightQueue[0] + self.ar

  proc addXmA*(self: var SlopeTrick, a: int) =
    if self.leftQueue.len != 0:
      self.minf += max(0, self.topLeft() - a)
    self.leftQueue.push(-a + self.al)
    self.rightQueue.push(-self.leftQueue.pop() + self.al - self.ar)

  proc addAmX*(self: var SlopeTrick, a: int) =
    if self.rightQueue.len != 0:
      self.minf += max(0, a - self.topRight())
    self.rightQueue.push(a - self.ar)
    self.leftQueue.push(-self.rightQueue.pop() - self.ar + self.al)

when not declared ATCODER_TREAP_HPP:
  const ATCODER_TREAP_HPP* = 1

  type TreapNode[T] = ref object
    key: T
    priority, cnt: int
    left, right: TreapNode[T]

  type Treap[T] = ref object
    root: TreapNode[T]
    randX: uint64

  proc initTreapNode*[T](key: T, priority: int, left, right: TreapNode[
      T]): TreapNode[T] =
    TreapNode[T](key: key, priority: priority, cnt: 1, left: left, right: right)
  proc initTreap*[T](): Treap[T] =
    Treap[T](root: nil, randX: 88172645463325252.uint64)

  proc split*[T](v: TreapNode[T], key: T, left, right: var TreapNode[T]) =
    if v == nil:
      left = nil
      right = nil
    elif key < v.key:
      split(v.left, key, left, v.left)
      right = v
    else:
      split(v.right, key, v.right, right)
      left = v

  proc merge*[T](v: var TreapNode[T], left, right: TreapNode[T]) =
    if left == nil:
      v = right
    elif right == nil:
      v = left
    elif left.priority > right.priority:
      merge(left.right, left.right, right)
      v = left
    else:
      merge(right.left, left, right.left)
      v = right

  proc insert*[T](v: var TreapNode[T], x: TreapNode[T]) =
    if v == nil:
      v = x
    elif x.key == v.key:
      v.cnt.inc
    elif x.priority > v.priority:
      split(v, x.key, x.left, x.right)
      v = x
    elif x.key < v.key:
      insert(v.left, x)
    else:
      insert(v.right, x)

  proc erase*[T](v: var TreapNode[T], key: T) =
    if v == nil:
      return
    if key == v.key:
      if v.cnt == 1:
        merge(v, v.left, v.right)
      else:
        v.cnt.dec
    elif key < v.key:
      erase(v.left, key)
    else:
      erase(v.right, key)

  proc contains*[T](v: var Treapnode[T], key: T): bool =
    if v == nil:
      return false
    if key == v.key:
      return true
    if key < v.key:
      return contains(v.left, key)
    return contains(v.right, key)

  proc min*[T](v: var TreapNode[T]): TreapNode[T] =
    if v.left == nil:
      return v
    return min(v.left)

  proc max*[T](v: var TreapNode[T]): TreapNode[T] =
    if v.right == nil:
      return v
    return max(v.left)

  proc next*[T](v: var TreapNode[T], key: T, incl: bool): TreapNode[T] =
    if v == nil:
      return nil
    if incl and v.key == key:
      return v
    if key < v.key:
      result = next(v.left, key, incl)
      if result == nil:
        return v
    else:
      return next(v.right, key, incl)

  proc prev*[T](v: var TreapNode[T], key: T, incl: bool): TreapNode[T] =
    if v == nil:
      return nil
    if incl and v.key == key:
      return v
    if key > v.key:
      result = prev(v.right, key, incl)
      if result == nil:
        return v
    else:
      return prev(v.left, key, incl)

  proc insert*[T](self: var Treap[T], key: T) {.inline.} =
    self.randX = xor64(self.randX)
    insert(self.root, initTreapNode(key, self.randX.int, nil, nil))

  proc erase*[T](self: var Treap[T], key: T) {.inline.} =
    if self.root == nil: return
    erase(self.root, key)

  proc contains*[T](self: var Treap[T], key: T): bool {.inline.} =
    return contains(self.root, key)

  proc min*[T](self: var Treap[T]): T {.inline.} =
    return min(self.root).key

  proc max*[T](self: var Treap[T]): T {.inline.} =
    return max(self.root).key

  proc next*[T](self: var Treap[T], key: T, incl = false): T {.inline.} =
    return next(self.root, key, incl).key

  proc prev*[T](self: var Treap[T], key: T, incl = false): T {.inline.} =
    return prev(self.root, key, incl).key
