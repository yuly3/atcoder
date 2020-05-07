import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    N = len(S)
    
    def f(idx):
        res = ''
        while idx < N:
            if S[idx] == '(':
                sub_s, idx = f(idx + 1)
                res += sub_s + ''.join(reversed(list(sub_s)))
            elif S[idx] == ')':
                return res, idx + 1
            else:
                res += S[idx]
                idx += 1
        return res
    
    ans = f(0)
    print(ans)


if __name__ == '__main__':
    solve()
