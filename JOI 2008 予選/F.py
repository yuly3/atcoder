def solve():
    n, k = map(int, input().split())
    INF = 1000000 * 1000
    graph = [[INF if i != j else 0 for i in range(n)] for j in range(n)]
    
    for _ in range(k):
        cmd, *data = map(int, input().split())
        if cmd == 0:
            u, v = data[0] - 1, data[1] - 1
            ans = graph[u][v] if graph[u][v] < INF else -1
            print(ans)
        else:
            u, v, cost = data[0] - 1, data[1] - 1, data[2]
            if graph[u][v] <= cost:
                continue
            for i in range(n):
                for j in range(i + 1, n):
                    min_cost = min(graph[i][u] + cost + graph[v][j], graph[i][v] + cost + graph[u][j], graph[i][j])
                    graph[i][j] = graph[j][i] = min_cost


if __name__ == '__main__':
    solve()
