def solve():
    S = list(input())
    ans = S[:]
    T = input()
    Sn = len(S)
    Tn = len(T)
    
    restorable = False
    for i in range(Sn - Tn, -1, -1):
        flag = True
        if S[i] == T[0] or S[i] == '?':
            for j in range(Tn):
                if S[i+j] != T[j] and S[i+j] != '?':
                    flag = False
                    break
            if flag:
                restorable = True
                for j in range(Tn):
                    ans[i+j] = T[j]
                break
    
    if not restorable:
        print('UNRESTORABLE')
    else:
        for i in range(Sn):
            if ans[i] == '?':
                ans[i] = 'a'
        print(''.join(ans))


if __name__ == '__main__':
    solve()
