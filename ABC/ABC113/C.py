from collections import defaultdict


def solve():
    N, M = map(int, input().split())
    p_dict = defaultdict(list)
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        p, y = map(int, input().split())
        p_dict[p].append(y)
        P[i], Y[i] = p, y
    
    recog_num = defaultdict(int)
    for i in range(1, N+1):
        birth = sorted(p_dict[i])
        for index, y in enumerate(birth):
            recog_num[y] = index + 1
    
    for i in range(M):
        print('{:06d}'.format(P[i]) + '{:06d}'.format(recog_num[Y[i]]))


if __name__ == '__main__':
    solve()
