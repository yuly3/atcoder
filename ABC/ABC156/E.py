class COM:
    def __init__(self, n: int, mod: int):
        self.n = n
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
    
    def get_cmb(self, n: int, k: int):
        if (k < 0) or (n < k):
            return 0
        k = min(k, n - k)
        return self.fact[n] * self.factinv[k] % self.mod * self.factinv[n - k] % self.mod


def solve():
    n, k = map(int, input().split())
    MOD = 10 ** 9 + 7
    
    com = COM(n, MOD)
    ans = 0
    for i in range(min(n, k + 1)):
        ans += com.get_cmb(n, i) * com.get_cmb(n - 1, i)
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    solve()
