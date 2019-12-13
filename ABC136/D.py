def solve():
    s = input()
    ans_l = [1] * len(s)

    for i in range(len(s)-2):
        if s[i] == 'R' and s[i+1] == 'R':
            ans_l[i+2] += ans_l[i]
            ans_l[i] = 0

    for i in range(len(s)-1, 1, -1):
        if s[i] == 'L' and s[i-1] == 'L':
            ans_l[i-2] += ans_l[i]
            ans_l[i] = 0

    print(' '.join(map(str, ans_l)))


if __name__ == '__main__':
    solve()