import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
    num0 = num0 mod num1


type
    UnionFind* = ref object
        n: Positive
        parents: seq[int]

proc initUnionFind*(n: Positive): UnionFind =
    return UnionFind(n: n, parents: newSeqWith(n, -1))

proc find*(self: var UnionFind, x: Natural): Natural =
    if self.parents[x] < 0:
        return x
    else:
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

proc union*(self: var UnionFind, x, y: Natural) =
    var
        root_x = self.find(x)
        root_y = self.find(y)
    
    if root_x == root_y:
        return
    if self.parents[root_y] < self.parents[root_x]:
        (root_x, root_y) = (root_y, root_x)
    self.parents[root_x] += self.parents[root_y]
    self.parents[root_y] = root_x

proc size*(self: var UnionFind, x: Natural): Positive =
    return -self.parents[self.find(x)]

proc same*(self: var UnionFind, x, y: Natural): bool =
    return self.find(x) == self.find(y)

proc members*(self: var UnionFind, x: Natural): seq[int] =
    let root = self.find(x)
    return toSeq(0..<int(self.n)).filterIt(self.find(it) == root)

proc roots*(self: var UnionFind): seq[int] =
    return toSeq(0..<int(self.n)).filterIt(self.parents[it] < 0)

proc group_count*(self: var UnionFind): Positive =
    return self.roots.len


var
    y_to_idx: Table[int, int]
    xy: seq[(int, int)]
    stack, ans: seq[int]
    uf: UnionFind

proc solve() =
    let N = input().parseInt
    y_to_idx = initTable[int, int]()
    var xi, yi: int
    for i in 0..<N:
        (xi, yi) = input().split.map(parseInt)
        y_to_idx[yi] = i
        xy.add((xi, yi))
    xy = sortedByIt(xy, it[0])

    uf = initUnionFind(N)
    var yj, min_y: int
    for (xi, yi) in xy:
        min_y = yi
        while stack.len != 0 and stack[^1] < yi:
            yj = stack.pop
            uf.union(y_to_idx[yj], y_to_idx[yi])
            min_y.chmin(yj)
        stack.add(min_y)
    
    ans = newSeq[int](N)
    for i in 0..<N:
        ans[i] = uf.size(i)
    echo ans.join("\n")

when is_main_module:
    solve()
