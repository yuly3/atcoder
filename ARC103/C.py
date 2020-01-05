from collections import defaultdict


def solve():
    n, *v = map(int, open(0).read().split())
    
    dict1 = defaultdict(int)
    for i in range(0, n, 2):
        dict1[v[i]] += 1
    
    dict2 = defaultdict(int)
    for i in range(1, n, 2):
        dict2[v[i]] += 1
    
    sorted1 = sorted(dict1.items(), key=lambda x: x[1], reverse=True) + [(-1, 0)]
    sorted2 = sorted(dict2.items(), key=lambda x: x[1], reverse=True) + [(-2, 0)]
    
    ans = n
    for i in range(2):
        for j in range(2):
            if sorted1[i][0] == sorted2[j][0]:
                continue
            ans = min(ans, n - sorted1[i][1] - sorted2[j][1])
    print(ans)


if __name__ == '__main__':
    solve()
