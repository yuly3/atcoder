import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        ai, bi, ci = rl().split()
        ai, bi = int(ai) - 1, int(bi) - 1
        graph[ai].append((bi, ci))
        graph[bi].append((ai, ci))
    
    que = deque([(0, N - 1, 0)])
    searched = set()
    searched.add((0, N - 1))
    ans = 10 ** 18
    while que:
        u, v, d = que.popleft()
        for u_to, cu in graph[u]:
            for v_to, cv in graph[v]:
                if cu != cv or (u_to, v_to) in searched:
                    continue
                searched.add((u_to, v_to))
                if u == v_to or v == u_to:
                    ans = min(ans, 2 * d + 1)
                    continue
                if u_to == v_to:
                    ans = min(ans, 2 * (d + 1))
                    continue
                que.append((u_to, v_to, d + 1))
    print(ans if ans != 10 ** 18 else -1)


if __name__ == '__main__':
    solve()
