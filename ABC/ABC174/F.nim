import algorithm, math, sequtils, strutils, sugar


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
    c: seq[int]
    lr: seq[array[2, int]]
    seg_tree: SegmentTree[int]
    c_to_idx: array[5 * 10^5, int]
    queries: seq[(int, int, int)]
    ans: seq[int]


proc solve() =
    var N, Q: int
    (N, Q) = stdin.readLine.split.map(parseInt)
    c = stdin.readLine.split.mapIt(it.parseInt - 1)
    var l, r: int
    for i in 0..<Q:
        (l, r) = stdin.readLine.split.map(parseInt)
        lr.add([l, r])
    
    seg_tree = initSegmntTree(N, 0, (a, b) => (a + b))
    c_to_idx.fill(-1)
    for idx, (left, right) in lr:
        queries.add((left - 1, right, idx))
    queries.sort((a, b) => (if a[1] < b[1]: -1 elif a[1] == b[1]: 0 else: 1))
    
    var p_right = 0
    ans = newSeq[int](Q)
    for (left, right, idx) in queries:
        for i in p_right..<right:
            if c_to_idx[c[i]] != -1:
                seg_tree.update(c_to_idx[c[i]], 0)
            seg_tree.update(i, 1)
            c_to_idx[c[i]] = i
        p_right = right
        ans[idx] = seg_tree.query(left, right)
    
    echo ans.join("\n")


when is_main_module:
    solve()
