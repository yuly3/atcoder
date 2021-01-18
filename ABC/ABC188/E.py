import sys
from collections import deque
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    A = list(map(int, rl().split()))
    graph = [[] for _ in range(N)]
    for _ in range(M):
        xi, yi = map(lambda n: int(n) - 1, rl().split())
        graph[xi].append(yi)
    
    B = [(ai, i) for i, ai in enumerate(A)]
    B.sort(key=itemgetter(0))
    
    INF = 10 ** 10
    profit = [-INF] * N
    for ai, i in B:
        que = deque([i])
        while que:
            cur = que.popleft()
            for child in graph[cur]:
                if profit[child] != -INF:
                    continue
                profit[child] = A[child] - ai
                que.append(child)
    print(max(profit))


if __name__ == '__main__':
    solve()
