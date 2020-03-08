import sys
sys.setrecursionlimit(10**7)

MOD = 1000000007
N, K = map(int, input().split())
edges = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    edges[a].append(b)
    edges[b].append(a)

colors = [K] + [0 for _ in range(N-1)]


def dfs(parent, edge, n):
    for child in edges[edge]:
        if child != parent:
            colors[child] = max(0, n)
            n -= 1
            dfs(edge, child, K-2)


def solve():
    dfs(0, 0, K-1)
    
    ans = K
    for color in colors[1:]:
        ans *= color
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    solve()
