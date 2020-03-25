import sys
sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(lambda x: int(x) - 1, rl().split())
        graph[a].append(b)
        graph[b].append(a)
    
    fen_dist, sun_dist = [0] * N, [0] * N
    
    def dfs1(node, parent, dist):
        fen_dist[node] = dist
        for child in graph[node]:
            if child != parent:
                dfs1(child, node, dist + 1)
    
    def dfs2(node, parent, dist):
        sun_dist[node] = dist
        for child in graph[node]:
            if child != parent:
                dfs2(child, node, dist + 1)
    
    dfs1(0, -1, 0)
    dfs2(N - 1, -1, 0)
    
    cnt_fen, cnt_sun = 0, 0
    for i in range(N):
        if fen_dist[i] <= sun_dist[i]:
            cnt_fen += 1
        else:
            cnt_sun += 1
    
    if cnt_fen <= cnt_sun:
        print('Snuke')
    else:
        print('Fennec')


if __name__ == '__main__':
    solve()
