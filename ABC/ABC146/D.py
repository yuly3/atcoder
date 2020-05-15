import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    graph = [[] for _ in range(N)]
    counter = defaultdict(int)
    edges = []
    for _ in range(N - 1):
        a, b = map(lambda x: int(x) - 1, rl().split())
        graph[a].append(b)
        edges.append(b)
        counter[a] += 1
        counter[b] += 1
    
    ans = [0] * N
    
    def bfs(parent, p_color):
        c_color = 1
        for child in graph[parent]:
            if c_color == p_color:
                c_color += 1
            ans[child] = c_color
            bfs(child, c_color)
            c_color += 1
    
    bfs(0, 0)
    print(max(counter.values()))
    for edge in edges:
        print(ans[edge])


if __name__ == '__main__':
    solve()
