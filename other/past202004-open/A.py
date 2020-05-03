import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S, T = rl().split()
    
    if S[0] == 'B':
        a = -int(S[1])
    else:
        a = int(S[0]) - 1
    if T[0] == 'B':
        b = -int(T[1])
    else:
        b = int(T[0]) - 1
    
    ans = abs(a - b)
    print(ans)


if __name__ == '__main__':
    solve()
