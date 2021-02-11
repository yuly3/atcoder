import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    a = list(map(int, rl().split()))
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        left, right, c = map(int, rl().split())
        graph[left - 1].append((right, c))
    
    for i, ai in enumerate(a):
        graph[i].append((i + 1, ai))
    for i in range(1, N + 1):
        graph[i].append((i - 1, 0))
    
    dist = [10 ** 18] * (N + 1)
    que = [(0, 0)]
    while que:
        prev_cost, cur = heappop(que)
        if cur == N:
            print(sum(a) - prev_cost)
            return
        if dist[cur] < prev_cost:
            continue
        for to, cost in graph[cur]:
            next_cost = prev_cost + cost
            if dist[to] <= next_cost:
                continue
            dist[to] = next_cost
            heappush(que, (next_cost, to))


if __name__ == '__main__':
    solve()
