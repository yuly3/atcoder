def solve():
    N, M = map(int, input().split())
    K = [0 for _ in range(N)]
    A = [[] for _ in range(N)]
    for i in range(N):
        K[i], *A[i] = map(int, input().split())
    
    ans = M
    for i in range(1, M+1):
        for j in range(N):
            if i not in A[j]:
                ans -= 1
                break
    print(ans)


if __name__ == '__main__':
    solve()
