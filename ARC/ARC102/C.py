def solve():
    N, K = map(int, input().split())
    
    mod_zero, mod_half = 0, 0
    for i in range(1, N+1):
        if i % K == 0:
            mod_zero += 1
        elif i % K == K // 2:
            mod_half += 1
    
    ans = mod_zero ** 3
    if K % 2 == 0:
        ans += mod_half ** 3
    print(ans)


if __name__ == '__main__':
    solve()
