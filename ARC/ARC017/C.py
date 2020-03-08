from collections import defaultdict
from itertools import combinations


def solve():
    N, X, *w = map(int, open(0).read().split())
    
    n1 = N // 2
    n2 = N - n1
    first_dict, second_dict = defaultdict(int), defaultdict(int)
    for i in range(n1 + 1):
        for goods in combinations(w[:n1], i):
            weight = sum(goods)
            if weight <= X:
                first_dict[weight] += 1
    for i in range(n2 + 1):
        for goods in combinations(w[n1:], i):
            weight = sum(goods)
            if weight <= X:
                second_dict[weight] += 1
    
    ans = 0
    for key, val in first_dict.items():
        ans += val * second_dict[X - key]
    print(ans)


if __name__ == '__main__':
    solve()
