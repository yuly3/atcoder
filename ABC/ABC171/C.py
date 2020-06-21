import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    ans = []
    while N:
        mod = (N - 1) % 26
        ans.append(chr(ord('a') + mod))
        N -= 1
        N //= 26
    print(''.join(reversed(ans)))


if __name__ == '__main__':
    solve()
