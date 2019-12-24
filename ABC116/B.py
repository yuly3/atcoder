def solve():
    s = int(input())
    
    ans, an = 1, s
    while 1:
        if an == 4 or an == 2 or an == 1:
            ans += 3
            break
        if an % 2 == 0:
            an //= 2
        else:
            an = 3 * an + 1
        ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
