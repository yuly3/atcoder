def solve():
    N, K = map(int, input().split())
    
    m_max = (N - 1) * (N - 2) // 2
    if m_max < K:
        print(-1)
        exit()
    
    M = 0
    graph = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        graph[1].append(i)
        M += 1
    
    cnt = m_max - K
    for i in range(2, N):
        for j in range(i + 1, N + 1):
            if cnt == 0:
                break
            graph[i].append(j)
            cnt -= 1
            M += 1
        else:
            continue
        break
    
    print(M)
    for parent in range(1, N + 1):
        for child in graph[parent]:
            print(parent, child)


if __name__ == '__main__':
    solve()
