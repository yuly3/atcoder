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
    DuelSegmentTree*[T] = ref object
        LV: Natural
        N0: Positive
        lazy_ide_ele: T
        lazy_data: seq[T]
        merge: proc (a, b: T): T

proc initDuelSegmentTree*[T](size: Positive, lazy_ide_ele: T, merge: proc (a, b: T): T): DuelSegmentTree[T] =
    var
        LV = bit_length(size - 1)
        N0 = 1 shl LV
        lazy_data = newSeqWith(2 * N0, lazy_ide_ele)
    return DuelSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: lazy_data, merge: merge)

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
        self.lazy_data[2*idx + 1] = self.merge(self.lazy_data[2*idx + 1], v)
        self.lazy_data[2*idx + 2] = self.merge(self.lazy_data[2*idx + 2], v)
        self.lazy_data[idx] = self.lazy_ide_ele

proc update*[T](self: var DuelSegmentTree[T], left, right: Natural, x: T) =
    # self.propagates(toSeq(self.gindex(left, right)))
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

proc query*[T](self: var DuelSegmentTree[T], k: Natural): T =
    self.propagates(toSeq(self.gindex(k, k + 1)))
    return self.lazy_data[k + self.N0 - 1]


const MOD = 998244353
var
    LR: seq[(int, int)]
    duel_seg_tree: DuelSegmentTree[int]

proc solve() =
    var N, K, li, ri: int
    (N, K) = input().split.map(parseInt)
    for _ in 0..<K:
        (li, ri) = input().split.map(parseInt)
        LR.add((li, ri))
    LR = LR.sortedByIt(it[0])

    duel_seg_tree = initDuelSegmentTree(N, 0, (a, b) => (a + b) mod MOD)
    duel_seg_tree.update(0, 1, 1)

    for i in 0..N - 2:
        let v = duel_seg_tree.query(i)
        for (li, ri) in LR:
            if N <= i + li:
                break
            duel_seg_tree.update(i + li, min(i + ri + 1, N), v)
    echo duel_seg_tree.query(N - 1)

when is_main_module:
    solve()
