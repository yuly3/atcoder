def solve():
    S = ''.join(list(map(str, input().split())))
    if S.find('1') == -1 or S.find('9') == -1 or S.find('7') == -1 or S.find('4') == -1:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    solve()
