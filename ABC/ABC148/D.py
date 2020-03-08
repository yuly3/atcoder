def solve():
    N, *a = map(int, open(0).read().split())
    
    if 1 not in a:
        print(-1)
        exit()
    
    ans = 0
    target = 1
    i_tmp = -1
    for i, x in enumerate(a):
        if x == target:
            ans += i - i_tmp - 1
            i_tmp = i
            target += 1
    ans += N - i_tmp - 1
    print(ans)


if __name__ == '__main__':
    solve()
