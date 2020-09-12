import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)


type
    SquareSkipList*[T] = ref object
        square: Natural
        rand_y: int
        layer1: seq[T]
        layer0: seq[seq[T]]
        cmp_func: proc (a, b: T): int

proc initSquareSkipList*[T](inf: T, cmp_func: proc (a, b: T): int, square=1000, rand_y=42): SquareSkipList[T] =
    var
        layer1 = newSeqWith(1, inf)
        layer0 = newSeqWith(1, newSeq[T]())
    return SquareSkipList[T](square: square, rand_y: rand_y, layer1: layer1, layer0: layer0, cmp_func: cmp_func)

proc add*[T](self: var SquareSkipList[T], x: T) =
    var y = self.rand_y
    y = y xor ((y and 0x7ffff) shl 13)
    y = y xor (y shr 17)
    y = y xor ((y and 0x7ffffff) shl 5)
    self.rand_y = y

    if y mod self.square == 0:
        let idx1 = self.layer1.upperBound(x, self.cmp_func)
        self.layer1.insert(@[x], idx1)
        let idx0 = self.layer0[idx1].upperBound(x, self.cmp_func)
        self.layer0.insert(self.layer0[idx1][idx0..^1], idx1 + 1)
        self.layer0[idx1].delete(idx0, self.layer0[idx1].len)
    else:
        let
            idx1 = self.layer1.upperBound(x, self.cmp_func)
            idx0 = self.layer0[idx1].upperBound(x, self.cmp_func)
        self.layer0[idx1].insert(@[x], idx0)

proc remove*[T](self: var SquareSkipList[T], x: T) =
    let
        idx1 = self.layer1.lowerBound(x, self.cmp_func)
        idx0 = self.layer0[idx1].lowerBound(x, self.cmp_func)
    if idx0 == self.layer0[idx1].len:
        self.layer1.delete(idx1, idx1)
        self.layer0[idx1] = concat(self.layer0[idx1], self.layer0[idx1 + 1])
        self.layer0.delete(idx1 + 1, idx1 + 1)
    else:
        self.layer0[idx1].delete(idx0, idx0)

proc contains*[T](self: var SquareSkipList[T], x: T): bool =
    let
        idx1 = self.layer1.lowerBound(x, self.cmp_func)
        idx0 = self.layer0[idx1].lowerBound(x, self.cmp_func)
    if idx0 == self.layer0[idx1].len:
        return self.layer1[idx1] == x
    else:
        return self.layer0[idx1][idx0] == x

proc pop*[T](self: var SquareSkipList[T], idx: Natural): T =
    var
        s = -1
        i: int
    for ii, l0 in self.layer0:
        s += l0.len + 1
        i = ii
        if idx <= s:
            break
    if s == idx:
        self.layer0[i] = concat(self.layer0[i], @[self.layer0[i + 1]])
        self.layer0.delete(i + 1, i + 1)
        let res = self.layer1[i]
        self.layer1.delete(i, i)
        return res
    else:
        let res = self.layer0[i][idx - s]
        self.layer0[i].delete(idx - s, idx - s)
        return res

proc pop_max*[T](self: var SquareSkipList[T]): T =
    if self.layer0[^1].len != 0:
        return self.layer0[^1].pop()
    elif 1 < self.layer1.len:
        self.layer0.delete(self.layer0.len - 1, self.layer0.len - 1)
        let res = self.layer1[^2]
        self.layer1.delete(self.layer1.len - 2, self.layer1.len - 2)
        return res

proc min*[T](self: var SquareSkipList[T]): T =
    return if self.layer0[0].len != 0: self.layer0[0][0] else: self.layer1[0]

proc max*[T](self: var SquareSkipList[T]): T =
    return if self.layer0[^1].len != 0: self.layer0[^1][^1] elif 1 < self.layer1.len: self.layer1[^2] else: self.layer1[^1]


proc bit_length(n: Natural): Natural =
    const BIT_SIZE = 24
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


const M = 2 * 10^5
var
    A, infant_to_idx, init_value: array[M, int]
    ssl_array: array[M, SquareSkipList[int]]
    seg_tree: SegmentTree[int]
    ans: seq[int]

proc solve() =
    var N, Q, a, b: int
    (N, Q) = input().split.map(parseInt)
    const inf = 10^10
    for i in 0..<M:
        ssl_array[i] = initSquareSkipList(inf, cmp[int])
    for i in 0..<N:
        (a, b) = input().split.map(parseInt)
        dec b
        A[i] = a
        infant_to_idx[i] = b
        ssl_array[b].add(a)
    
    for i in 0..<M:
        init_value[i] = ssl_array[i].max
    seg_tree = toSegmentTree(init_value, inf, (a, b) => min(a, b))

    ans = newSeq[int](Q)
    var c, d, prev_idx: int
    for i in 0..<Q:
        (c, d) = input().split.mapIt(it.parseInt - 1)
        prev_idx = infant_to_idx[c]
        ssl_array[prev_idx].remove(A[c])
        seg_tree.update(prev_idx, ssl_array[prev_idx].max)
        infant_to_idx[c] = d
        ssl_array[d].add(A[c])
        seg_tree.update(d, ssl_array[d].max)
        ans[i] = seg_tree.data[0]
    echo ans.join("\n")

when is_main_module:
    solve()
