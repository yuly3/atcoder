def solve():
    N, *h = map(int, open(0).read().split())
    
    ans = 0
    for _ in range(10000000):
        l, r = 0, 0
        tmp_min = 1000
        flag = False
        
        for i in range(N):
            if 0 < h[i]:
                l = i
                r = i
                flag = True
                tmp_min = h[i]
                break
        for i in range(l+1, N):
            if h[i] == 0:
                break
            r = i
            tmp_min = min(tmp_min, h[i])
        for i in range(l, r+1):
            h[i] -= tmp_min
        
        if not flag:
            break
        ans += tmp_min
    print(ans)


if __name__ == '__main__':
    solve()
