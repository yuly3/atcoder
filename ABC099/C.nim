import strutils

var
    N: int
    dp: array[100001, int]
const INF = 100001


proc dfs(t: int): int =
    if t == 0:
        return 0
    if 0 < dp[t]:
        return dp[t]
    
    var res = INF
    res = min(res, dfs(t - 1) + 1)

    var x = 6
    while x <= t:
        res = min(res, dfs(t - x) + 1)
        x *= 6
    
    x = 9
    while x <= t:
        res = min(res, dfs(t - x) + 1)
        x *= 9
    
    dp[t] = res
    return res


proc solve() =
    N = stdin.readLine.parseInt
    var ans = dfs(N)
    echo ans


when is_main_module:
    solve()
