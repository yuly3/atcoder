def solve():
    *antenna, k = map(int, open(0).read().split())
    
    if k < antenna[4] - antenna[0]:
        print(':(')
    else:
        print('Yay!')


if __name__ == '__main__':
    solve()
