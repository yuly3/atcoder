from collections import deque


def solve():
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for i in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    val = [0 for _ in range(N + 1)]
    for i in range(Q):
        p, x = map(int, input().split())
        val[p] += x

    que = deque([1])
    parent = [0 for _ in range(N+1)]
    while que:
        i = que.popleft()
        for j in graph[i]:
            if j == parent[i]:
                continue
            parent[j] = i
            que.append(j)
            val[j] += val[i]

    print(*val[1:])


if __name__ == '__main__':
    solve()
