import sys
from collections import deque

rl = sys.stdin.readline


def solve():
    N = int(rl())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, rl().split())
        u -= 1
        v -= 1
        graph[u].append([v, w])
        graph[v].append([u, w])
    
    ans = [-1] * N
    stack = deque([[0, 0]])
    while stack:
        node, dist = stack.pop()
        for child, weight in graph[node]:
            if ans[child] != -1:
                continue
            nd = dist + weight
            if nd % 2 == 0:
                ans[child] = 0
            else:
                ans[child] = 1
            stack.append([child, nd])
    
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    solve()
