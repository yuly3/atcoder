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
        propagates_when_updating: bool

proc initDuelSegmentTree*[T](size: Positive, lazy_ide_ele: T, merge: proc (a, b: T): T, propagates_when_updating=false): DuelSegmentTree[T] =
    let
        LV = bit_length(size - 1)
        N0 = 1 shl LV
        lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    return DuelSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: lazy_data, merge: merge, propagates_when_updating: propagates_when_updating)

proc toDuelSegmentTree*[T](init_value: openArray[T], lazy_ide_ele: T, merge: proc (a, b: T): T, propagates_when_updating=false): DuelSegmentTree[T] =
    let
        LV = bit_length(init_value.len - 1)
        N0 = 1 shl LV
    var lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    for i, x in init_value:
        lazy_data[i + N0 - 1] = x
    return DuelSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: lazy_data, merge: merge, propagates_when_updating: propagates_when_updating)

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
    if self.propagates_when_updating:
        self.propagates(toSeq(self.gindex(left, right)))
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


var
    duel_seg_tree: DuelSegmentTree[int]

proc solve() =
    var N, K: int
    (N, K) = input().split.map(parseInt)

    duel_seg_tree = initDuelSegmentTree(300001, 0, (a, b) => max(a, b))
    var
        ans = 0
        ai, v: int
    for _ in 0..<N:
        ai = input().parseInt
        v = duel_seg_tree.query(ai)
        ans.chmax(v + 1)
        duel_seg_tree.update(max(0, ai - K), min(300001, ai + K + 1), v + 1)
    echo ans

when is_main_module:
    solve()
