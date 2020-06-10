import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    
    i = 0
    while i < len(S):
        sub_str = S[i:i + 5]
        if sub_str == 'dream':
            i += 5
            if i < len(S) - 2 and S[i:i + 2] == 'er' and S[i + 2] != 'a' or \
               i == len(S) - 2 and S[i:i + 2] == 'er':
                i += 2
        elif sub_str == 'erase':
            i += 5
            if i < len(S) and S[i] == 'r':
                i += 1
        else:
            print('NO')
            return
    print('YES')


if __name__ == '__main__':
    solve()
