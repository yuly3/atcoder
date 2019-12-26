N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
ans = 0


def dfs(v, history):
    if len(history) == N:
        global ans
        ans += 1
    else:
        children = graph[v]
        for child in children:
            if child not in history:
                dfs(child, history + (child,))


def solve():
    dfs(1, (1,))
    print(ans)


if __name__ == '__main__':
    solve()
