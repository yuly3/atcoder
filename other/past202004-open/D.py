import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def f(s):
    n = len(s)
    res = []
    for bit in range(1 << n):
        t = ''
        for k in range(n):
            t += s[k] if bit >> k & 1 else '.'
        res.append(t)
    return res


def solve():
    S = rl().rstrip()
    
    s_set = set()
    for i in range(len(S)):
        for j in range(1, 4):
            sub_s = f(S[i:i + j])
            for si in sub_s:
                s_set.add(si)
    print(len(s_set))


if __name__ == '__main__':
    solve()
