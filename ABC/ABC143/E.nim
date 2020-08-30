import math, sequtils, strutils


type
    Graph[N: static[int]; T] = array[N, array[N, T]]

proc floyd_warshall*(graph: var Graph, n: Natural) =
    for k in 0..<n:
        for i in 0..<n:
            for j in 0..<n:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


const INF = 10^18
var dist, cost: Graph[300, int]


proc solve() =
    var N, M, L, a, b, c: int
    (N, M, L) = stdin.readLine.split.map(parseInt)
    for i in 0..<N:
        for j in 0..<N:
            dist[i][j] = INF
            cost[i][j] = INF
    for _ in 0..<M:
        (a, b, c) = stdin.readLine.split.map(parseInt)
        dec a; dec b
        dist[a][b] = c
        dist[b][a] = c
    
    dist.floyd_warshall(N)
    
    for i in 0..<N:
        for j in 0..<N:
            if dist[i][j] <= L:
                cost[i][j] = 1
    
    cost.floyd_warshall(N)
    
    var
        Q = stdin.readLine.parseInt
        ans = newSeqWith(Q, -1)
        s, t: int
    for i in 0..<Q:
        (s, t) = stdin.readLine.split.mapIt(it.parseInt - 1)
        if cost[s][t] != INF:
            ans[i] = cost[s][t] - 1
    echo ans.join("\n")


when is_main_module:
    solve()
