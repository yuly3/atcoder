def solve():
    N, K, M, *A = map(int, open(0).read().split())
    
    target = N * M
    ans = target - sum(A)
    if K < ans:
        print(-1)
    elif ans < 0:
        print(0)
    else:
        print(ans)


if __name__ == '__main__':
    solve()
