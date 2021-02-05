import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def inv_gcd(a, b):
    a %= b
    if a == 0:
        return b, 0
    
    s, t = b, a
    m0, m1 = 0, 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t = t, s
        m0, m1 = m1, m0
    
    if m0 < 0:
        m0 += b // s
    return s, m0


def crt(r, m):
    # assert len(r) == len(m)
    n = len(r)
    r0, m0 = 0, 1
    for i in range(n):
        # assert 1 <= m[i]
        r1, m1 = r[i] % m[i], m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return [0, 0]
            continue
        
        g, im = inv_gcd(m0, m1)
        if (r1 - r0) % g:
            return [0, 0]
        
        u1 = m0 * m1 // g
        r0 += (r1 - r0) // g * m0 * im % u1
        m0 = u1
    return r0, m0


def solve():
    N, S, K = map(int, rl().split())
    
    y, m = crt((0, N - S), (K, N))
    if m == 0:
        return -1
    else:
        return y // K


if __name__ == '__main__':
    T = int(rl())
    ans = []
    for _ in range(T):
        ans.append(solve())
    print('\n'.join(map(str, ans)))
