import sequtils, strutils, math

const MOD = 10^9 + 7
var
    N = stdin.readLine.parseInt
    graph = newSeqWith(N + 1, newSeq[int]())
    dp: array[10^5 + 1, array[2, int]]


proc dfs(v, parent: int) =
    (dp[v][0], dp[v][1]) = (1, 1)
    for child in graph[v]:
        if child != parent:
            dfs(child, v)
            dp[v][0] = dp[v][0] * (dp[child][0] + dp[child][1]) mod MOD
            dp[v][1] = dp[v][1] * dp[child][0] mod MOD


proc solve() =
    for _ in 0..<N - 1:
        var x, y: int
        (x, y) = stdin.readLine.split.map(parseInt)
        graph[x].add(y)
        graph[y].add(x)
    
    dfs(1, 0)
    var ans = sum(dp[1]) mod MOD
    echo ans


when is_main_module:
    solve()
