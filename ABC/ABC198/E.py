import sys
from collections import deque
from math import sqrt

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    C = list(map(int, rl().split()))
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, rl().split())
        graph[a].append(b)
        graph[b].append(a)
    
    boundary = int(sqrt(N))
    que = deque([(1, 0, [])])
    searched = [False] * (N + 1)
    colors = [set() for _ in range(N + 1)]
    ans = []
    while que:
        cur, parent, ss = que.popleft()
        if C[cur - 1] not in colors[parent] and all(C[cur - 1] not in colors[s] for s in ss):
            ans.append(cur)
        if len(colors[parent]) <= boundary:
            colors[cur] = colors[parent] | {C[cur - 1]}
        else:
            colors[cur].add(C[cur - 1])
            ss.append(parent)
        for to in graph[cur]:
            if searched[to]:
                continue
            searched[to] = True
            que.append((to, cur, ss))
    ans.sort()
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    solve()
