def solve():
    S = list(input())
    
    ans, n = 0, len(S)
    for i in range(1, n):
        if S[i-1] == S[i] == '0':
            S[i] = '1'
            ans += 1
        elif S[i-1] == S[i] == '1':
            S[i] = '0'
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
