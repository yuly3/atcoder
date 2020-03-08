def solve():
    N, *A = map(int, open(0).read().split())
    B = [a for a in A if a % 2 == 0]
    
    for b in B:
        if b % 3 != 0 and b % 5 != 0:
            print('DENIED')
            exit()
    print('APPROVED')


if __name__ == '__main__':
    solve()
