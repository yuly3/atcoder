def solve():
    N = int(input())
    s = ['' for _ in range(N)]
    t = [0] * N
    for i in range(N):
        si, ti = map(str, input().split())
        s[i], t[i] = si, int(ti)
    X = input()
    
    idx = s.index(X) + 1
    ans = sum(t[idx:])
    print(ans)


if __name__ == '__main__':
    solve()
