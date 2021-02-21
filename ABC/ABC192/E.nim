import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string = stdin.readLine
proc inputInt*(): int = stdin.readLine.parseInt()
proc inputInts*(): seq[int] = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) = num0 = floorMod(num0, num1)

var
  graph: seq[seq[(int, int)]]
  T, K, dist: seq[int]
  que: HeapQueue[(int, int)]

proc solve() =
  var N, M, X, Y, a, b, t, k: int
  (N, M, X, Y) = inputInts()
  dec X; dec Y
  graph = newSeqWith(N, newSeq[(int, int)]())
  (T, K) = (newSeq[int](M), newSeq[int](M))
  for i in 0..<M:
    (a, b, t, k) = inputInts()
    dec a; dec b
    graph[a].add((b, i))
    graph[b].add((a, i))
    (T[i], K[i]) = (t, k)
  
  dist = newSeqWith(N, 10^18)
  dist[X] = 0
  que = initHeapQueue[(int, int)]()
  que.push((0, X))
  var time, cur, wait: int
  while que.len != 0:
    (time, cur) = que.pop()
    if cur == Y:
      echo time
      return
    if dist[cur] < time:
      continue
    for (to, idx) in graph[cur]:
      wait = K[idx] * (time div K[idx] + 1) - time
      if wait == K[idx]:
        wait = 0
      let next_t = time + wait + T[idx]
      if dist[to] <= next_t:
        continue
      dist[to] = next_t
      que.push((next_t, to))
  echo -1

when is_main_module:
  solve()
