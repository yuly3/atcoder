import sys
sys.setrecursionlimit(10**7)

N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    edges[u].append([v, w])
    edges[v].append([u, w])
ans = [-1 for _ in range(N)]


def dfs(edge, pd):
    for child, d in edges[edge]:
        if ans[child-1] != -1:
            continue
        cd = pd + d
        if cd % 2 == 0:
            ans[child-1] = 0
        else:
            ans[child-1] = 1
        dfs(child, cd)


def solve():
    dfs(1, 0)
    for i in range(N):
        print(ans[i])


if __name__ == '__main__':
    solve()
