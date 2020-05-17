import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, rl().split())
        graph[a].append(b)
        graph[b].append(a)
    
    ans = [0] * N
    que = deque([0])
    while que:
        cur = que.popleft()
        for child in graph[cur]:
            if ans[child] == 0:
                ans[child] = cur + 1
                que.append(child)
    
    if any(ansi == 0 for ansi in ans[1:]):
        print('No')
    else:
        print('Yes')
        print(*ans[1:], sep='\n')


if __name__ == '__main__':
    solve()
