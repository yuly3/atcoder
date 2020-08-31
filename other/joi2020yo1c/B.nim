import strutils


proc solve() =
    var
        _ = stdin.readLine.parseInt
        S = stdin.readLine
        ans = S.replace("joi", "JOI")
    echo ans


when is_main_module:
    solve()
