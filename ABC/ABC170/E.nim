import strutils, sequtils, math, heapqueue


proc bit_length(n: int): int =
  if n == 0:
    return 0
  let s = toBin(n, 60)
  return 60 - s.find('1')


type
    SegmentTree* = ref object
        N0: int
        ide_ele: int
        data: seq[int]

proc initSegmntTree*(init_value: seq[int], ide_ele: int): SegmentTree =
    return SegmentTree(N0: 1 shl bit_length(init_value.len - 1), ide_ele: ide_ele, data: newSeqWith(2 * (1 shl bit_length(init_value.len - 1)), ide_ele))

proc update(self: var SegmentTree, idx, x: int) =
    var k = self.N0 - 1 + idx
    self.data[k] = x
    while k != 0:
        k = (k - 1) div 2
        self.data[k] = min(self.data[k * 2 + 1], self.data[k * 2 + 2])


type Pair = object
    priority, idx: int

proc `<`(a, b: Pair): bool = a.priority < b.priority


const M = 2 * 10 ^ 5
var
    infant_to_idx, infant_to_rate: array[M, int]
    hq_arr = newSeqWith(M, initHeapQueue[Pair]())


proc solve() =
    var N, Q: int
    (N, Q) = stdin.readLine.split.map(parseInt)
    var a, b: int
    for i in 0..<N:
        (a, b) = stdin.readLine.split.map(parseInt)
        b -= 1
        infant_to_idx[i] = b
        infant_to_rate[i] = a
        hq_arr[b].push(Pair(priority: -a, idx: i))
    
    const ide_ele = 10 ^ 10
    var seg_tree = initSegmntTree(newSeqWith(M, ide_ele), ide_ele)
    for i, hq in hq_arr:
        if hq.len == 0:
            continue
        seg_tree.update(i, -hq[0].priority)
    
    var ans = newSeq[int]()
    var c, d: int
    for _ in 0..<Q:
        (c, d) = stdin.readLine.split.map(parseInt)
        c -= 1
        d -= 1
        let p_idx = infant_to_idx[c]
        infant_to_idx[c] = d
        while hq_arr[p_idx].len != 0:
            if infant_to_idx[hq_arr[p_idx][0].idx] == p_idx:
                break
            let _ = hq_arr[p_idx].pop()
        if hq_arr[p_idx].len != 0:
            seg_tree.update(p_idx, -hq_arr[p_idx][0].priority)
        else:
            seg_tree.update(p_idx, ide_ele)
        
        hq_arr[d].push(Pair(priority: -infant_to_rate[c], idx: c))
        seg_tree.update(d, -hq_arr[d][0].priority)
        ans.add(seg_tree.data[0])
    
    for i in 0..<Q:
        echo ans[i]


when is_main_module:
    solve()
