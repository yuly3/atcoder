import algorithm, deques, math, sequtils, strutils, sugar


proc bit_length(n: int): int =
    if n == 0:
      return 0
    let s = toBin(n, 60)
    return 60 - s.find('1')


type
    SegmentTree*[T] = ref object
        N0: Natural
        ide_ele: T
        data: seq[T]
        segfunc: proc (a, b: T): T

proc initSegmntTree*[T](size: Natural, ide_ele: T, f: proc (a, b: T): T): SegmentTree[T] =
    var N0 = 1 shl bit_length(size - 1)
    return SegmentTree[T](N0: N0, ide_ele: ide_ele, data: newSeqWith(2 * N0, ide_ele), segfunc: f)

proc update*[T](self: var SegmentTree[T], idx: int, x: T) =
    var k = self.N0 - 1 + idx
    self.data[k] = x
    while k != 0:
        k = (k - 1) div 2
        self.data[k] = self.segfunc(self.data[k * 2 + 1], self.data[k * 2 + 2])

proc query*[T](self: var SegmentTree[T], left, right: int): T =
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
    T: array[10^5, Deque[int]]
    kiti, a, ans: seq[int]
    seg_tree0, seg_tree1: SegmentTree[(int, int)]


proc solve() =
    let N = stdin.readLine.parseInt
    var ki: int
    for i in 0..<N:
        kiti = stdin.readLine.split.map(parseInt)
        ki = kiti[0]
        T[i] = initDeque[int]()
        for j in 1..ki:
            T[i].addLast(kiti[j])
    let M = stdin.readLine.parseInt
    a = stdin.readLine.split.map(parseInt)

    let ide_ele = (0, -1)
    seg_tree0 = initSegmntTree(N, ide_ele, (x, y) => (if x[0] < y[0]: y else: x))
    seg_tree1 = initSegmntTree(N, ide_ele, (x, y) => (if x[0] < y[0]: y else: x))
    for i in 0..<N:
        seg_tree0.update(i, (T[i].popFirst, i))
        seg_tree1.update(i, ((if T[i].len != 0: T[i].popFirst else: 0), i))
    
    var idx: int
    ans = newSeq[int](M)
    for i, ai in a:
        if ai == 1 or seg_tree1.data[0][0] < seg_tree0.data[0][0]:
            (ans[i], idx) = seg_tree0.data[0]
            seg_tree0.update(idx, seg_tree1.data[idx + seg_tree1.N0 - 1])
            seg_tree1.update(idx, ((if T[idx].len != 0: T[idx].popFirst else: 0), idx))
        else:
            (ans[i], idx) = seg_tree1.data[0]
            seg_tree1.update(idx, ((if T[idx].len != 0: T[idx].popFirst else: 0), idx))
    
    echo ans.join("\n")


when is_main_module:
    solve()
