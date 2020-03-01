from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import bellman_ford, NegativeCycleError


def reachable_nodes(s, edges):
    cur = {s}
    reachable = set()
    while cur:
        reachable |= cur
        cur = set().union(*(edges[node] for node in cur)) - reachable
    return reachable


def solve():
    N, M, P = map(int, input().split())
    A, B, C = [0] * M, [0] * M, [0] * M
    to = [[] for _ in range(N)]
    reverse_to = [[] for _ in range(N)]
    for i in range(M):
        a, b, c = map(int, input().split())
        A[i], B[i], C[i] = a - 1, b - 1, P - c
        to[a - 1].append(b - 1)
        reverse_to[b - 1].append(a - 1)
    
    reachable = reachable_nodes(0, to) & reachable_nodes(N - 1, reverse_to)
    
    edge_dict = dict()
    for a, b, c in zip(A, B, C):
        if a in reachable and b in reachable:
            edge_dict[(a, b)] = min(c, edge_dict.get((a, b), 10 ** 6))
    AA, BB, CC = [], [], []
    for (a, b), c in edge_dict.items():
        AA.append(a)
        BB.append(b)
        CC.append(c)
    
    graph = csr_matrix((CC, (AA, BB)), shape=(N, N))
    try:
        bf = bellman_ford(graph, indices=[0])
        print(max(0, -int(bf[0][N - 1])))
    except NegativeCycleError:
        print(-1)


if __name__ == '__main__':
    solve()
