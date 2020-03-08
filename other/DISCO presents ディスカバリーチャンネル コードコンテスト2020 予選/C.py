def solve():
    H, W, K = map(int, input().split())
    cake = ['' for _ in range(H)]
    for i in range(H):
        cake[i] = input()
    
    ans = [[0 for _ in range(W)] for _ in range(H)]
    index = 0
    while '#' not in cake[index]:
        index += 1
    
    not_strawberry = index
    color = 0
    for line in cake[index:]:
        if '#' not in line:
            ans[index] = ans[index-1]
            index += 1
            continue
        color += 1
        count = 0
        for i in range(W):
            if line[i] == '#':
                count += 1
                if 1 < count:
                    color += 1
            ans[index][i] = color
        index += 1
    
    for i in range(not_strawberry):
        ans[i] = ans[not_strawberry]
    
    for i in range(H):
        print(*ans[i])


if __name__ == '__main__':
    solve()