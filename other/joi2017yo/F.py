import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.buffer.readline


def solve():
    N, M, X = map(int, rl().split())
    T = [int(rl()) for _ in range(N)]
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, d = map(int, rl().split())
        a, b = a - 1, b - 1
        graph[a].append((b, d))
        graph[b].append((a, d))
    
    INF = 10 ** 18
    costs = [[[INF] * 2 for _ in range(201)] for _ in range(10000)]
    costs[0][X][0] = 0
    hq = [(0, 0, X, 0)]
    while hq:
        cost, cur, ct, last_param = heappop(hq)
        if costs[cur][ct][last_param] < cost:
            continue
        for child, d in graph[cur]:
            child_t = T[child]
            if child_t == 1:
                nct = max(0, ct - d)
                nlast_param = last_param
            elif child_t == 0:
                if last_param == 1 and d < ct:
                    continue
                nct = X
                nlast_param = 0
            else:
                if last_param == 0 and d < ct:
                    continue
                nct = X
                nlast_param = 1
            ncost = cost + d
            if ncost < costs[child][nct][nlast_param]:
                costs[child][nct][nlast_param] = ncost
                heappush(hq, (ncost, child, nct, nlast_param))
    
    ans = INF
    for costs_n in costs[N - 1]:
        ans = min(ans, min(costs_n))
    print(ans)


if __name__ == '__main__':
    solve()
