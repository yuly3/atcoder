import heapqueue, sequtils

when not declared ATCODER_MINCOSTFLOW_HPP:
  const ATCODER_MINCOSTFLOW_HPP* = 1

  type Edge*[Cap, Cost] = object
    dst, rev: int
    cap: Cap
    cost: Cost
  
  type MCFGraph*[Cap, Cost] = object
    n: int
    pos: seq[(int, int)]
    g: seq[seq[Edge[Cap, Cost]]]
  
  type EdgeInfo*[Cap, Cost] = object
    src*, dst*: int
    cap*, flow*: Cap
    cost*: Cost
  
  proc initMCFGraph*[Cap, Cost](n: int): auto =
    MCFGraph[Cap, Cost](n: n, g: newSeq[seq[Edge[Cap, Cost]]](n))

  proc addEdge*[Cap, Cost](self: var MCFGraph[Cap, Cost], src, dst: int, cap: Cap, cost: Cost): int {.discardable.} =
    let m = self.pos.len
    self.pos.add((src, self.g[src].len))
    var
      srcId = self.g[src].len
      dstId = self.g[dst].len
    if src == dst: dstId.inc
    self.g[src].add(Edge[Cap, Cost](dst: dst, rev: dstId, cap: cap, cost: cost))
    self.g[dst].add(Edge[Cap, Cost](dst: src, rev: srcId, cap: Cap(0), cost: -cost))
    return m

  proc getEdge*[Cap, Cost](self: MCFGraph[Cap, Cost], i: int): EdgeInfo[Cap, Cost] =
    let
      e = self.g[self.pos[i][0]][self.pos[i][1]]
      re = self.g[e.dst][e.rev]
    return EdgeInfo[Cap, Cost](src: self.pos[i][0], dst: e.dst, cap: e.cap + re.cap, flow: re.cap, cost: e.cost)

  proc edges*[Cap, Cost](self: MCFGraph[Cap, Cost]): seq[EdgeInfo[Cap, Cost]] =
    let m = self.pos.len
    result = newSeq[EdgeInfo[Cap, Cost]](m)
    for i in 0..<m:
      result[i] = self.getEdge(i)
  
  proc slope*[Cap, Cost](self: var MCFGraph[Cap, Cost], s, t: int, flowLimit: Cap): seq[(Cap, Cost)] =
    var
      dual = newSeqWith(self.n, Cost(0))
      dist = newSeq[Cost](self.n)
      pv, pe = newSeq[int](self.n)
      vis = newSeq[bool](self.n)
    
    proc dualRef(self: var MCFGraph[Cap, Cost]): bool =
      for p in dist.mitems: p = Cost.high
      for p in pv.mitems: p = -1
      for p in pe.mitems: p = -1
      for p in vis.mitems: p = false

      type Q = tuple[key: Cost, dst: int]
      proc `<`(l, r: Q): bool = l.key < r.key

      var que = initHeapQueue[Q]()
      dist[s] = 0
      que.push((Cost(0), s))
      while que.len > 0:
        let v = que.pop().dst
        if vis[v]: continue
        vis[v] = true
        if v == t: break

        for i in 0..<self.g[v].len:
          let e = self.g[v][i]
          if vis[e.dst] or e.cap == 0: continue
          let cost = e.cost - dual[e.dst] + dual[v]
          if dist[e.dst] - dist[v] > cost:
            dist[e.dst] = dist[v] + cost
            pv[e.dst] = v
            pe[e.dst] = i
            que.push((dist[e.dst], e.dst))
      if not vis[t]:
        return false

      for v in 0..<self.n:
        if not vis[v]: continue
        dual[v] -= dist[t] - dist[v]
      return true

    var
      flow = Cap(0)
      cost = Cost(0)
      prevCostPerFlow = -1
    result = newSeq[(Cap, Cost)]()
    result.add((flow, cost))
    while flow < flowLimit:
      if not self.dualRef(): break
      var
        c = flowLimit - flow
        v = t
      while v != s:
        c = min(c, self.g[pv[v]][pe[v]].cap)
        v = pv[v]
      v = t
      while v != s:
        var e = self.g[pv[v]][pe[v]].addr
        e[].cap -= c
        self.g[v][e[].rev].cap += c
        v = pv[v]
      let d = -dual[s]
      flow += c
      cost += c*d
      if prevCostPerFlow == d:
        discard result.pop()
      result.add((flow, cost))
      prevCostPerFlow = cost
  
  proc flow*[Cap, Cost](self: var MCFGraph[Cap, Cost], s, t: int, flowLimit: Cap): (Cap, Cost) =
    self.slope(s, t, flowLimit)[^1]
  proc flow*[Cap, Cost](self: var MCFGraph[Cap, Cost], s, t: int): (Cap, Cost) =
    self.flow(s, t, Cap.high)
  proc slope*[Cap, Cost](self: var MCFGraph[Cap, Cost], s, t: int): seq[(Cap, Cost)] =
    self.slope(s, t, Cap.high)
