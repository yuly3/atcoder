def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    odd, even = 0, 0
    cnt1 = 0
    for i in range(n):
        if i % 2 == 0:
            odd += a[i]
            if odd + even <= 0:
                tmp = 1 - (odd + even)
                odd += tmp
                cnt1 += tmp
        else:
            even += a[i]
            if 0 <= odd + even:
                tmp = -1 - (odd + even)
                even += tmp
                cnt1 += abs(tmp)
    
    odd, even = 0, 0
    cnt2 = 0
    for i in range(n):
        if i % 2 == 0:
            odd += a[i]
            if 0 <= odd + even:
                tmp = -1 - (odd + even)
                odd += tmp
                cnt2 += abs(tmp)
        else:
            even += a[i]
            if odd + even <= 0:
                tmp = 1 - (odd + even)
                even += tmp
                cnt2 += tmp
    
    ans = min(cnt1, cnt2)
    print(ans)


if __name__ == '__main__':
    solve()
