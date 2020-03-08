def solve():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    ans = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]
    print(ans)


if __name__ == '__main__':
    solve()
