from collections import defaultdict


def solve():
    N, M = map(int, input().split())
    ac_dict = defaultdict(int)
    wa_dict = defaultdict(int)
    ac_p, wa_p = set(), set()
    for _ in range(M):
        p, s = map(str, input().split())
        p = int(p)
        if s == 'AC':
            ac_p.add(p)
            ac_dict[p] = 1
        else:
            if ac_dict[p] != 1:
                wa_p.add(p)
                wa_dict[p] += 1
    
    wa = 0
    for pi in ac_p:
        if pi in wa_p:
            wa += wa_dict[pi]
    
    print(sum(ac_dict.values()), wa)


if __name__ == '__main__':
    solve()
