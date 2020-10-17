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


const MOD = 10^9 + 7
var
    S: seq[string]
    uf_w, uf_h: array[2000, UnionFind]
    pow2: array[4000001, int]

proc solve() =
    var H, W: int
    (H, W) = input().split.map(parseInt)
    S = newSeqWith(H, input())

    for i in 0..<H:
        uf_w[i] = initUnionFind(W)
        for j in 0..<W - 1:
            if S[i][j] == '.' and S[i][j + 1] == '.':
                uf_w[i].union(j, j + 1)
    for i in 0..<W:
        uf_h[i] = initUnionFind(H)
        for j in 0..<H - 1:
            if S[j][i] == '.' and S[j + 1][i] == '.':
                uf_h[i].union(j, j + 1)
    
    var K = H*W
    for i in 0..<H:
        K -= S[i].count('#')
    
    pow2[0] = 1
    for i in 1..K:
        pow2[i] = 2*pow2[i - 1] mod MOD
    
    var ans = 0
    for i in 0..<H:
        for j in 0..<W:
            if S[i][j] == '.':
                let n = uf_w[i].size(j) + uf_h[j].size(i) - 1
                ans += (pow2[n] - 1)*pow2[K - n]
                ans %= MOD
    echo ans

when is_main_module:
    solve()
