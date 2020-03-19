def solve():
    s = sorted(list(input()))
    t = sorted(list(input()), reverse=True)
    if ''.join(s) < ''.join(t):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
