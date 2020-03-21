def solve():
    N = int(input())
    S1 = input()
    S2 = input()
    MOD = 1000000007
    
    pattern = []
    i = 0
    while i < N:
        if S1[i] == S2[i]:
            pattern.append(0)
            i += 1
        else:
            pattern.append(1)
            i += 2
    
    ans = 3 if pattern[0] == 0 else 6
    for i in range(1, len(pattern)):
        if pattern[i] == 0:
            if pattern[i - 1] == 0:
                ans = ans * 2 % MOD
        else:
            if pattern[i - 1] == 0:
                ans = ans * 2 % MOD
            else:
                ans = ans * 3 % MOD
    print(ans)


if __name__ == '__main__':
    solve()
