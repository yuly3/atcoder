from bisect import bisect_left
from collections import defaultdict


def solve():
    s = input()
    t = input()

    n = len(s)
    index = defaultdict(list)
    for i, char in enumerate(s):
        index[char] += [i]
    
    cur, orbit = -1, 0
    for char in t:
        target = index[char]
        if not target:
            print(-1)
            exit()
        
        i = bisect_left(target, cur + 1)
        if i < len(target):
            cur = target[i]
        else:
            cur = target[0]
            orbit += 1
    print(n*orbit + cur + 1)


if __name__ == '__main__':
    solve()