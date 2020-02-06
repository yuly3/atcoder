import strutils, sequtils, math

var
    N: int
    graph: seq[seq[int]]
    dp: array[10^5 + 1, array[2, int]]
const MOD = 10^9 + 7


proc dfs(cur, parent: int) =
    dp[cur][0] = 1
    dp[cur][1] = 1

    for child in graph[cur]:
        if child != parent:
            dfs(child, cur)
            dp[cur][0] = dp[cur][0] * sum(dp[child]) mod MOD
            dp[cur][1] = dp[cur][1] * dp[child][0] mod MOD


proc solve() =
    N = stdin.readLine.parseInt
    graph = newSeqWith(N+1, newSeq[int]())
    var a, b: int
    for _ in 0..<N-1:
        (a, b) = stdin.readLine.split.map(parseInt)
        graph[a].add(b)
        graph[b].add(a)
    
    dfs(1, -1)
    echo sum(dp[1]) mod MOD


when is_main_module:
    solve()
