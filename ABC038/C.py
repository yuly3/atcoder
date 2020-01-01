def solve():
    N, *a = map(int, open(0).read().split())
    
    ans, j = 0, 0
    for i in range(N):
        while j < N:
            if i == j:
                j += 1
            elif a[j] <= a[j-1]:
                ans += j - i
                break
            else:
                j += 1
        if j == N:
            ans += j - i
    print(ans)


if __name__ == '__main__':
    solve()
