def solve():
    N, K, *V = map(int, open(0).read().split())
    
    AB_MAX = min(N, K)
    val = []
    for left in range(AB_MAX+1):
        for right in range(AB_MAX-left+1):
            get = V[:left] + V[-right:] if right != 0 else V[:left]
            get.sort()
            i = K - left - right
            if get:
                while get[0] < 0 and 0 < i:
                    get = get[1:]
                    i -= 1
                    if not get:
                        break
            val.append(sum(get))
    print(max(val))


if __name__ == '__main__':
    solve()
