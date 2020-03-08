def solve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = list(input())
    
    ans = 0
    for i in range(K):
        if T[i] == 'r':
            ans += P
        elif T[i] == 's':
            ans += R
        else:
            ans += S
    for i in range(K, N):
        if T[i-K] != T[i]:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R
            else:
                ans += S
        else:
            T[i] = 'n'
    print(ans)


if __name__ == '__main__':
    solve()
