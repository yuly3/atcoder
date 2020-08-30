import math, sets, sequtils, strutils


proc eratosthnes(n: Natural): seq[int] =
    var
        prime = @[2]
        res = newSeq[int](n + 1)
        limit = int(sqrt(float(n)))
        data = newSeq[int]()
    for i in countup(2, n, 2):
        res[i] = 2
    for i in countup(2, n - 1, 2):
        data.add(i + 1)
    
    var p: int
    while true:
        p = data[0]
        if limit <= p:
            for e in data:
                res[e] = e
            return res
        prime.add(p)
        res[p] = p
        for e in data:
            if e mod p == 0:
                res[e] = p
        data.keepItIf(it mod p != 0)


var
    A, prime_fact: seq[int]
    prime_fact_set: HashSet[int]


proc solve() =
    var N = stdin.readLine.parseInt
    A = stdin.readLine.split.map(parseInt)
    
    prime_fact = eratosthnes(10^6)
    prime_fact_set = initHashSet[int]()
    var
        p_flg = true
        prime_fact_ai: HashSet[int]
        num: int
    for ai in A:
        num = ai
        prime_fact_ai = initHashSet[int]()
        while num != 1:
            prime_fact_ai.incl(prime_fact[num])
            num = num div prime_fact[num]
        for p in prime_fact_ai:
            if p in prime_fact_set:
                p_flg = false
                break
            prime_fact_set.incl(p)
        if not p_flg:
            break
    
    if p_flg:
        echo "pairwise coprime"
        return

    var gcd_a = A[0]
    for i in 1..<N:
        gcd_a = gcd(gcd_a, A[i])
    if gcd_a == 1:
        echo "setwise coprime"
        return

    echo "not coprime"


when is_main_module:
    solve()
