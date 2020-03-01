def solve():
    n = input()
    ans = ''
    for ni in n:
        if ni == '1':
            ans += '9'
        else:
            ans += '1'
    print(ans)


if __name__ == '__main__':
    solve()
