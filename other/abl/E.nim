import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
    num0 = num0 mod num1

proc bit_length(n: Natural): Natural =
    const BIT_SIZE = 24
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
        fold: proc (a, b: T): T
        eval: proc (a: T, b: K): T
        merge: proc (a, b: K): K
        propagates_when_updating: bool

proc initLazySegmentTree*[T, K](size: Positive, ide_ele: T, lazy_ide_ele: K, fold: proc (a, b: T): T, eval: proc (a: T, b: K): T, merge: proc (a, b: K): K, propagates_when_updating=false): LazySegmentTree[T, K] =
    let
        LV = bit_length(size - 1)
        N0 = 1 shl LV
        data = newSeqWith(2*N0, ide_ele)
        lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    return LazySegmentTree[T, K](LV: LV, N0: N0, ide_ele: ide_ele, lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data, fold: fold, eval: eval, merge: merge, propagates_when_updating: propagates_when_updating)

proc toLazySegmentTree*[T, K](init_value: openArray[T], ide_ele: T, lazy_ide_ele: K, fold: proc (a, b: T): T, eval: proc (a: T, b: K): T, merge: proc (a, b: K): K, propagates_when_updating=false): LazySegmentTree[T, K] =
    let
        LV = bit_length(init_value.len - 1)
        N0 = 1 shl LV
        lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    var data = newSeqWith(2*N0, ide_ele)
    for i, x in init_value:
        data[i + N0 - 1] = x
    for i in countdown(N0 - 2, 0):
        data[i] = fold(data[2*i + 1], data[2*i + 2])
    return LazySegmentTree[T, K](LV: LV, N0: N0, ide_ele: ide_ele, lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data, fold: fold, eval: eval, merge: merge, propagates_when_updating: propagates_when_updating)

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
        # v = v shr 1
        self.data[2*idx + 1] = self.eval(self.data[2*idx + 1], v)
        self.data[2*idx + 2] = self.eval(self.data[2*idx + 2], v)
        self.lazy_data[2*idx + 1] = self.merge(self.lazy_data[2*idx + 1], v)
        self.lazy_data[2*idx + 2] = self.merge(self.lazy_data[2*idx + 2], v)
        self.lazy_data[idx] = self.lazy_ide_ele

proc update*[T, K](self: var LazySegmentTree[T, K], left, right: Natural, x: K) =
    let ids = toSeq(self.gindex(left, right))
    if self.propagates_when_updating:
        self.propagates(ids)
    var
        L = left + self.N0
        R = right + self.N0
        # x = x
    
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
        # x = x shl 1
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
        res = self.ide_ele
        a = newSeq[int]()
        b = newSeq[int]()
    
    while L < R:
        if (L and 1) == 1:
            a.add(L - 1)
            inc L
        if (R and 1) == 1:
            dec R
            b.add(R - 1)
        L = L shr 1
        R = R shr 1
    for id in concat(a, b.reversed):
        res = self.fold(res, self.data[id])
    return res


const MOD = 998244353
var
    same_num_mod: array[10, array[200001, int]]
    pow10: array[200001, int]
    init_val: seq[(int, int)]
    lazy_seg_tree: LazySegmentTree[(int, int), int]
    ans: seq[int]

proc solve() =
    var N, Q: int
    (N, Q) = input().split.map(parseInt)

    for i in 1..9:
        for j in 1..N:
            same_num_mod[i][j] = (10*same_num_mod[i][j - 1] + i) mod MOD
    
    pow10[0] = 1
    for i in 1..N:
        pow10[i] = 10*pow10[i - 1] mod MOD
    
    init_val = newSeqWith(N, (1, 1))
    let ide_ele = (0, 0)
    proc fold(a, b: (int, int)): (int, int) =
        if b == ide_ele:
            return a
        return ((a[0]*pow10[b[1]] + b[0]) mod MOD, a[1] + b[1])
    proc eval(a: (int, int), b: int): (int, int) =
        return (same_num_mod[b][a[1]], a[1])
    proc merge(a, b: int): int =
        return b
    lazy_seg_tree = toLazySegmentTree(init_val, ide_ele, 0, fold, eval, merge, true)

    ans = newSeq[int](Q)
    var li, ri, di: int
    for i in 0..<Q:
        (li, ri, di) = input().split.map(parseInt)
        lazy_seg_tree.update(li - 1, ri, di)
        ans[i] = lazy_seg_tree.query(0, N)[0]
    echo ans.join("\n")

when is_main_module:
    solve()
