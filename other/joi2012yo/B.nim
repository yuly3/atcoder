import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string = stdin.readLine
proc inputs*(): seq[string] = stdin.readLine.split
proc inputInt*(): int = stdin.readLine.parseInt
proc inputInts*(): seq[int] = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) = num0 = floorMod(num0, num1)

proc solve() =
  let N = inputInt()
  var
    points = newSeq[int](N)
    a, b, c, d: int
  for _ in 0..<N*(N - 1) div 2:
    (a, b, c, d) = inputInts()
    dec a; dec b
    if c < d:
      points[b] += 3
    elif c > d:
      points[a] += 3
    else:
      inc points[a]
      inc points[b]
  
  var ls = newSeq[(int, int)]()
  for i, pi in points:
    ls.add((pi, i))
  ls.sort(order=Descending)

  var ans = newSeq[int](N)
  for j, (p, i) in ls:
    if j != 0 and ls[j - 1][0] == p:
      ans[i] = ans[ls[j - 1][1]]
    else:
      ans[i] = j + 1
  echo ans.join("\n")

when is_main_module:
  solve()
