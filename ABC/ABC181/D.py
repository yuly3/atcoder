import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    
    if len(S) <= 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
        return
    
    S_counter = Counter(S)
    for num in range(112, 1000, 8):
        if all(val <= S_counter[key] for key, val in Counter(str(num)).items()):
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    solve()
