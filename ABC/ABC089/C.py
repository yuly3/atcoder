def solve():
    N = int(input())
    counter = [0] * 5
    for _ in range(N):
        S = input()
        if S[0] == 'M':
            counter[0] += 1
        elif S[0] == 'A':
            counter[1] += 1
        elif S[0] == 'R':
            counter[2] += 1
        elif S[0] == 'C':
            counter[3] += 1
        elif S[0] == 'H':
            counter[4] += 1
    
    ans = 0
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                ans += counter[i] * counter[j] * counter[k]
    print(ans)


if __name__ == '__main__':
    solve()
