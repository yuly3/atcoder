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
    DualSegmentTree*[T] = ref object
        LV: Natural
        N0: Positive
        lazy_ide_ele: T
        lazy_data: seq[T]

proc initDualSegmentTree*[T](size: Positive, lazy_ide_ele: T): DualSegmentTree[T] =
    var
        LV = bit_length(size - 1)
        N0 = 1 shl LV
    return DualSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: newSeqWith(2 * N0, lazy_ide_ele))

iterator gindex*[T](self: var DualSegmentTree[T], left, right: Natural): Natural =
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

proc propagates*[T](self: var DualSegmentTree[T], ids: seq[Natural]) =
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

proc update*[T](self: var DualSegmentTree[T], left, right: Natural, x: T) =
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

proc query*[T](self: var DualSegmentTree[T], k: Natural): T =
    self.propagates(toSeq(self.gindex(k, k + 1)))
    return self.lazy_data[k + self.N0 - 1]


var
    score: HashSet[int]
    queries: seq[(int, int, int)]
    score_to_idx: Table[int, int]
    A, ans: seq[int]
    dual_seg_tree: DualSegmentTree[int]


proc solve() =
    var N, M, ai: int
    (N, M) = input().split.map(parseInt)
    score = toHashSet([0, 10^9 + 1])
    for i in 0..<N:
        ai = input().parseInt
        score.incl(ai)
        queries.add((2, i + 1, ai))
    var
        query: seq[int]
        tj, bj, cj, dj: int
    for _ in 0..<M:
        query = input().split.map(parseInt)
        if query[0] == 1:
            (tj, bj) = query
            score.incl(bj)
            queries.add((1, bj, 0))
        else:
            (tj, cj, dj) = query
            score.incl(dj)
            queries.add((2, cj, dj))
    
    score_to_idx = initTable[int, int]()
    for idx, val in sorted(toSeq(score.items)):
        score_to_idx[val] = idx
    
    A = newSeq[int](N + 2)
    dual_seg_tree = initDualSegmentTree(score_to_idx.len, 0)
    var b, c, d, bigger, smaller: int
    for query in queries:
        if query[0] == 1:
            b = query[1]
            ans.add(dual_seg_tree.query(score_to_idx[b]))
        else:
            (c, d) = (query[1], query[2])
            bigger = max(A[c - 1], A[c + 1])
            smaller = min(A[c - 1], A[c + 1])
            if A[c] < d:
                if 0 < smaller - A[c]:
                    dual_seg_tree.update(score_to_idx[A[c]] + 1, score_to_idx[min(smaller, d)] + 1, -1)
                if 0 < d - bigger:
                    dual_seg_tree.update(score_to_idx[max(bigger, A[c])] + 1, score_to_idx[d] + 1, 1)
            elif d < A[c]:
                if 0 < A[c] - bigger:
                    dual_seg_tree.update(score_to_idx[max(bigger, d)] + 1, score_to_idx[A[c]] + 1, -1)
                if 0 < smaller - d:
                    dual_seg_tree.update(score_to_idx[d] + 1, score_to_idx[min(smaller, A[c])] + 1, 1)
            A[c] = d
    echo ans.join("\n")


when is_main_module:
    solve()
