import sequtils, strutils, algorithm

var
    N = stdin.readLine.parseInt
    a = stdin.readLine.split.map(parseInt)
    dp: array[301, array[301, array[301, float]]]

proc dfs(i, j, k:int): float =
    if 0 <= dp[i][j][k]:
        return dp[i][j][k]
    if i == 0 and j == 0 and k == 0:
        return 0
    
    var res: float = 0
    if 0 < i:
        res += dfs(i-1, j, k) * float(i)
    if 0 < j:
        res += dfs(i+1, j-1, k) * float(j)
    if 0 < k:
        res += dfs(i, j+1, k-1) * float(k)
    res += float(N)
    res *= 1 / float(i + j + k)
    dp[i][j][k] = res
    return res

proc solve() =
    for i in 0..N:
        for j in 0..N:
            dp[i][j].fill(-1.0)
    
    var one, two, three: int
    (one, two, three) = (0, 0, 0)
    for ai in a:
        if ai == 1:
            one += 1
        elif ai == 2:
            two += 1
        else:
            three += 1
    var ans = dfs(one, two, three)
    echo ans

when is_main_module:
    solve()
