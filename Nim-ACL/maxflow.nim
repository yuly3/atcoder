import algorithm

when not declared ATCODER_INTERNAL_QUEUE_HPP:
  const ATCODER_INTERNAL_QUEUE_HPP* = 1

  type simpleQueue[T] = object
    payload: seq[T]
    pos: int
  
  proc initSimpleQueue*[T](): auto = simpleQueue[T](payload: newSeq[T](), pos:0)
  proc len*[T](self: simpleQueue[T]): int = self.payload.len - self.pos
  proc empty*[T](self: simpleQueue[T]): bool = self.pos == self.payload.len
  proc push*[T](self: var simpleQueue[T], t: T) = self.payload.add(t)
  proc front*[T](self: simpleQueue[T]): T = self.payload[self.pos]
  proc clear*[T](self: var simpleQueue[T]) =
    self.payload.setLen(0)
    self.pos = 0
  proc pop*[T](self: var simpleQueue[T]) = self.pos.inc

when not declared ATCODER_MAXFLOW_HPP:
  const ATCODER_MAXFLOW_HPP* = 1

  type edge[Cap] = object
    dst, rev: int
    cap: Cap
  
  type MFGraph*[Cap] = object
    n: int
    pos: seq[(int, int)]
    g: seq[seq[edge[Cap]]]
  
  proc initMFGraph*[Cap](n: int): auto = MFGraph[Cap](n: n, g: newSeq[seq[edge[Cap]]](n))

  proc addEdge*[Cap](self: var MFGraph[Cap], src, dst: int, cap: Cap): int {.discardable.} =
    let m = self.pos.len
    self.pos.add((src, self.g[src].len))
    var
      srcId = self.g[src].len
      dstId = self.g[dst].len
    if src == dst: dstId.inc
    self.g[src].add(edge[Cap](dst: dst, rev: dstId, cap: cap))
    self.g[dst].add(edge[Cap](dst: src, rev: srcId, cap: 0))
    return m

  type EdgeInfo*[Cap] = object
    src*, dst*: int
    cap*, flow*: Cap
  
  proc getEdge*[Cap](self: MFGraph[Cap], i: int): EdgeInfo[Cap] =
    let
      m = self.pos.len
      e = self.g[self.pos[i][0]][self.pos[i][1]]
      re = self.g[e.dst][e.rev]
    return EdgeInfo[Cap](src: self.pos[i][0], dst: e.dst, cap: e.cap + re.cap, flow: re.cap)

  proc edges*[Cap](self: MFGraph[Cap]): seq[EdgeInfo[Cap]] =
    let m = self.pos.len
    result = newSeqOfCap[EdgeInfo[Cap]](m)
    for i in 0..<m:
      result.add(self.getEdge(i))
  
  proc changeEdge*[Cap](self: var MFGraph[Cap], i: int, newCap, newFlow: Cap) =
    var
      e = self.g[self.pos[i][0]][self.pos[i][1]].addr
      re = self.g[e[].dst][e[].rev].addr
    e[].cap = newCap - newFlow
    re[].cap = newFlow
  
  proc flow*[Cap](self: var MFGraph[Cap], s, t: int, flowLimit: Cap): Cap =
    var
      level, iter = newSeq[int](self.n)
      que = initSimpleQueue[int]()
    
    proc bfs(self: MFGraph[Cap]) =
      level.fill(-1)
      level[s] = 0
      que.clear()
      que.push(s)
      while not que.empty():
        let v = que.front()
        que.pop
        for e in self.g[v]:
          if e.cap == 0 or level[e.dst] >= 0: continue
          level[e.dst] = level[v] + 1
          if e.dst == t: return
          que.push(e.dst)
    
    proc dfs(self: var MFGraph[Cap], v: int, up: Cap): Cap =
      if v == s: return up
      result = Cap(0)
      let levelV = level[v]
      var i = iter[v].addr
      while i[] < self.g[v].len:
        let e = self.g[v][i[]].addr
        if levelV <= level[e[].dst] or self.g[e[].dst][e[].rev].cap == 0:
          i[].inc
          continue
        let d = self.dfs(e.dst, min(up - result, self.g[e[].dst][e[].rev].cap))
        if d <= 0:
          i[].inc
          continue
        self.g[v][i[]].cap += d
        self.g[e[].dst][e[].rev].cap -= d
        result += d
        if result == up: break
        i[].inc
    
    var flow = Cap(0)
    while flow < flowLimit:
      self.bfs()
      if level[t] == -1: break
      iter.fill(0)
      while flow < flowLimit:
        let f = self.dfs(t, flowLimit - flow)
        if f == Cap(0): break
        flow += f
    return flow

  proc flow*[Cap](self: var MFGraph[Cap], s, t: int): auto = self.flow(s, t, Cap.high)

  proc minCut*[Cap](self: MFGraph[Cap], s: int): seq[bool] =
    var
      visited = newSeq[bool](self.n)
      que = initSimpleQueue[int]()
    que.push(s)
    while not que.empty():
      let p = que.front()
      que.pop()
      visited[p] = true
      for e in self.g[p]:
        if e.cap != Cap(0) and not visited[e.dst]:
          visited[e.dst] = true
          que.push(e.dst)
    return visited
