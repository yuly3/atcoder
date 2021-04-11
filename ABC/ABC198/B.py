import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = list(rl().rstrip())
    
    cnt = 0
    for ni in N[::-1]:
        if ni != '0':
            break
        cnt += 1
    
    M = ['0'] * cnt + N
    N.reverse()
    N += ['0'] * cnt
    if N == M:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
