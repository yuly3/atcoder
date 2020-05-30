import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    T = rl().rstrip()
    
    ans = []
    for ti in T:
        if ti == '?':
            ans.append('D')
        else:
            ans.append(ti)
    print(''.join(ans))


if __name__ == '__main__':
    solve()
