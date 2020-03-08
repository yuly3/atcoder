import strutils, sequtils, math

var
    N, K: int
    graph: seq[seq[int]]
    colors: seq[int]
const MOD = 10^9 + 7


proc dfs(cur, parent, n_color: int) =
    var n = n_color
    for child in graph[cur]:
        if child != parent:
            colors[child] = max(0, n)
            n -= 1
            dfs(child, cur, K - 2)


proc solve() =
    (N, K) = stdin.readLine.split.map(parseInt)
    graph = newSeqWith(N + 1, newSeq[int]())
    var a, b: int
    for _ in 0..<N - 1:
        (a, b) = stdin.readLine.split.map(parseInt)
        graph[a].add(b)
        graph[b].add(a)
    colors = newSeq[int](N + 1)
    
    dfs(1, 0, K - 1)
    
    var ans = K
    for color in colors[2..N]:
        ans = ans * color mod MOD
    echo ans


when is_main_module:
    solve()
