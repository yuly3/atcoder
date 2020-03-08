import strutils, sequtils, math

var
    graph: seq[seq[int]]
    searched: array[1000^2, int]
    dist: array[1000^2, int]


proc encode(i, j: int): int =
    let (i, j) = if i < j: (i, j) else: (j, i)
    return j * (j - 1) div 2 + i + 1


proc dfs(cur: int): int =
    if searched[cur] == 2:
        return dist[cur]
    
    searched[cur] = 1
    for child in graph[cur]:
        if searched[child] == 1:
            echo -1
            quit()
        dist[cur] = max(dist[cur], dfs(child) + 1)
    searched[cur] = 2
    return dist[cur]


proc solve() =
    var N = stdin.readLine.parseInt
    graph = newSeqWith(N * (N - 1) div 2 + 1, newSeq[int]())
    for i in 0..<N:
        var now = 0
        let ai = stdin.readLine.split.mapIt(it.parseInt - 1)
        for j in ai:
            let next = encode(i, j)
            graph[now].add(next)
            now = next
    
    var ans = dfs(0)
    echo ans


when is_main_module:
    solve()
