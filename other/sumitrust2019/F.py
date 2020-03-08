def solve():
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())
    
    d1 = (A1 - B1) * T1
    d2 = (A2 - B2) * T2
    if d1 < 0:
        d1 *= -1
        d2 *= -1
    
    if d1 + d2 == 0:
        print('infinity')
        exit()
    if 0 < d1 + d2:
        print(0)
        exit()
    
    s = -d1 // (d1 + d2)
    t = d1 % (d1 + d2)
    if t == 0:
        print(s * 2)
    else:
        print(s * 2 + 1)


if __name__ == '__main__':
    solve()
