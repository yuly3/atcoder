from collections import deque


def cmb(n, r, mod=10 ** 9 + 7):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    numerator, denominator = 1, 1
    for i in range(1, r + 1):
        numerator = (numerator * (n + 1 - i)) % mod
        denominator = (denominator * i) % mod
    return numerator * pow(denominator, mod - 2, mod) % mod


def cmb_replace(n, r, mod=10 ** 9 + 7):
    return cmb(n + r - 1, r, mod)


def mod_div(x, y, mod=10 ** 9 + 7):
    return x * pow(y, mod - 2, mod) % mod


class Combination:
    def __init__(self, n: int, mod: int):
        self.mod = mod
        self.fact = [0] * (n + 1)
        self.factinv = [0] * (n + 1)
        self.inv = [0] * (n + 1)
        
        self.fact[0] = self.fact[1] = 1
        self.factinv[0] = self.factinv[1] = 1
        self.inv[1] = 1
        for i in range(2, n + 1):
            self.fact[i] = (self.fact[i - 1] * i) % mod
            self.inv[i] = (-self.inv[mod % i] * (mod // i)) % mod
            self.factinv[i] = (self.factinv[i - 1] * self.inv[i]) % mod
    
    def ncr(self, n: int, r: int):
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] % self.mod * self.factinv[n - r] % self.mod
    
    def nhr(self, n: int, r: int):
        return self.ncr(n + r - 1, r)
    
    def npr(self, n: int, r: int):
        if r < 0 or n < r:
            return 0
        return self.fact[n] * self.factinv[n - r] % self.mod


def matmul(a, b, mod):
    N0 = len(a)
    N1 = len(b[0])
    N2 = len(a[0])
    res = [[0] * N1 for _ in range(N0)]
    for i in range(N0):
        for j in range(N1):
            tmp = 0
            for k in range(N2):
                tmp = (tmp + a[i][k] * b[k][j]) % mod
            res[i][j] = tmp
    return res


def matpow(a, k, mod):
    N = len(a)
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        res[i][i] = 1
    while k:
        if k & 1:
            res = matmul(res, a, mod)
        a = matmul(a, a, mod)
        k >>= 1
    return res


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if not arr:
        arr.append([n, 1])
    return arr


def eratosthenes(n):
    prime = [2]
    if n == 2:
        return prime
    limit = int(n ** 0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


def reachable_nodes(s, edges):
    cur = {s}
    reachable = set()
    while cur:
        reachable |= cur
        cur = set().union(*(edges[node] for node in cur)) - reachable
    return reachable


def is_bipartite(n, graph):
    colors = [0] * n
    stack = [(0, 1)]
    while stack:
        v, color = stack.pop()
        colors[v] = color
        for child in graph[v]:
            if colors[child] == color:
                return False
            if colors[child] == 0:
                stack.append((child, -color))
    return True


class RollingHash:
    def __init__(self, s: str, base=10007, mod=(1 << 61) - 1):
        self.mod = mod
        length = len(s)
        self.pw = [1] * (length + 1)
        self.h = [0] * (length + 1)
        
        v = 0
        for i in range(length):
            self.h[i + 1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(length):
            self.pw[i + 1] = v = v * base % mod
    
    def slice(self, left, right):
        return (self.h[right] - self.h[left] * self.pw[right - left]) % self.mod
    
    def concatenate(self, left0, right0, left1, right1):
        return (self.slice(left0, right0) * self.pw[right1 - left1] + self.slice(left1, right1)) % self.mod


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x: int):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        if self.parents[y] < self.parents[x]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x: int):
        return -self.parents[self.find(x)]
    
    def same(self, x: int, y: int):
        return self.find(x) == self.find(y)
    
    def members(self, x: int):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


class BinaryIndexedTree:
    # 1-indexed
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
    
    def add(self, i, x):
        # Accessed by 0-indexed
        i += 1
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    
    def sum(self, i):
        # [0, i)
        res = 0
        while i:
            res += self.data[i]
            i -= i & -i
        return res
    
    def bisect_left(self, w):
        if w <= 0:
            return 0
        i = 0
        k = 1 << (self.n.bit_length() - 1)
        while 0 < k:
            if i + k <= self.n and self.data[i + k] < w:
                w -= self.data[i + k]
                i += k
            k >>= 1
        return i + 1


class SegmentTree:
    def __init__(self, init_value: list, segfunc, ide_ele):
        n = len(init_value)
        self.N0 = 1 << (n - 1).bit_length()
        self.ide_ele = ide_ele
        self.data = [ide_ele] * (2 * self.N0)
        self.segfunc = segfunc
        
        for i, x in enumerate(init_value):
            self.data[i + self.N0 - 1] = x
        for i in range(self.N0 - 2, -1, -1):
            self.data[i] = self.segfunc(self.data[2 * i + 1], self.data[2 * i + 2])
    
    def update(self, k: int, x):
        k += self.N0 - 1
        ################################################################
        self.data[k] = x
        ################################################################
        while k:
            k = (k - 1) // 2
            self.data[k] = self.segfunc(self.data[k * 2 + 1], self.data[k * 2 + 2])
    
    def query(self, left: int, right: int):
        L = left + self.N0
        R = right + self.N0
        res = self.ide_ele
        ################################################################
        a, b = [], []
        while L < R:
            if L & 1:
                a.append(L - 1)
                L += 1
            if R & 1:
                R -= 1
                b.append(R - 1)
            L >>= 1
            R >>= 1
        for i in a + b[::-1]:
            res = self.segfunc(res, self.data[i])
        ################################################################
        return res


class LazySegmentTree:
    def __init__(self, init_value: list, segfunc, ide_ele=0, lazy_ide_ele=0):
        self.ide_ele = ide_ele
        self.lazy_ide_ele = lazy_ide_ele
        self.segfunc = segfunc
        n = len(init_value)
        self.N0 = 1 << (n - 1).bit_length()
        self.data = [self.ide_ele] * (2 * self.N0)
        self.lazy = [self.lazy_ide_ele] * (2 * self.N0)
        
        for i, x in enumerate(init_value):
            self.data[i + self.N0 - 1] = x
        for i in range(self.N0 - 2, -1, -1):
            self.data[i] = segfunc(self.data[2 * i + 1], self.data[2 * i + 2])
    
    def gindex(self, left, right):
        L = left + self.N0
        R = right + self.N0
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1
            R >>= 1
        while L:
            yield L
            L >>= 1
    
    def propagates(self, *ids):
        for i in reversed(ids):
            idx = i - 1
            v = self.lazy[idx]
            if v == self.lazy_ide_ele:
                continue
            ################################################################
            self.data[2 * idx + 1] += v >> 1
            self.data[2 * idx + 2] += v >> 1
            self.lazy[2 * idx + 1] += v >> 1
            self.lazy[2 * idx + 2] += v >> 1
            ################################################################
            self.lazy[idx] = self.lazy_ide_ele
    
    def update(self, left: int, right: int, x):
        ids = tuple(self.gindex(left, right))
        ################################################################
        # self.propagates(*ids)
        ################################################################
        L = self.N0 + left
        R = self.N0 + right
        
        while L < R:
            if R & 1:
                R -= 1
                ################################################################
                self.lazy[R - 1] += x
                self.data[R - 1] += x
                ################################################################
            if L & 1:
                ################################################################
                self.lazy[L - 1] += x
                self.data[L - 1] += x
                ################################################################
                L += 1
            L >>= 1
            R >>= 1
            ################################################################
            x <<= 1
            ################################################################
        for i in ids:
            idx = i - 1
            self.data[idx] = self.segfunc(self.data[2 * idx + 1], self.data[2 * idx + 2]) + self.lazy[idx]
    
    def query(self, left: int, right: int):
        self.propagates(*self.gindex(left, right))
        L = left + self.N0
        R = right + self.N0
        res = self.ide_ele
        ################################################################
        a, b = [], []
        while L < R:
            if L & 1:
                a.append(L - 1)
                L += 1
            if R & 1:
                R -= 1
                b.append(R - 1)
            L >>= 1
            R >>= 1
        for i in a + b[::-1]:
            res = self.segfunc(res, self.data[i])
        ################################################################
        return res


class DualSegmentTree:
    def __init__(self, size: int, segfunc, lazy_ide_ele=0):
        self.lazy_ide_ele = lazy_ide_ele
        self.segfunc = segfunc
        self.N0 = 1 << (size - 1).bit_length()
        self.lazy = [self.lazy_ide_ele] * (2 * self.N0)
    
    def gindex(self, left, right):
        L = left + self.N0
        R = right + self.N0
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1
            R >>= 1
        while L:
            yield L
            L >>= 1
    
    def propagates(self, *ids):
        for i in reversed(ids):
            idx = i - 1
            v = self.lazy[idx]
            if v == self.lazy_ide_ele:
                continue
            self.lazy[2 * idx + 1] = self.segfunc(self.lazy[2 * idx + 1], v)
            self.lazy[2 * idx + 2] = self.segfunc(self.lazy[2 * idx + 2], v)
            self.lazy[idx] = self.lazy_ide_ele
    
    def update(self, left: int, right: int, x):
        L = self.N0 + left
        R = self.N0 + right
        
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R - 1] = self.segfunc(self.lazy[R - 1], x)
            if L & 1:
                self.lazy[L - 1] = self.segfunc(self.lazy[L - 1], x)
                L += 1
            L >>= 1
            R >>= 1
    
    def query(self, k: int):
        self.propagates(*self.gindex(k, k + 1))
        return self.lazy[k + self.N0 - 1]


class LowestCommonAncestor:
    def __init__(self, tree, root):
        self.n = len(tree)
        self.depth = [0] * self.n
        self.log_size = self.n.bit_length()
        self.parent = [[-1] * self.n for _ in range(self.log_size)]
        
        q = deque([(root, -1, 0)])
        while q:
            v, par, dist = q.pop()
            self.parent[0][v] = par
            self.depth[v] = dist
            for child in tree[v]:
                if child != par:
                    self.depth[child] = dist + 1
                    q.append((child, v, dist + 1))
        
        for k in range(1, self.log_size):
            for v in range(self.n):
                self.parent[k][v] = self.parent[k - 1][self.parent[k - 1][v]]
    
    def query(self, u, v):
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        for k in range(self.log_size):
            if self.depth[v] - self.depth[u] >> k & 1:
                v = self.parent[k][v]
        if u == v:
            return u
        
        for k in reversed(range(self.log_size)):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][v]
    
    def get_dist(self, u, v):
        ancestor = self.query(u, v)
        return self.depth[u] - self.depth[ancestor] + self.depth[v] - self.depth[ancestor]


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = None
        self.it = None
    
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.graph[fr].append(forward)
        self.graph[to].append(backward)
    
    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.graph[v1].append(edge1)
        self.graph[v2].append(edge2)
    
    def bfs(self, s, t):
        self.level = level = [-1] * self.n
        deq = deque([s])
        level[s] = 0
        G = self.graph
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] == -1:
                    level[w] = lv
                    deq.append(w)
        return level[t] != -1
    
    def dfs(self, v, t, f):
        if v == t:
            return f
        for e in self.it[v]:
            w, cap, rev = e
            if cap and self.level[v] < self.level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0
    
    def flow(self, s, t):
        flow = 0
        INF = 10 ** 18
        while self.bfs(s, t):
            *self.it, = map(iter, self.graph)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


class HopcroftKarp:
    def __init__(self, N0, N1):
        self.N0 = N0
        self.N1 = N1
        self.N = N = 2 + N0 + N1
        self.graph = [[] for _ in range(N)]
        self.level = None
        self.it = None
        for i in range(N0):
            forward = [2 + i, 1, None]
            forward[2] = backward = [0, 0, forward]
            self.graph[0].append(forward)
            self.graph[2 + i].append(backward)
        self.backwards = bs = []
        for i in range(N1):
            forward = [1, 1, None]
            forward[2] = backward = [2 + N0 + i, 0, forward]
            bs.append(backward)
            self.graph[2 + N0 + i].append(forward)
            self.graph[1].append(backward)
    
    def add_edge(self, fr, to):
        v0 = 2 + fr
        v1 = 2 + self.N0 + to
        forward = [v1, 1, None]
        forward[2] = backward = [v0, 0, forward]
        self.graph[v0].append(forward)
        self.graph[v1].append(backward)
    
    def bfs(self):
        graph = self.graph
        level = [-1] * self.N
        deq = deque([0])
        level[0] = 0
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in graph[v]:
                if cap and level[w] == -1:
                    level[w] = lv
                    deq.append(w)
        self.level = level
        return level[1] != -1
    
    def dfs(self, v, t):
        if v == t:
            return 1
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w] and self.dfs(w, t):
                e[1] = 0
                rev[1] = 1
                return 1
        return 0
    
    def flow(self):
        flow = 0
        graph = self.graph
        bfs = self.bfs
        dfs = self.dfs
        while bfs():
            *self.it, = map(iter, graph)
            while dfs(0, 1):
                flow += 1
        return flow
    
    def matching(self):
        return [cap for _, cap, _ in self.backwards]


def upsqrt(x):
    k = x ** 0.5
    res = 1
    while res < k:
        res <<= 1
    return res


def botsqrt(x):
    k = x ** 0.5
    res = 1
    while res <= k:
        res <<= 1
    return res >> 1


class VanEmdeBoasTree:
    def __init__(self, size):
        self.universe_size = 1
        while self.universe_size < size:
            self.universe_size <<= 1
        self.minimum = -1
        self.maximum = -1
        self.summary = None
        self.cluster = {}
    
    def __high(self, x):
        return x // botsqrt(self.universe_size)
    
    def __low(self, x):
        return x % botsqrt(self.universe_size)
    
    def __generate_index(self, x, y):
        return x * botsqrt(self.universe_size) + y
    
    def min(self):
        return self.minimum
    
    def max(self):
        return self.maximum
    
    def __empinsert(self, key):
        self.minimum = self.maximum = key
    
    def insert(self, key):
        if self.minimum == -1:
            self.__empinsert(key)
        else:
            if key < self.minimum:
                self.minimum, key = key, self.minimum
            if 2 < self.universe_size:
                if self.__high(key) not in self.cluster:
                    self.cluster[self.__high(key)] = VanEmdeBoasTree(botsqrt(self.universe_size))
                    if self.summary is None:
                        self.summary = VanEmdeBoasTree(upsqrt(self.universe_size))
                    self.summary.insert(self.__high(key))
                    self.cluster[self.__high(key)].__empinsert(self.__low(key))
                else:
                    self.cluster[self.__high(key)].insert(self.__low(key))
            if self.maximum < key:
                self.maximum = key
    
    def is_member(self, key):
        if self.minimum == key or self.maximum == key:
            return True
        elif self.universe_size == 2:
            return False
        else:
            if self.__high(key) in self.cluster:
                return self.cluster[self.__high(key)].is_member(self.__low(key))
            else:
                return False
    
    def successor(self, key):
        if self.universe_size == 2:
            if key == 0 and self.maximum == 1:
                return 1
            else:
                return -1
        elif self.minimum != -1 and key < self.minimum:
            return self.minimum
        else:
            max_incluster = -1
            if self.__high(key) in self.cluster:
                max_incluster = self.cluster[self.__high(key)].max()
            if max_incluster != -1 and self.__low(key) < max_incluster:
                offset = self.cluster[self.__high(key)].successor(self.__low(key))
                return self.__generate_index(self.__high(key), offset)
            else:
                succ_cluster = self.summary.successor(self.__high(key))
                if succ_cluster == -1:
                    return -1
                else:
                    offset = self.cluster[succ_cluster].min()
                    return self.__generate_index(succ_cluster, offset)
    
    def predecessor(self, key):
        if self.universe_size == 2:
            if key == 1 and self.minimum == 0:
                return 0
            else:
                return -1
        elif self.maximum != -1 and self.maximum < key:
            return self.maximum
        else:
            min_incluster = -1
            if self.__high(key) in self.cluster:
                min_incluster = self.cluster[self.__high(key)].min()
            if min_incluster != -1 and min_incluster < self.__low(key):
                offset = self.cluster[self.__high(key)].predecessor(self.__low(key))
                return self.__generate_index(self.__high(key), offset)
            else:
                pred_cluster = -1
                if self.summary is not None:
                    pred_cluster = self.summary.predecessor(self.__high(key))
                if pred_cluster == -1:
                    if self.minimum != -1 and self.minimum < key:
                        return self.minimum
                    else:
                        return -1
                else:
                    offset = self.cluster[pred_cluster].max()
                    return self.__generate_index(pred_cluster, offset)
    
    def delete(self, key):
        if self.minimum == self.maximum:
            self.minimum = self.maximum = -1
            return True
        elif self.universe_size == 2:
            if key == 0:
                self.minimum = 1
            else:
                self.minimum = 0
            self.maximum = self.minimum
            return False
        else:
            if key == self.minimum:
                first_cluster = self.summary.min()
                key = self.__generate_index(first_cluster, self.cluster[first_cluster].min())
                self.minimum = key
            flg0 = self.cluster[self.__high(key)].delete(self.__low(key))
            if flg0:
                del self.cluster[self.__high(key)]
                flg1 = self.summary.delete(self.__high(key))
                if key == self.maximum:
                    if flg1:
                        self.maximum = self.minimum
                    else:
                        max_insummary = self.summary.max()
                        self.maximum = self.__generate_index(max_insummary, self.cluster[max_insummary].max())
            elif key == self.maximum:
                self.maximum = self.__generate_index(self.__high(key), self.cluster[self.__high(key)].max())
