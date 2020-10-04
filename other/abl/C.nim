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


var uf: UnionFind

proc solve() =
    var N, M, ai, bi: int
    (N, M) = input().split.map(parseInt)
    uf = initUnionFind(N)
    for _ in 0..<M:
        (ai, bi) = input().split.mapIt(it.parseInt - 1)
        uf.union(ai, bi)
    
    echo uf.group_count - 1

when is_main_module:
    solve()
