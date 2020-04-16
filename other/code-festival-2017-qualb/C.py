import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def is_bipartite(graph, colors):
    stack = [(0, 1)]
    while stack:
        v, color = stack.pop()
        colors[v] = color
        for child in graph[v]:
            if colors[child] == color:
                return False
            if colors[child] == 0:
                stack.append((child, -color))
    return True


def solve():
    N, M = map(int, rl().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, rl().split())
        graph[a].append(b)
        graph[b].append(a)
    
    colors = [0] * N
    if is_bipartite(graph, colors):
        w = colors.count(1)
        ans = w * (N - w) - M
    else:
        ans = N * (N - 1) // 2 - M
    print(ans)


if __name__ == '__main__':
    solve()
