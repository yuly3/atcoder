from collections import defaultdict
from itertools import combinations


def solve():
    N = int(input())
    S = input()
    s1, s2 = S[:N], S[N:][::-1]
    
    l_dict = defaultdict(int)
    r_dict = defaultdict(int)
    for i in range(N+1):
        for red_idx in combinations(range(N), i):
            red, blue = '', ''
            for j in range(N):
                if j in red_idx:
                    red += s1[j]
                else:
                    blue += s1[j]
            l_dict[red+' '+blue] += 1
    for i in range(N+1):
        for red_idx in combinations(range(N), i):
            red, blue = '', ''
            for j in range(N):
                if j in red_idx:
                    red += s2[j]
                else:
                    blue += s2[j]
            r_dict[red+' '+blue] += 1
    
    ans = sum(l_dict[key] * r_dict[key] for key in l_dict)
    print(ans)


if __name__ == '__main__':
    solve()
