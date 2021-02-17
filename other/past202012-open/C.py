import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    if N == 0:
        print(0)
        return
    
    ans = ''
    t = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for d in range(2, -1, -1):
        i = N // 36 ** d
        if i or ans != '':
            ans += t[i]
            N -= 36 ** d * i
    print(ans)


if __name__ == '__main__':
    solve()
