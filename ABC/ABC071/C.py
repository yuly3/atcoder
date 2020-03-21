from collections import defaultdict


def solve():
    _ = int(input())
    A = list(map(int, input().split()))
    
    counter = defaultdict(int)
    for ai in A:
        counter[ai] += 1
    
    first, second = 0, 0
    for key, val in counter.items():
        if 4 <= val:
            if first < key:
                first, second = key, key
            elif second < key:
                second = key
        elif 2 <= val:
            if first < key:
                first, second = key, first
            elif second < key:
                second = key
    ans = first * second
    print(ans)


if __name__ == '__main__':
    solve()
