import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    a, b = [], []
    for _ in range(N):
        si = rl().rstrip()
        if si[0] == '!':
            b.append(si)
        else:
            a.append(si)
    
    d = {ai for ai in a}
    for bi in b:
        if bi[1:] in d:
            print(bi[1:])
            return
    print('satisfiable')


if __name__ == '__main__':
    solve()
