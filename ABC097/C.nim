import strutils, sets, algorithm


proc solve() =
    var
        s = stdin.readLine
        N = s.len
        K = stdin.readLine.parseInt
        sub_strs = initSet[string]()
        sub_str: string
    
    for i in 0..<N:
        sub_str = $s[i]
        sub_strs.incl(sub_str)
        for j in 1..<K:
            if N <= i + j:
                break
            sub_str &= $s[i + j]
            sub_strs.incl(sub_str)
    
    var set_to_seq = newSeq[string]()
    for str in sub_strs.items:
        set_to_seq.add(str)
    let sub_strs_sorted = set_to_seq.sorted(system.cmp)
    echo sub_strs_sorted[K - 1]


when is_main_module:
    solve()
