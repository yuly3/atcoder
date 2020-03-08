def solve():
    S = input()
    T = input()
    
    s_counter = sorted([S.count(chr(i)) for i in range(ord('a'), ord('z') + 1)])
    t_counter = sorted([T.count(chr(i)) for i in range(ord('a'), ord('z') + 1)])
    if s_counter == t_counter:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
