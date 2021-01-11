import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    a, b = [], []
    ab, ba = dict(), dict()
    graph0 = [[] for _ in range(N)]
    for i in range(N - 1):
        ai, bi = map(lambda n: int(n) - 1, rl().split())
        a.append(ai)
        b.append(bi)
        ab[(ai, bi)] = ba[(bi, ai)] = i
        graph0[ai].append(bi)
        graph0[bi].append(ai)
    
    graph1 = [[] for _ in range(N)]
    p = [False] * (N - 1)
    que = [(-1, 0)]
    while que:
        parent, cur = que.pop()
        for child in graph0[cur]:
            if child == parent:
                continue
            if (cur, child) in ba:
                p[ba[(cur, child)]] = True
            graph1[cur].append(child)
            que.append((cur, child))
    
    c = [0] * N
    Q = int(rl())
    for _ in range(Q):
        ti, ei, xi = map(int, rl().split())
        ei -= 1
        if ti == 1:
            if p[ei]:
                c[a[ei]] += xi
            else:
                c[0] += xi
                c[b[ei]] -= xi
        else:
            if p[ei]:
                c[0] += xi
                c[a[ei]] -= xi
            else:
                c[b[ei]] += xi
    
    que = [0]
    while que:
        cur = que.pop()
        for child in graph1[cur]:
            c[child] += c[cur]
            que.append(child)
    
    print('\n'.join(map(str, c)))


if __name__ == '__main__':
    solve()
