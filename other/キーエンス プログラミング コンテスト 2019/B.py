def solve():
    S = input()
    N = len(S)
    for i in range(N-(N-8)):
        if S[:i] + S[i+(N-7):] == 'keyence':
            print('YES')
            exit()
    print('NO')


if __name__ == '__main__':
    solve()
