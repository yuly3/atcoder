import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    graph = [[] for _ in range(N)]
    indegrees = defaultdict(int)
    for _ in range(N - 1 + M):
        a, b = map(lambda x: int(x) - 1, rl().split())
        graph[a].append(b)
        indegrees[b] += 1
    
    que = deque([])
    for i in range(N):
        if indegrees[i] == 0:
            que.append(i)
    
    ans = [0] * N
    while que:
        idx = que.pop()
        for child in graph[idx]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                que.append(child)
                ans[child] = idx + 1
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
