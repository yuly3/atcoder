from collections import Counter


def solve():
    N, K = map(int,  input().split())
    S = input()
    
    ans = []
    s_sorted = sorted(S)
    different = 0
    for i in range(N):
        counter = Counter(S[:i+1]) - Counter(ans)
        counts = sum(counter.values())
        for j, char in enumerate(s_sorted):
            d1, d2 = different, counts
            if char != S[i]:
                d1 += 1
            if 0 < counter[char]:
                d2 -= 1
            if d1 + d2 <= K:
                ans.append(char)
                different = d1
                del s_sorted[j]
                break
    print(''.join(ans))


if __name__ == '__main__':
    solve()
