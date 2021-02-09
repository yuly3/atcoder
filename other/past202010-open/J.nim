import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
  return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
  num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
  num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
  num0 = num0 mod num1

var
  graph: seq[seq[(int, int)]]
  ord_S, min_dist: seq[int]
  heapque: HeapQueue[(int, int)]

proc solve() =
  var N, M, xab, xac, xbc: int
  (N, M) = input().split.map(parseInt)
  (xab, xac, xbc) = input().split.map(parseInt)
  let
    X = [[0, xab, xac], [xab, 0, xbc], [xac, xbc, 0]]
    S = input()
  graph = newSeqWith(N + 6, newSeq[(int, int)]())
  var a, b, c: int
  for _ in 0..<M:
    (a, b, c) = input().split.map(parseInt)
    dec a; dec b
    graph[a].add((b, c))
    graph[b].add((a, c))
  
  ord_S = S.mapIt(ord(it) - ord('A'))
  for i, si in ord_S:
    graph[i].add((N + si, 0))
    graph[N + 3 + si].add((i, 0))
  for i in 0..<3:
    for j in 0..<3:
      if i == j:
        continue
      graph[N + i].add((N + 3 + j, X[i][j]))
  
  min_dist = newSeqWith(N + 6, 10^18)
  heapque = initHeapQueue[(int, int)]()
  heapque.push((0, 0))
  var t, cur, nt: int
  while heapque.len != 0:
    (t, cur) = heapque.pop()
    if cur == N - 1:
      echo t
      break
    if min_dist[cur] < t:
      continue
    for (to, cost) in graph[cur]:
      nt = t + cost
      if min_dist[to] <= nt:
        continue
      min_dist[to] = nt
      heapque.push((nt, to))

when is_main_module:
  solve()
