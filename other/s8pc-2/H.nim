import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)

proc bit_length(n: Natural): Natural =
    const BIT_SIZE = 60
    if n == 0:
      return 0
    let s = toBin(n, BIT_SIZE)
    return BIT_SIZE - s.find('1')


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
        v: K
    for id in reversed(ids):
        idx = id - 1
        v = self.lazy_data[idx]
        if v == self.lazy_ide_ele:
            continue
        self.data[2*idx + 1] = (self.data[2*idx + 1][1], self.data[2*idx + 1][0])
        self.data[2*idx + 2] = (self.data[2*idx + 2][1], self.data[2*idx + 2][0])
        self.lazy_data[2*idx + 1] = self.lazy_data[2*idx + 1] xor 1
        self.lazy_data[2*idx + 2] = self.lazy_data[2*idx + 2] xor 1
        self.lazy_data[idx] = self.lazy_ide_ele

proc update*[T, K](self: var LazySegmentTree[T, K], left, right: Natural, x: K) =
    let ids = toSeq(self.gindex(left, right))
    self.propagates(ids)
    var
        L = left + self.N0
        R = right + self.N0
    
    while L < R:
        if (L and 1) == 1:
            self.lazy_data[L - 1] = self.lazy_data[L - 1] xor 1
            self.data[L - 1] = (self.data[L - 1][1], self.data[L - 1][0])
            inc L
        if (R and 1) == 1:
            dec R
            self.lazy_data[R - 1] = self.lazy_data[R - 1] xor 1
            self.data[R - 1] = (self.data[R - 1][1], self.data[R - 1][0])
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


var
    lazy_seg_tree: LazySegmentTree[(int, int), int]
    ans: seq[int]

proc solve() =
    var n, Q: int
    (n, Q) = input().split.map(parseInt)

    lazy_seg_tree = toLazySegmentTree(newSeqWith(n, (1, 0)), (0, 0), 0, (a, b) => (a[0] + b[0], a[1] + b[1]))
    ans = newSeq[int]()
    var qi, li, ri: int
    for _ in 0..<Q:
        (qi, li, ri) = input().split.map(parseInt)
        if qi == 1:
            lazy_seg_tree.update(li, ri, 1)
        else:
            ans.add(lazy_seg_tree.query(li, ri)[1])
    echo ans.join("\n")

when is_main_module:
    solve()
