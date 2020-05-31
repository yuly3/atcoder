import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, K, S = map(int, rl().split())
    P, Q = map(int, rl().split())
    C = [int(rl()) - 1 for _ in range(K)]
    A, B = [0] * M, [0] * M
    graph = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(lambda x: int(x) - 1, rl().split())
        graph[a].append(b)
        graph[b].append(a)
        A[i], B[i] = a, b
    
    danger = set()
    que = C
    C = set(C)
    cnt = 0
    while que and cnt < S:
        que_tmp = []
        for cur in que:
            for child in graph[cur]:
                if child in danger:
                    continue
                danger.add(child)
                que_tmp.append(child)
        cnt += 1
        que = que_tmp
    
    graph = [[] for _ in range(N)]
    for i in range(M):
        a, b = A[i], B[i]
        if a in C or b in C:
            continue
        if a == N - 1:
            graph[b].append((a, 0))
        elif a in danger:
            graph[b].append((a, Q))
        else:
            graph[b].append((a, P))
        if b == N - 1:
            graph[a].append((b, 0))
        elif b in danger:
            graph[a].append((b, Q))
        else:
            graph[a].append((b, P))
    
    INF = 10 ** 18
    costs = [INF] * N
    que = [(0, 0)]
    while que:
        cost, cur = heappop(que)
        if costs[cur] < cost:
            continue
        for child, w in graph[cur]:
            ncost = cost + w
            if ncost < costs[child]:
                costs[child] = ncost
                heappush(que, (ncost, child))
    print(costs[-1])


if __name__ == '__main__':
    solve()
