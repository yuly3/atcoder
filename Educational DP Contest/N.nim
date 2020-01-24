import strutils, sequtils, math

var
    dp: array[401, array[401, int]]
    searched: array[401, array[401, bool]]
    cumsum: array[401, int]
const INF = 10^10*400


proc dfs(l, r: int): int =
    if searched[l][r]:
        return dp[l][r]
    
    searched[l][r] = true
    if r - l == 1:
        return 0
    
    var ans_tmp = INF
    for m in l+1..<r:
        ans_tmp = min(ans_tmp, dfs(l, m) + dfs(m, r))
    dp[l][r] = ans_tmp + cumsum[r] - cumsum[l]
    return dp[l][r]


proc solve() =
    var
        N = stdin.readLine.parseInt
        a = stdin.readLine.split.map(parseInt)
    for i in 1..N:
        cumsum[i] = cumsum[i-1] + a[i-1]
    
    var ans = dfs(0, N)
    echo ans


when is_main_module:
    solve()
