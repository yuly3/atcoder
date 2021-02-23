import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string = stdin.readLine
proc inputs*(): seq[string] = stdin.readLine.split
proc inputInt*(): int = stdin.readLine.parseInt
proc inputInts*(): seq[int] = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) = num0 = floorMod(num0, num1)

proc solve() =
  let S = input()

  var
    ans = 0
    cur = 0
    counter = [0, 0, 0]
  while cur < S.len:
    if S[cur] == 'J':
      if cur != 0 and S[cur - 1] != 'J':
        counter[0] = 0
      counter[1] = 0; counter[2] = 0
      inc counter[0]
    elif S[cur] == 'O':
      if cur != 0 and S[cur - 1] == 'I':
        counter.fill(0)
      else:
        inc counter[1]
        if counter[0] < counter[1]:
          counter.fill(0)
    else:
      if cur != 0 and S[cur - 1] == 'J':
        counter.fill(0)
      else:
        inc counter[2]
    inc cur
    if counter[1] == counter[2]:
      ans.chmax(counter[1])
  echo ans

when is_main_module:
  solve()
