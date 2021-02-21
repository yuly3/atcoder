import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
  return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
  num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
  num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
  num0 = floorMod(num0, num1)

proc solve() =
  let
    ABC = input().split
    A = parseInt(ABC[0][ABC[0].len - 1..ABC[0].len - 1])
    B = parseInt(ABC[1])
    C = parseInt(ABC[2])

  var pa = newSeq[char](5)
  for i in 1..4:
    pa[i] = ($(A^i))[^1]
  
  if B mod 4 == 2 and C mod 2 == 1:
    if C == 1:
      echo pa[2]
    else:
      echo pa[4]
    return
  
  var pbmc = newSeq[int](3)
  for i in 1..2:
    pbmc[i] = B^i mod 4
  
  var m = if C mod 2 == 1: pbmc[1] else: pbmc[2]
  if m == 0:
    m = 4
  echo pa[m]

when is_main_module:
  solve()
