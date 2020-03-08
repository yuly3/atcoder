def solve():
    a1, a2, a3 = map(int, input().split())
    if a1+a2+a3 >= 22:
        print('bust')
    else:
        print('win')


if __name__ == '__main__':
    solve()