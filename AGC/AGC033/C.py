import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(lambda x: int(x) - 1, rl().split())
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(node):
        searched = [False] * N
        que = deque([(node, 0)])
        v, dist = 0, 0
        while que:
            v, dist = que.popleft()
            searched[v] = True
            for child in graph[v]:
                # noinspection PyTypeChecker
                if not searched[child]:
                    que.append((child, dist + 1))
        return v, dist
    
    e, _ = bfs(0)
    _, diameter = bfs(e)
    print('Second' if diameter % 3 == 1 else 'First')


if __name__ == '__main__':
    solve()
