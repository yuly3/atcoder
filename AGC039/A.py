def counter(s):
    res, cnt = 0, 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            res += cnt // 2
            cnt = 1
    res += cnt // 2
    return res


def solve():
    S = list(input())
    K = int(input())
    
    N = len(S)
    if len(set(S)) == 1:
        print(N * K // 2)
        exit()
    
    a = counter(S)
    b = counter(S + S)
    print(a + (K - 1) * (b - a))


if __name__ == '__main__':
    solve()
