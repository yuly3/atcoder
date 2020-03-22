def solve():
    N = int(input())
    a = list(map(int, input().split()))
    
    m2, m4 = 0, 0
    for ai in a:
        if ai % 2 == 0:
            m2 += 1
            if ai % 4 == 0:
                m4 += 1
    
    if N % 2 == 0:
        if N - m2 <= m4:
            print('Yes')
        else:
            print('No')
    else:
        if N - m2 - 1 <= m4:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    solve()
