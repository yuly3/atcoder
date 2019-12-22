def solve():
    N = int(input())
    S, T = map(str, input().split())
    
    ans = []
    for i in range(N):
        ans.append(S[i]+T[i])
    print(''.join(ans))


if __name__ == '__main__':
    solve()
