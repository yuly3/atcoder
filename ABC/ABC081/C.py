from collections import defaultdict


def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    counter = defaultdict(int)
    for ai in A:
        counter[ai] += 1
    
    sorted_c = sorted(counter.values())
    ans = 0
    for i in range(len(counter) - K):
        ans += sorted_c[i]
    print(ans)


if __name__ == '__main__':
    solve()
