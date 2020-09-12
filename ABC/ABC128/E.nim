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
    else:
        self.layer0.delete(self.layer0.len - 1, self.layer0.len - 1)
        let res = self.layer1[^2]
        self.layer1.delete(self.layer1.len - 2, self.layer1.len - 2)
        return res

proc min*[T](self: var SquareSkipList[T]): T =
    return if self.layer0[0].len != 0: self.layer0[0][0] else: self.layer1[0]

proc max*[T](self: var SquareSkipList[T]): T =
    return if self.layer0[^1].len != 0: self.layer0[^1][^1] else: self.layer1[^2]


var
    events: seq[(int, int, int)]
    ssl: SquareSkipList[int]
    ans: seq[int]

proc solve() =
    var N, Q: int
    (N, Q) = input().split.map(parseInt)
    events = newSeq[(int, int, int)]()
    var s, t, x: int
    for _ in 0..<N:
        (s, t, x) = input().split.map(parseInt)
        events.add((t - x, 0, x))
        events.add((s - x, 1, x))
    for _ in 0..<Q:
        events.add((input().parseInt, 2, -1))
    events = events.sortedByIt((it[0], it[1]))

    const inf = 10^10
    ssl = initSquareSkipList(inf, cmp[int])
    ans = newSeq[int]()
    for (_, com, pos) in events:
        if com == 0:
            ssl.remove(pos)
        elif com == 1:
            ssl.add(pos)
        else:
            ans.add(if ssl.min != inf: ssl.min else: -1)
    echo ans.join("\n")

when is_main_module:
    solve()
