from collections import defaultdict
from itertools import accumulate


def solve():
    N, K, *A = map(int, open(0).read().split())
    
    Acumsum = [0] + list(accumulate(A))
    si = [(Acumsum[i] - i) % K for i in range(N + 1)]
    counter = defaultdict(int)
    
    ans = 0
    for j in range(N):
        counter[si[j]] += 1
        if 0 <= j - K + 1:
            counter[si[j - K + 1]] -= 1
        ans += counter[si[j + 1]]
    print(ans)


if __name__ == '__main__':
    solve()
