def solve():
    N = int(input())
    S = input()

    if N % 2 != 0:
        print('No')
        exit()
    s_1 = S[:len(S)//2]
    s_2 = S[len(S)//2:]
    if s_1 == s_2:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()