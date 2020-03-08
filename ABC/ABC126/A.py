def solve():
    N, K = map(int, input().split())
    s = input()
    s_lower = s.lower()
    s = list(s)
    s[K-1] = s_lower[K-1]
    print(''.join(s))

if __name__ == '__main__':
    solve()