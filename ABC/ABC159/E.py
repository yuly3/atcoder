import sys
rl = sys.stdin.readline


def solve():
    H, W, K = map(int, rl().split())
    S = [[] for _ in range(H)]
    for i in range(H):
        S[i] = list(map(int, list(input())))
    
    ans = 10 ** 6
    for s in range(1 << (H - 1)):
        pop_cnt = 0
        for i in range(H - 1):
            if s >> i & 1:
                pop_cnt += 1
        
        tmp = pop_cnt
        b = [0] * (tmp + 1)
        flg = True
        for i in range(W):
            j = 0
            for k in range(H):
                if S[k][i]:
                    b[j] += 1
                if s >> k & 1:
                    j += 1
            
            flg = True
            for bi in b:
                if K < bi:
                    flg = False
            
            if not flg:
                tmp += 1
                b = [0] * (pop_cnt + 1)
                j = 0
                for k in range(H):
                    if S[k][i]:
                        b[j] += 1
                    if s >> k & 1:
                        j += 1
                
                flg = True
                for bi in b:
                    if K < bi:
                        flg = False
        
        if flg:
            ans = min(ans, tmp)
    print(ans)


if __name__ == '__main__':
    solve()
