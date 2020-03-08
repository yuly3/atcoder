N, u, v = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    dist = [-1 for _ in range(N+1)]
    stack = [v]
    dist[v] = 0
    while stack:
        v = stack.pop()
        dist_x = dist[v] + 1
        for child in graph[v]:
            if 0 <= dist[child]:
                continue
            dist[child] = dist_x
            stack.append(child)
    return dist


def solve():
    dist_u, dist_v = dfs(u), dfs(v)
    
    ans = 0
    for a, b in zip(dist_u[1:], dist_v[1:]):
        if a < b:
            ans = max(ans, b-1)
    print(ans)


if __name__ == '__main__':
    solve()
