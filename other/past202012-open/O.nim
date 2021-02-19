import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
  return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
  num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
  num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
  num0 = floorMod(num0, num1)

var
  graph, higher: seq[seq[int]]
  receive, send, read, ans: seq[int]

proc solve() =
  var N, M, a, b: int
  (N, M) = input().split.map(parseInt)
  graph = newSeqWith(N, newSeq[int]())
  for _ in 0..<M:
    (a, b) = input().split.mapIt(it.parseInt - 1)
    graph[a].add(b)
    graph[b].add(a)
  let Q = input().parseInt
  
  const boundary = 500
  higher = newSeqWith(N, newSeq[int]())
  for i in 0..<N:
    for j in graph[i]:
      if graph[j].len >= boundary:
        higher[i].add(j)
  
  (receive, send, read) = (newSeq[int](N), newSeq[int](N), newSeq[int](N))
  ans = newSeq[int]()
  var T, x: int
  for _ in 0..<Q:
    (T, x) = input().split.map(parseInt)
    dec x
    if T == 1:
      if graph[x].len < boundary:
        for to in graph[x]:
          receive[to] += 1
      else:
        send[x] += 1
    else:
      var cnt = receive[x]
      for i in higher[x]:
        cnt += send[i]
      ans.add(cnt - read[x])
      read[x] = cnt
  echo ans.join("\n")

when is_main_module:
  solve()
