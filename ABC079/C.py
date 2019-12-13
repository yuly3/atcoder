S = input()
ans = ''


def calc(i, s, num):
    if i == 3:
        if num == 7:
            global ans
            ans = s + '=7'
    else:
        calc(i+1, s+'+'+S[i+1], num+int(S[i+1]))
        calc(i+1, s+'-'+S[i+1], num-int(S[i+1]))


def solve():
    calc(0, S[0], int(S[0]))
    print(ans)


if __name__ == '__main__':
    solve()