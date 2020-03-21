import sys
rline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(rline())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, rline().split())
    a -= 1
    b -= 1
    graph[a].append([b, c])
    graph[b].append([a, c])
to_k = [0] * N


def dfs(node, parent, dist):
    to_k[node] = dist
    
    for child, d in graph[node]:
        if child != parent:
            dfs(child, node, dist + d)


def solve():
    Q, K = map(int, rline().split())
    K -= 1
    dfs(K, -1, 0)
    for _ in range(Q):
        x, y = map(lambda z: int(z) - 1, rline().split())
        print(to_k[x] + to_k[y])


if __name__ == '__main__':
    solve()
