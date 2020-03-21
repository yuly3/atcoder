from collections import defaultdict


def solve():
    _ = int(input())
    a = list(map(int, input().split()))
    
    counter = defaultdict(int)
    for ai in a:
        counter[ai] += 1
        counter[ai + 1] += 1
        counter[ai - 1] += 1
    
    ans = 0
    for val in counter.values():
        ans = max(ans, val)
    print(ans)


if __name__ == '__main__':
    solve()
