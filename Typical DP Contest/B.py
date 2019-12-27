def solve():
    A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    dp = [[0 for _ in range(B+1)] for _ in range(A+1)]
    for i in range(A+1)[::-1]:
        for j in range(B+1)[::-1]:
            if i+j == A+B:
                continue
            
            if (i+j) % 2 == 0:
                if i == A:
                    dp[i][j] = dp[i][j+1] + b[j]
                elif j == B:
                    dp[i][j] = dp[i+1][j] + a[i]
                else:
                    dp[i][j] = max(dp[i][j+1] + b[j], dp[i+1][j] + a[i])
            
            else:
                if i == A:
                    dp[i][j] = dp[i][j+1]
                elif j == B:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = min(dp[i][j+1], dp[i+1][j])
    print(dp[0][0])


if __name__ == '__main__':
    solve()
