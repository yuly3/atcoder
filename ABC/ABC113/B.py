def solve():
    N, T, A, *H = map(int, open(0).read().split())
    
    aveT = [0] * N
    for i in range(N):
        aveT[i] = T - H[i] * 0.006
    
    ans, d_min = 0, 10 ** 5
    for i in range(N):
        if abs(A - aveT[i]) < d_min:
            ans = i + 1
            d_min = abs(A - aveT[i])
    print(ans)


if __name__ == '__main__':
    solve()
