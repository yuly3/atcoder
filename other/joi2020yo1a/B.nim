import strutils


proc solve() =
    var
        _ = stdin.readLine.parseInt
        S = stdin.readLine
    echo S.count('a') + S.count('i') + S.count('u') + S.count('e') + S.count('o')


when is_main_module:
    solve()
