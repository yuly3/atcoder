import strutils, sequtils, math


proc solve() =
    var
        N, M: int
        ac_p, wa_p: array[10^5 + 1, int]
        p: int
        S: string
    
    (N, M) = stdin.readLine.split.map(parseInt)
    for _ in 1..M:
        let pS = stdin.readLine.split
        p = pS[0].parseInt
        S = pS[1]
        if S == "AC":
            ac_p[p] = 1
        else:
            if ac_p[p] == 0:
                inc wa_p[p]
    
    var ans_ac, ans_p = 0
    for i in 1..N:
        if ac_p[i] != 0:
            inc ans_ac
            ans_p += wa_p[i]
    echo ans_ac, ' ', ans_p


when is_main_module:
    solve()
