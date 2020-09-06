import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)


proc bit_length(n: Natural): Natural =
    if n == 0:
      return 0
    let s = toBin(n, 60)
    return 60 - s.find('1')


type
    LazySegmentTree*[T] = ref object
        LV: Natural
        N0: Positive
        ide_ele, lazy_ide_ele: T
        data, lazy_data: seq[T]
        segfunc: proc (a, b: T): T

proc initLazySegmentTree*[T](size: Positive, ide_ele, lazy_ide_ele: T, f: proc (a, b: T): T): LazySegmentTree[T] =
    var
        LV = bit_length(size - 1)
        N0 = 1 shl LV
        data = newSeqWith(2*N0, ide_ele)
        lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    return LazySegmentTree[T](LV: LV, N0: N0, ide_ele: ide_ele, lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data, segfunc: f)

proc toLazySegmentTree*[T](init_value: openArray[T], ide_ele, lazy_ide_ele: T, f: proc (a, b: T): T): LazySegmentTree[T] =
    var
        LV = bit_length(init_value.len - 1)
        N0 = 1 shl LV
        data = newSeqWith(2*N0, ide_ele)
        lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    for i, x in init_value:
        data[i + N0 - 1] = x
    for i in countdown(N0 - 2, 0):
        data[i] = f(data[2*i + 1], data[2*i + 2])
    return LazySegmentTree[T](LV: LV, N0: N0, ide_ele: ide_ele, lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data, segfunc: f)

iterator gindex*[T](self: var LazySegmentTree[T], left, right: Natural): Natural =
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

proc propagates*[T](self: var LazySegmentTree[T], ids: seq[Natural]) =
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

proc update*[T](self: var LazySegmentTree[T], left, right: Natural, x: T) =
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
        self.data[idx] = self.segfunc(self.data[2*idx + 1], self.data[2*idx + 2])

proc query*[T](self: var LazySegmentTree[T], left, right: Natural): T =
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
    lazy_seg_tree: LazySegmentTree[int]
    st: array[10^5, array[2, int]]
    ans: seq[int]


proc solve() =
    var N, M: int
    (N, M) = input().split.map(parseInt)
    lazy_seg_tree = toLazySegmentTree(newSeq[int](N), 10^6, 0, (a, b) => min(a, b))
    var si, ti: int
    for i in 0..<M:
        (si, ti) = input().split.map(parseInt)
        dec si
        st[i] = [si, ti]
        lazy_seg_tree.update(si, ti, 1)

    ans = newSeq[int]()
    for i, (si, ti) in st[0..<M]:
        if 1 < lazy_seg_tree.query(si, ti):
            ans.add(i + 1)
    
    echo ans.len
    if ans.len != 0:
        echo ans.join("\n")


when is_main_module:
    solve()
