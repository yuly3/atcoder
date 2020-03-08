def solve():
    s = input()
    s_set = set(s)
    s_set_l = list(s_set)
    if len(s_set) == 2:
        if s.count(s_set_l[0]) == 2 and s.count(s_set_l[1]) == 2:
            print('Yes')
            exit()
    print('No')


if __name__ == '__main__':
    solve()