def solve():
    s = input()
    
    len_s = len(s)
    for i in range(len_s - 1):
        c = s[i:i + 2]
        if c[0] == c[1]:
            print(i + 1, i + 2)
            exit()
    for i in range(len_s - 2):
        c = s[i:i + 3]
        if c[0] == c[-1]:
            print(i + 1, i + 3)
            exit()
    print(-1, -1)


if __name__ == '__main__':
    solve()
