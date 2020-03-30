import sys
from operator import itemgetter

rl = sys.stdin.readline


def solve():
    N, W = map(int, rl().split())
    w1, w2, w3, w4 = [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]]
    w1.append(list(map(int, rl().split())))
    min_w = w1[1][0]
    for _ in range(N - 1):
        w, v = map(int, rl().split())
        d = w - min_w
        if d == 0:
            w1.append([w, v])
        elif d == 1:
            w2.append([w, v])
        elif d == 2:
            w3.append([w, v])
        else:
            w4.append([w, v])
    w1.sort(key=itemgetter(1), reverse=True)
    w2.sort(key=itemgetter(1), reverse=True)
    w3.sort(key=itemgetter(1), reverse=True)
    w4.sort(key=itemgetter(1), reverse=True)
    
    ans = 0
    for i in range(len(w1)):
        w_tmp1, v_tmp1 = 0, 0
        for j in range(i):
            w_tmp1 += w1[j][0]
            v_tmp1 += w1[j][1]
        for j in range(len(w2)):
            w_tmp2, v_tmp2 = w_tmp1, v_tmp1
            for k in range(j):
                w_tmp2 += w2[k][0]
                v_tmp2 += w2[k][1]
            for k in range(len(w3)):
                w_tmp3, v_tmp3 = w_tmp2, v_tmp2
                for l in range(k):
                    w_tmp3 += w3[l][0]
                    v_tmp3 += w3[l][1]
                for l in range(len(w4)):
                    w_tmp4, v_tmp4 = w_tmp3, v_tmp3
                    for m in range(l):
                        w_tmp4 += w4[m][0]
                        v_tmp4 += w4[m][1]
                    if w_tmp4 <= W:
                        ans = max(ans, v_tmp4)
    print(ans)


if __name__ == '__main__':
    solve()
