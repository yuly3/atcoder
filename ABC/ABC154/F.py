import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class Combination:
    def __init__(self, n: int, mod: int):
        self.mod = mod
        self.fact = [0] * (n + 1)
        self.factinv = [0] * (n + 1)
        self.inv = [0] * (n + 1)
        
        self.fact[0] = self.fact[1] = 1
        self.factinv[0] = self.factinv[1] = 1
        self.inv[1] = 1
        for i in range(2, n + 1):
            self.fact[i] = (self.fact[i - 1] * i) % mod
            self.inv[i] = (-self.inv[mod % i] * (mod // i)) % mod
            self.factinv[i] = (self.factinv[i - 1] * self.inv[i]) % mod
    
    def ncr(self, n: int, r: int):
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] % self.mod * self.factinv[n - r] % self.mod
    
    def nhr(self, n: int, r: int):
        return self.ncr(n + r - 1, r)
    
    def npr(self, n: int, r: int):
        if r < 0 or n < r:
            return 0
        return self.fact[n] * self.factinv[n - r] % self.mod


def solve():
    r1, c1, r2, c2 = map(int, rl().split())
    MOD = 10 ** 9 + 7
    
    com = Combination(r2 + c2 + 100, MOD)
    ans = com.ncr(r2 + c2 + 2, c2 + 1)
    ans = (ans - com.ncr(r1 + c2 + 1, c2 + 1)) % MOD
    ans = (ans - com.ncr(r2 + c1 + 1, c1)) % MOD
    ans = (ans + com.ncr(r1 + c1, c1)) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
