import algorithm, sequtils, strutils, sugar

proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)


type
    UnionFind* = ref object
        n: Positive
        parents: seq[int]

proc initUnionFind*(n: Positive): UnionFind =
    return UnionFind(n: n, parents: newSeqWith(n, -1))

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

proc size*(self: var UnionFind, x: Natural): Positive =
    return -self.parents[self.find(x)]

proc same*(self: var UnionFind, x, y: Natural): bool =
    return self.find(x) == self.find(y)

proc members*(self: var UnionFind, x: Natural): seq[int] =
    let root = self.find(x)
    return toSeq(0..<int(self.n)).filterIt(self.find(it) == root)

proc roots*(self: var UnionFind): seq[int] =
    return toSeq(0..<int(self.n)).filterIt(self.parents[it] < 0)

proc group_count*(self: var UnionFind): Positive =
    return self.roots.len


proc bit_length(n: Natural): Natural =
    const BIT_SIZE = 60
    if n == 0:
      return 0
    let s = toBin(n, BIT_SIZE)
    return BIT_SIZE - s.find('1')


type
    SegmentTree*[T] = ref object
        N0: Positive
        ide_ele: T
        data: seq[T]
        segfunc: proc (a, b: T): T

proc initSegmentTree*[T](size: Positive, ide_ele: T, f: proc (a, b: T): T): SegmentTree[T] =
    var
        N0 = 1 shl bit_length(size - 1)
        data = newSeqWith(2*N0, ide_ele)
    return SegmentTree[T](N0: N0, ide_ele: ide_ele, data: data, segfunc: f)

proc toSegmentTree*[T](init_value: openArray[T], ide_ele: T, f: proc (a, b: T): T): SegmentTree[T] =
    var
        N0 = 1 shl bit_length(init_value.len - 1)
        data = newSeqWith(2*N0, ide_ele)
    for i, x in init_value:
        data[i + N0 - 1] = x
    for i in countdown(N0 - 2, 0):
        data[i] = f(data[2*i + 1], data[2*i + 2])
    return SegmentTree[T](N0: N0, ide_ele: ide_ele, data: data, segfunc: f)

proc update*[T](self: var SegmentTree[T], idx: Natural, x: T) =
    var k = self.N0 - 1 + idx
    self.data[k] = x
    while k != 0:
        k = (k - 1) div 2
        self.data[k] = self.segfunc(self.data[2*k + 1], self.data[2*k + 2])

proc query*[T](self: var SegmentTree[T], left, right: Natural): T =
    var
        L = left + self.N0
        R = right + self.N0
        res = self.ide_ele
    
    while L < R:
        if (L and 1) == 1:
            res = self.segfunc(res, self.data[L - 1])
            inc L
        if (R and 1) == 1:
            dec R
            res = self.segfunc(res, self.data[R - 1])
        L = L shr 1
        R = R shr 1
    return res


type
    LazySegmentTree*[T, K] = ref object
        LV: Natural
        N0: Positive
        ide_ele: T
        lazy_ide_ele: K
        data: seq[T]
        lazy_data: seq[K]
        segfunc: proc (a, b: T): T

proc initLazySegmentTree*[T, K](size: Positive, ide_ele: T, lazy_ide_ele: K, f: proc (a, b: T): T): LazySegmentTree[T, K] =
    var
        LV = bit_length(size - 1)
        N0 = 1 shl LV
        data = newSeqWith(2*N0, ide_ele)
        lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    return LazySegmentTree[T, K](LV: LV, N0: N0, ide_ele: ide_ele, lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data, segfunc: f)

proc toLazySegmentTree*[T, K](init_value: openArray[T], ide_ele: T, lazy_ide_ele: K, f: proc (a, b: T): T): LazySegmentTree[T, K] =
    var
        LV = bit_length(init_value.len - 1)
        N0 = 1 shl LV
        data = newSeqWith(2*N0, ide_ele)
        lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    for i, x in init_value:
        data[i + N0 - 1] = x
    for i in countdown(N0 - 2, 0):
        data[i] = f(data[2*i + 1], data[2*i + 2])
    return LazySegmentTree[T, K](LV: LV, N0: N0, ide_ele: ide_ele, lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data, segfunc: f)

iterator gindex*[T, K](self: var LazySegmentTree[T, K], left, right: Natural): Natural =
    var
        L = (left + self.N0) shr 1
        R = (right + self.N0) shr 1
        lc = if (left and 1) == 1: 0 else: bit_length(L and -L)
        rc = if (right and 1) == 1: 0 else: bit_length(R and -R)
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
        v: T
    for id in reversed(ids):
        idx = id - 1
        v = self.lazy_data[idx]
        if v == self.lazy_ide_ele:
            continue
        self.data[2*idx + 1] += v
        self.data[2*idx + 2] += v
        self.lazy_data[2*idx + 1] += v
        self.lazy_data[2*idx + 2] += v
        self.lazy_data[idx] = self.lazy_ide_ele

proc update*[T, K](self: var LazySegmentTree[T, K], left, right: Natural, x: T) =
    let ids = toSeq(self.gindex(left, right))
    self.propagates(ids)
    var
        L = left + self.N0
        R = right + self.N0
    
    while L < R:
        if (L and 1) == 1:
            self.lazy_data[L - 1] += x
            self.data[L - 1] += x
            inc L
        if (R and 1) == 1:
            dec R
            self.lazy_data[R - 1] += x
            self.data[R - 1] += x
        L = L shr 1
        R = R shr 1
    var idx: Natural
    for id in ids:
        idx = id - 1
        self.data[idx] = self.segfunc(self.data[2*idx + 1], self.data[2*idx + 2])# + self.lazy_data[idx]

proc query*[T, K](self: var LazySegmentTree[T, K], left, right: Natural): T =
    self.propagates(toSeq(self.gindex(left, right)))
    var
        L = left + self.N0
        R = right + self.N0
        res = self.ide_ele
    
    while L < R:
        if (L and 1) == 1:
            res = self.segfunc(res, self.data[L - 1])
            inc L
        if (R and 1) == 1:
            dec R
            res = self.segfunc(res, self.data[R - 1])
        L = L shr 1
        R = R shr 1
    return res


type
    DuelSegmentTree*[T] = ref object
        LV: Natural
        N0: Positive
        lazy_ide_ele: T
        lazy_data: seq[T]

proc initDuelSegmentTree*[T](size: Positive, lazy_ide_ele: T): DuelSegmentTree[T] =
    var
        LV = bit_length(size - 1)
        N0 = 1 shl LV
        lazy_data = newSeqWith(2 * N0, lazy_ide_ele)
    return DuelSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: lazy_data)

iterator gindex*[T](self: var DuelSegmentTree[T], left, right: Natural): Natural =
    var
        L = (left + self.N0) shr 1
        R = (right + self.N0) shr 1
        lc = if (left and 1) == 1: 0 else: bit_length(L and -L)
        rc = if (right and 1) == 1: 0 else: bit_length(R and -R)
    for i in 0..<self.LV:
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L = L shr 1
        R = R shr 1

proc propagates*[T](self: var DuelSegmentTree[T], ids: seq[Natural]) =
    var
        idx: Natural
        v: T
    for id in reversed(ids):
        idx = id - 1
        v = self.lazy_data[idx]
        if v == self.lazy_ide_ele:
            continue
        self.lazy_data[2*idx + 1] += v
        self.lazy_data[2*idx + 2] += v
        self.lazy_data[idx] = self.lazy_ide_ele

proc update*[T](self: var DuelSegmentTree[T], left, right: Natural, x: T) =
    # self.propagates(toSeq(self.gindex(left, right)))
    var
        L = left + self.N0
        R = right + self.N0
    
    while L < R:
        if (L and 1) == 1:
            self.lazy_data[L - 1] += x
            inc L
        if (R and 1) == 1:
            dec R
            self.lazy_data[R - 1] += x
        L = L shr 1
        R = R shr 1

proc query*[T](self: var DuelSegmentTree[T], k: Natural): T =
    self.propagates(toSeq(self.gindex(k, k + 1)))
    return self.lazy_data[k + self.N0 - 1]
