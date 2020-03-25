import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    graph = []
    for _ in range(M):
        a, b, c = map(int, rl().split())
        a -= 1
        b -= 1
        c *= -1
        graph.append([a, b, c])
    
    def bellman_ford(s):
        dist_ls = [10 ** 15] * N
        dist_ls[s] = 0
        for i in range(N):
            for u, v, w in graph:
                if dist_ls[u] + w < dist_ls[v]:
                    dist_ls[v] = dist_ls[u] + w
                    if i == N - 1 and v == N - 1:
                        return -1
        return dist_ls
    
    dist = bellman_ford(0)
    if dist == -1:
        print('inf')
    else:
        print(-dist[-1])


if __name__ == '__main__':
    solve()
