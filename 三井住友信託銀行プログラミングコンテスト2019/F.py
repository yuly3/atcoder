def solve():
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())
    p = (A1 - B1) * T1
    q = (A2 - B2) * T2
    if p < 0:
        p *= -1
        q *= -1

    if p + q > 0:
        print(0)
    elif p + q == 0:
        print('infinity')
    else:
        s = -p // (p + q)
        t = -p % (p + q)
        if t != 0:
            print(s*2+1)
        else:
            print(s*2)


if __name__ == '__main__':
    solve()