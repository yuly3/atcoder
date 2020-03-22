import sys
rl = sys.stdin.readline


def solve():
    S = input()
    reverse_S = list(reversed(S))
    for i in range(len(S)):
        if S[i] != reverse_S[i]:
            print('No')
            exit()
    s2 = S[:(len(S) - 1) // 2]
    reverse_s2 = list(reversed(s2))
    for i in range(len(s2)):
        if s2[i] != reverse_s2[i]:
            print('No')
            exit()
    s3 = S[(len(S) + 3) // 2 - 1:]
    reverse_s3 = list(reversed(s3))
    for i in range(len(s3)):
        if s3[i] != reverse_s3[i]:
            print('No')
            exit()
    print('Yes')


if __name__ == '__main__':
    solve()
