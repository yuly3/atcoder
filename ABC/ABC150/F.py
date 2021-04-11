import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class RollingHash:
    def __init__(self, s, base=10007, mod=(1 << 61) - 1):
        self.mod = mod
        length = len(s)
        self.pw = [1] * (length + 1)
        self.h = [0] * (length + 1)
        
        v = 0
        for i in range(length):
            self.h[i + 1] = v = (v * base + s[i]) % mod
        v = 1
        for i in range(length):
            self.pw[i + 1] = v = v * base % mod
    
    def slice(self, left, right):
        # [left, right)
        return (self.h[right] - self.h[left] * self.pw[right - left]) % self.mod
    
    def concatenate(self, left0, right0, left1, right1):
        return (self.slice(left0, right0) * self.pw[right1 - left1] + self.slice(left1, right1)) % self.mod


def solve():
    N = int(rl())
    a = list(map(int, rl().split()))
    b = list(map(int, rl().split()))
    
    c, d = [], []
    for i in range(N):
        c.append(a[i] ^ a[i - 1])
        d.append(b[i] ^ b[i - 1])
    c *= 2
    
    rhc = RollingHash(c)
    rhd = RollingHash(d)
    dh = rhd.slice(0, N - 1)
    
    ans = []
    for i in range(N):
        if rhc.slice(i, i + N - 1) == dh:
            ans.append(f'{i} {a[i] ^ b[0]}')
    if ans:
        print('\n'.join(ans))


if __name__ == '__main__':
    solve()
