def solve():
    N, M = map(int, input().split())
    
    graph = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].add(b)
        graph[b].add(a)
    
    for i in range(N):
        candidate = set()
        for child in graph[i]:
            candidate |= graph[child]
        print(max(0, len(candidate - graph[i]) - 1))


if __name__ == '__main__':
    solve()
