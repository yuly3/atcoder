import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


def solve():
    _ = int(rl())
    X = list(map(int, rl().rstrip()))[::-1]
    
    ones = X.count(1)
    upmod = X[0] % (ones + 1)
    c = 1
    for xi in X[1:]:
        c = c * 2 % (ones + 1)
        upmod = (upmod + c * xi) % (ones + 1)
    botmod = 0
    if ones - 1 != 0:
        botmod = X[0] % (ones - 1)
        c = 1
        for xi in X[1:]:
            c = c * 2 % (ones - 1)
            botmod = (botmod + c * xi) % (ones - 1)
    
    ans = []
    for i, xi in enumerate(X):
        if ones == 1 and xi == 1:
            ans.append(0)
            continue
        if xi == 0:
            xmod = (upmod + pow(2, i, ones + 1)) % (ones + 1)
        else:
            xmod = (botmod - pow(2, i, ones - 1)) % (ones - 1)
        cnt = 1
        while xmod != 0:
            xmod = xmod % popcount(xmod)
            cnt += 1
        ans.append(cnt)
    print(*ans[::-1], sep='\n')


if __name__ == '__main__':
    solve()
