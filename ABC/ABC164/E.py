import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, S = map(int, rl().split())
    init_s = min(2500, S)
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v, a, b = map(int, rl().split())
        u, v = u - 1, v - 1
        graph[u].append((v, a, b))
        graph[v].append((u, a, b))
    C, D = [0] * N, [0] * N
    for i in range(N):
        C[i], D[i] = map(int, rl().split())
    
    costs = [[10 ** 18] * 2501 for _ in range(N)]
    costs[0][init_s] = 0
    
    que = [(0, 0, init_s)]
    while que:
        t, cur, s = heappop(que)
        self_roop_s = min(s + C[cur], 2500)
        self_roop_t = t + D[cur]
        if self_roop_t < costs[cur][self_roop_s]:
            costs[cur][self_roop_s] = self_roop_t
            heappush(que, (self_roop_t, cur, self_roop_s))
        for child, s_cost, t_cost in graph[cur]:
            if s < s_cost:
                continue
            nt = t + t_cost
            ns = s - s_cost
            if nt < costs[child][ns]:
                costs[child][ns] = nt
                heappush(que, (nt, child, ns))
    
    for costs_i in costs[1:]:
        print(min(costs_i))


if __name__ == '__main__':
    solve()
