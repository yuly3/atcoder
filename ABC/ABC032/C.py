def solve():
    N, K, *s = map(int, open(0).read().split())
    
    if 0 in s:
        print(N)
        exit()
    
    ans, prodoct, j = 0, 1, 0
    for i in range(N):
        while j < N:
            prodoct *= s[j]
            if K < prodoct:
                j += 1
                break
            ans = max(ans, j - i + 1)
            j += 1
        prodoct //= s[i]
    print(ans)


if __name__ == '__main__':
    solve()
