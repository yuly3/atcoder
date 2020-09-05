import algorithm, deques, math, sets, sequtils, strutils, sugar, tables


proc bit_length(n: int): int =
    if n == 0:
      return 0
    let s = toBin(n, 60)
    return 60 - s.find('1')


type
    DualSegmentTree*[T] = ref object
        LV, N0: Natural
        lazy_ide_ele: T
        lazy_data: seq[T]

proc initDualSegmentTree*[T](size: Natural, lazy_ide_ele: T): DualSegmentTree[T] =
    var
        LV = bit_length(size - 1)
        N0 = 1 shl LV
    return DualSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: newSeqWith(2 * N0, lazy_ide_ele))

iterator gindex*[T](self: var DualSegmentTree[T], left, right: int): int =
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

proc propagates*[T](self: var DualSegmentTree[T], ids: seq[int]) =
    var
        idx: int
        v: T
    for id in reversed(ids):
        idx = id - 1
        v = self.lazy_data[idx]
        if v == self.lazy_ide_ele:
            continue
        self.lazy_data[2*idx + 1] += v
        self.lazy_data[2*idx + 2] += v
        self.lazy_data[idx] = self.lazy_ide_ele

proc update*[T](self: var DualSegmentTree[T], left, right: int, x: T) =
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

proc query*[T](self: var DualSegmentTree[T], k: int): T =
    self.propagates(toSeq(self.gindex(k, k + 1)))
    return self.lazy_data[k + self.N0 - 1]


type
    Event = array[5, int]

proc eventCmp(A, B: Event): int =
    if A[1] < B[1]: return -1
    if A[1] > B[1]: return 1
    if A[0] < B[0]: return -1
    if A[0] > B[0]: return 1
    else: return 0


var
    events: seq[Event]
    y: HashSet[int]
    y_to_idx: Table[int, int]
    dual_seg_tree: DualSegmentTree[int]
    ans: seq[int]


proc solve() =
    var N, Q: int
    (N, Q) = stdin.readLine.split.map(parseInt)
    events = newSeq[Event]()
    y = initHashSet[int]()
    var xmin, ymin, d, c, a, b: int
    for _ in 0..<N:
        (xmin, ymin, d, c) = stdin.readLine.split.map(parseInt)
        events.add([0, xmin, ymin, ymin + d, c])
        events.add([2, xmin + d, ymin, ymin + d, c])
        y.incl(ymin)
        y.incl(ymin + d)
    for i in 0..<Q:
        (a, b) = stdin.readLine.split.map(parseInt)
        events.add([1, a, b, i, 0])
        y.incl(b)
    
    events.sort(eventCmp)
    y_to_idx = initTable[int, int]()
    for idx, val in sorted(toSeq(y.items)):
        y_to_idx[val] = idx
    
    dual_seg_tree = initDualSegmentTree(y.len, 0)
    ans = newSeq[int](Q)
    var ys, ye, cost, bi, i: int
    for event in events:
        if event[0] == 0:
            (ys, ye, cost) = event[2..^1]
            dual_seg_tree.update(y_to_idx[ys], y_to_idx[ye] + 1, cost)
        elif event[0] == 2:
            (ys, ye, cost) = event[2..^1]
            dual_seg_tree.update(y_to_idx[ys], y_to_idx[ye] + 1, -cost)
        else:
            (bi, i) = event[2..^2]
            ans[i] = dual_seg_tree.query(y_to_idx[bi])
    echo ans.join("\n")


when is_main_module:
    solve()
