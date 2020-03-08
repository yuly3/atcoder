def solve():
    N, *A = map(int, open(0).read().split())
    
    A_set = set(A)
    if len(A_set) == N:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    solve()
