import strutils, sequtils, math, algorithm


proc modpow(a, b, MOD: int): int =
    var
        res = 1
        (a, b) = (a, b)
    while 0 < b:
        if (b and 1) == 1:
            res = res * a mod MOD
        a = a * a mod MOD
        b = b shr 1
    return res


proc solve() =
    var
        N = stdin.readLine.parseInt
        C = stdin.readLine.split.map(parseInt)
    const MOD = 10^9 + 7
    
    C.sort(system.cmp, order=Descending)
    var ans = 0
    for i in 0..<N:
        ans = (ans + C[i] * (i + 2)) mod MOD
    ans = ans * modpow(4, N - 1, MOD) mod MOD
    echo ans


when is_main_module:
    solve()
