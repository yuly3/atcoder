def solve():
    H = int(input())
    
    ans = 0
    tmp_h, n = H, 1
    while 1 < tmp_h:
        ans += n
        n *= 2
        tmp_h = tmp_h // 2
    ans += n
    print(ans)


if __name__ == '__main__':
    solve()
