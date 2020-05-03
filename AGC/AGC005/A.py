import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X = rl().rstrip()
    
    ans = len(X)
    cnt_s = 0
    for xi in X:
        if xi == 'S':
            cnt_s += 1
        elif xi == 'T' and cnt_s:
            ans -= 2
            cnt_s -= 1
    print(ans)


if __name__ == '__main__':
    solve()
