def solve():
    N, M = map(int, input().split())
    
    if N == 1 and M == 1:
        print(1)
        exit()
    
    if M < N:
        N, M = M, N
    if N == 1:
        print(M - 2)
        exit()
    
    print((N - 2) * (M - 2))


if __name__ == '__main__':
    solve()
