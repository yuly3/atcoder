import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, Q = map(int, rl().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(lambda node: int(node) - 1, rl().split())
        graph[u].append(v)
        graph[v].append(u)
    c = list(map(int, rl().split()))
    
    ans = []
    for _ in range(Q):
        cmd, *xy = map(int, rl().split())
        if cmd == 1:
            x = xy[0] - 1
            ans.append(c[x])
            for child in graph[x]:
                c[child] = c[x]
        else:
            x, y = xy
            x -= 1
            ans.append(c[x])
            c[x] = y
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
