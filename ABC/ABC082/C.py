from collections import defaultdict


def solve():
    _ = int(input())
    a = list(map(int, input().split()))
    
    b_dict = defaultdict(int)
    for ai in a:
        b_dict[ai] += 1
    
    ans = 0
    for key, val in b_dict.items():
        if val < key:
            ans += val
        elif key < val:
            ans += val - key
    print(ans)


if __name__ == '__main__':
    solve()
