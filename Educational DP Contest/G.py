import sys

sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

dp = [-1] * (10 ** 5 + 1)


def dfs(v):
    if dp[v] != -1:
        return dp[v]

    res = 0
    for child in graph[v]:
        res = max(res, dfs(child) + 1)
    dp[v] = res
    return res


def solve():
    ans = 0
    for v in range(1, N + 1):
        ans = max(ans, dfs(v))
    print(ans)


if __name__ == '__main__':
    solve()
