import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    s = rl().rstrip()
    t = s.replace('BC', 'D')
    
    cnt = 0
    i = 0
    ans = 0
    while i < len(t):
        if t[i] == 'B' or t[i] == 'C':
            cnt = 0
        elif t[i] == 'A':
            cnt += 1
        else:
            ans += cnt
        i += 1
    print(ans)


if __name__ == '__main__':
    solve()
