import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    K = int(rl())
    S = rl().rstrip()
    T = rl().rstrip()
    
    counterS = {n: 0 for n in range(1, 10)}
    counterT = {n: 0 for n in range(1, 10)}
    for si in S[:4]:
        counterS[int(si)] += 1
    for ti in T[:4]:
        counterT[int(ti)] += 1
    
    num = 0
    for a in range(1, 10):
        c = K - counterS[a] - counterT[a]
        if c <= 0:
            continue
        counterS[a] += 1
        p = sum(k * 10 ** v for k, v in counterS.items())
        for b in range(1, 10):
            d = K - counterS[b] - counterT[b]
            if d <= 0:
                continue
            counterT[b] += 1
            q = sum(k * 10 ** v for k, v in counterT.items())
            if q < p:
                num += c * d
            counterT[b] -= 1
        counterS[a] -= 1
    den = 9 * K - 8
    den = den * (den - 1)
    print(num / den)


if __name__ == '__main__':
    solve()
