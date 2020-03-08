def solve():
    S = input()
    if len(S) % 2 == 1 or len(S) == 0:
        print('No')
        exit()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] != 'h':
                print('No')
                exit()
        else:
            if S[i] != 'i':
                print('No')
                exit()
    print('Yes')


if __name__ == '__main__':
    solve()
