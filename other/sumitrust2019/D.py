def solve():
    N = int(input())
    S = input()
    
    ans = 0
    memo1 = set()
    for i in range(N - 2):
        si = int(S[i])
        if si in memo1:
            continue
        memo1.add(si)
        memo2 = set()
        for j in range(i + 1, N - 1):
            sj = int(S[j])
            if sj in memo2:
                continue
            memo2.add(sj)
            ans += len(set(S[j + 1:]))
    print(ans)


if __name__ == '__main__':
    solve()
