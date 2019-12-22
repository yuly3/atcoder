def solve():
    N, K = map(int, input().split())
    S = input()
    
    cur = S[0]
    start = [0]
    end = []
    for i, char in enumerate(S):
        if cur == '0' and char == '1':
            start.append(i)
        elif cur == '1' and char == '0':
            end.append(i)
        cur = char
    end.append(len(S))
    
    ans = 0
    for s, e in zip(start, end[K+int(S[0])-1:]):
        ans = max(ans, e - s)
    if ans == 0:
        ans = len(S)
    print(ans)


if __name__ == '__main__':
    solve()
