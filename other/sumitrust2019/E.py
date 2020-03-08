def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 1000000007
    
    color = [0] * N
    can_use = [0] * (N + 1)
    can_use[0] = 3
    for i in range(N):
        color[i] = can_use[A[i]]
        can_use[A[i]] -= 1
        can_use[A[i] + 1] += 1
    ans = 1
    for c in color:
        ans = ans * c % MOD
    print(ans)


if __name__ == '__main__':
    solve()
