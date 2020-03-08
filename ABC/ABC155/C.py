from collections import defaultdict


def solve():
    N = int(input())
    S_dict = defaultdict(int)
    S = ['' for _ in range(N)]
    for i in range(N):
        si = input()
        S[i] = si
        S_dict[si] += 1
    
    max_v = max(S_dict.values())
    tmp = [s for s in S if S_dict[s] == max_v]
    tmp.sort()
    p_ans = ''
    for ans in tmp:
        if p_ans != ans:
            print(ans)
            p_ans = ans


if __name__ == '__main__':
    solve()
