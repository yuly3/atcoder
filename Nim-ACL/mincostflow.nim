import heapqueue

when not declared ATCODER_INTERNAL_CSR_HPP:
  const ATCODER_INTERNAL_CSR_HPP* = 1

  type csr*[E] = object
    start*: seq[int]
    elist*: seq[E]
  proc initCsr*[E](n: int, edges: seq[(int, E)]): csr[E] =
    var start = newSeq[int](n + 1)
    var elist = newSeq[E](edges.len)
    for e in edges: start[e[0] + 1].inc
    for i in 1..n: start[i] += start[i - 1]
    var counter = start
    for e in edges:
      elist[counter[e[0]]] = e[1]
      counter[e[0]].inc
    return csr[E](start: start, elist: elist)

when not declared ATCODER_INTERNAL_QUEUE_HPP:
  const ATCODER_INTERNAL_QUEUE_HPP* = 1

  type simple_queue[T] = object
    payload: seq[T]
    pos: int
  proc init_simple_queue*[T](): auto = simple_queue[T](payload: newSeq[T](), pos: 0)

  proc len*[T](self: simple_queue[T]): int = self.payload.len - self.pos
  proc empty*[T](self: simple_queue[T]): bool = self.pos == self.payload.len
  proc push*[T](self: var simple_queue[T], t: T) = self.payload.add(t)
  proc front*[T](self: simple_queue[T]): T = self.payload[self.pos]
  proc clear*[T](self: var simple_queue[T]) =
    self.payload.setLen(0)
    self.pos = 0
  proc pop*[T](self: var simple_queue[T]) = self.pos.inc

when not declared ATCODER_INTERNAL_HEAP:
  const ATCODER_INTERNAL_HEAP* = 1
  proc push_heap*[T](v: var openArray[T], p: Slice[int]) {.inline.} =
    var i = p.b
    while i > 0:
      var p = (i - 1) shr 1
      if v[p] < v[i]: swap v[p], v[i]
      else: break
      i = p
  proc pop_heap*[T](v: var openArray[T], p: Slice[int]) {.inline.} =
    swap v[0], v[p.b]
    var p = p
    p.b.dec
    var i = 0
    while true:
      var (c0, c1) = (i * 2 + 1, i * 2 + 2)
      if c1 in p:
        if v[c1] > v[i]:
          if v[c0] > v[c1]:
            swap(v[i], v[c0])
            i = c0
          else:
            swap(v[i], v[c1])
            i = c1
        elif v[c0] > v[i]:
          swap(v[i], v[c0])
          i = c0
        else: break
      elif c0 in p:
        if v[c0] > v[i]:
          swap(v[i], v[c0])
          i = c0
        else: break
      else: break

when not declared ATCODER_MINCOSTFLOW_HPP:
  const ATCODER_MINCOSTFLOW_HPP* = 1

  type MCFEdge*[Cap, Cost] = object
    src*, dst*: int
    cap*, flow*: Cap
    cost*: Cost

  type MCFInternalEdge[Cap, Cost] = object
    dst, rev: int
    cap: Cap
    cost: Cost

  type MCFGraph*[Cap, Cost] = object
    n: int
    edges: seq[MCFEdge[Cap, Cost]]

  proc initMCFGraph*[Cap, Cost](n: int): MCFGraph[Cap, Cost] = result.n = n
  proc initMinCostFLow*[Cap, Cost](n: int): MCFGraph[Cap, Cost] = result.n = n

  proc add_edge*[Cap, Cost](
    self: var MCFGraph[Cap, Cost], src, dst: int, cap: Cap, cost: Cost
  ): int {.discardable.} =
    assert src in 0..<self.n
    assert dst in 0..<self.n
    assert 0 <= cap
    assert 0 <= cost
    var m = self.edges.len
    self.edges.add(MCFEdge[Cap, Cost](src: src, dst: dst, cap: cap, flow: 0, cost: cost))
    return m

  proc get_edge*[Cap, Cost](self: MCFGraph[Cap, Cost], i: int): MCFEdge[Cap, Cost] =
    let m = self.edges.len
    assert i in 0..<m
    return self.edges[i]

  proc edges*[Cap, Cost](self: var MCFGraph[Cap, Cost]): seq[MCFEdge[Cap, Cost]] =
    self.edges
  type MCFQ[Cost] = object
    key: Cost
    dst: int
  proc `<`*[Cost](l, r: MCFQ[Cost]): bool = l.key > r.key

  proc slope*[Cap, Cost](
    self: MCFGraph[Cap, Cost],
    g: var csr[MCFInternalEdge[Cap, Cost]],
    s, t: int,
    flow_limit: Cap
  ): seq[tuple[cap: Cap, cost: Cost]] =
    var
      dual_dist = newSeq[(Cap, Cost)](self.n)
      prev_e = newSeq[int](self.n)
      vis = newSeq[bool](self.n)
      que_min = newSeq[int]()
      que = newSeq[MCFQ[Cost]]()
    proc dual_ref(g: csr[MCFInternalEdge[Cap, Cost]]): bool =
      for i in 0..<self.n: dual_dist[i][1] = Cost.high
      vis.fill(false)
      que_min.setLen(0)
      que.setLen(0)

      var heap_r = 0

      dual_dist[s][1] = 0
      que_min.add(s)
      while que_min.len > 0 or que.len > 0:
        var v: int
        if que_min.len > 0:
          v = que_min.pop()
        else:
          while heap_r < que.len:
            heap_r.inc
            que.push_heap(0 ..< heap_r)
          v = que[0].dst
          que.pop_heap(0 ..< que.len)
          discard que.pop()
          heap_r.dec
        if vis[v]: continue
        vis[v] = true
        if v == t: break
        let (dual_v, dist_v) = dual_dist[v]
        for i in g.start[v] ..< g.start[v + 1]:
          let e = g.elist[i]
          if e.cap == Cap(0): continue
          let cost = e.cost - dual_dist[e.dst][0] + dual_v
          if dual_dist[e.dst][1] - dist_v > cost:
            let dist_to = dist_v + cost
            dual_dist[e.dst][1] = dist_to
            prev_e[e.dst] = e.rev
            if dist_to == dist_v:
              que_min.add(e.dst)
            else:
              que.add(MCFQ[Cost](key: dist_to, dst: e.dst))
      if not vis[t]:
        return false

      for v in 0..<self.n:
        if not vis[v]: continue
        dual_dist[v][0] -= dual_dist[t][1] - dual_dist[v][1]
      return true
    var
      flow: Cap = 0
      cost: Cost = 0
      prev_cost_per_flow: Cost = -1
    result = @[(Cap(0), Cost(0))]
    while flow < flow_limit:
      if not g.dual_ref(): break
      var c = flow_limit - flow
      block:
        var v = t
        while v != s:
          c = min(c, g.elist[g.elist[prev_e[v]].rev].cap)
          v = g.elist[prev_e[v]].dst
      block:
        var v = t
        while v != s:
          var e = g.elist[prev_e[v]].addr
          e[].cap += c
          g.elist[e[].rev].cap -= c
          v = g.elist[prev_e[v]].dst
      let d = -dual_dist[s][0]
      flow += c
      cost += c * d
      if prev_cost_per_flow == d:
        discard result.pop()
      result.add((flow, cost))
      prev_cost_per_flow = d

  proc slope*[Cap, Cost](
    self: var MCFGraph[Cap, Cost],
    s, t: int,
    flow_limit: Cap
  ): seq[tuple[cap: Cap, cost: Cost]] =
    assert s in 0..<self.n
    assert t in 0..<self.n
    assert s != t

    let m = self.edges.len
    var edge_idx = newSeq[int](m)

    var g = block:
      var degree = newSeq[int](self.n)
      var redge_idx = newSeq[int](m)
      var elist = newSeqOfCap[(int, MCFInternalEdge[Cap, Cost])](2 * m)
      for i in 0..<m:
        let e = self.edges[i]
        edge_idx[i] = degree[e.src]
        degree[e.src].inc
        redge_idx[i] = degree[e.dst]
        degree[e.dst].inc
        elist.add(
          (
            e.src,
            MCFInternalEdge[Cap, Cost](dst: e.dst, rev: -1, cap: e.cap - e.flow, cost: e.cost)
          )
        )
        elist.add(
          (
            e.dst,
            MCFInternalEdge[Cap, Cost](dst: e.src, rev: -1, cap: e.flow, cost: -e.cost)
          )
        )
      var g = initCSR[MCFInternalEdge[Cap, Cost]](self.n, elist)
      for i in 0..<m:
        let e = self.edges[i]
        edge_idx[i] += g.start[e.src]
        redge_idx[i] += g.start[e.dst]
        g.elist[edge_idx[i]].rev = redge_idx[i];
        g.elist[redge_idx[i]].rev = edge_idx[i];
      g

    result = self.slope(g, s, t, flow_limit)

    for i in 0..<m:
      let e = g.elist[edge_idx[i]]
      self.edges[i].flow = self.edges[i].cap - e.cap

  proc flow*[Cap, Cost](
    self: var MCFGraph[Cap, Cost],
    s, t: int,
    flow_limit: Cap
  ): tuple[cap: Cap, cost: Cost] = self.slope(s, t, flow_limit)[^1]
  proc flow*[Cap, Cost](self: var MCFGraph[Cap, Cost], s, t: int): tuple[
      cap: Cap, cost: Cost] = self.flow(s, t, Cap.high)
  proc slope*[Cap, Cost](self: var MCFGraph[Cap, Cost], s, t: int): seq[tuple[
      cap: Cap, cost: Cost]] = self.slope(s, t, Cap.high)
