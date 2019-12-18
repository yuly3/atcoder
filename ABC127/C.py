def solve():
    N, M = map(int, input().split())
    L = [0 for _ in range(M)]
    R = [0 for _ in range(M)]
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    
    ans = max(0, min(R) - max(L) + 1)
    print(ans)


if __name__ == '__main__':
    solve()