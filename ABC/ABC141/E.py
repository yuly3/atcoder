import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class RollingHash:
    def __init__(self, s: str, base=1007, mod=10 ** 9 + 7):
        self.mod = mod
        length = len(s)
        self.pw = [1] * (length + 1)
        self.h = [0] * (length + 1)
        
        v = 0
        for i in range(length):
            self.h[i + 1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(length):
            self.pw[i + 1] = v = v * base % mod
    
    def query(self, left, right):
        return (self.h[right] - self.h[left] * self.pw[right - left]) % self.mod


def solve():
    N = int(rl())
    S = input()
    
    rh = RollingHash(S)
    
    def check(t):
        dist = dict()
        for i in range(N - t + 1):
            h = rh.query(i, i + t)
            if h in dist:
                if t <= i - dist[h]:
                    return True
            else:
                dist[h] = i
        return False
    
    ok, ng = 0, N // 2 + 1
    while 1 < ng - ok:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    solve()
