import algorithm, heapqueue, math, sequtils, strutils


type Ele = tuple
    t, cur, s: int

proc `<`(a, b: Ele): bool = a.t < b.t


var
    cost: array[50, array[2501, int]]
    heapque: HeapQueue[Ele]


proc solve() =
    var N, M, S: int
    (N, M, S) = stdin.readLine.split.map(parseInt)
    var
        graph = newSeqWith(N, newSeq[(int, int, int)]())
        u, v, a, b: int
    for _ in 0..<M:
        (u, v, a, b) = stdin.readLine.split.map(parseInt)
        dec u; dec v
        graph[u].add((v, a, b))
        graph[v].add((u, a, b))
    var C, D: array[50, int]
    for i in 0..<N:
        (C[i], D[i]) = stdin.readLine.split.map(parseInt)
    
    let init_s = min(2500, S)
    for i in 0..<N:
        cost[i].fill(10^18)
    cost[0][init_s] = 0

    heapque = initHeapQueue[Ele]()
    heapque.push((0, 0, init_s))
    var self_roop_s, self_roop_t, t, cur, s, n_t, n_s: int
    while heapque.len != 0:
        (t, cur, s) = heapque.pop()
        self_roop_s = min(2500, s + C[cur])
        self_roop_t = t + D[cur]
        if self_roop_t < cost[cur][self_roop_s]:
            cost[cur][self_roop_s] = self_roop_t
            heapque.push((self_roop_t, cur, self_roop_s))
        for (to, s_cost, t_cost) in graph[cur]:
            if s < s_cost:
                continue
            n_t = t + t_cost
            n_s = s - s_cost
            if n_t < cost[to][n_s]:
                cost[to][n_s] = n_t
                heapque.push((n_t, to, n_s))
    
    var ans = newSeq[int](N - 1)
    for i in 1..<N:
        ans[i - 1] = min(cost[i])
    echo ans.join("\n")


when is_main_module:
    solve()
