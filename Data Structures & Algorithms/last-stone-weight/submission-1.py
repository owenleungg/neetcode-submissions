class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            max_heap.append(stone * -1)
        heapq.heapify(max_heap) # build max heap

        while len(max_heap) > 1:
            candidate1 = heapq.heappop(max_heap)
            candidate2 = heapq.heappop(max_heap)
            if candidate1 != candidate2:
                winner = min(candidate1, candidate2) - max(candidate1, candidate2)
                heapq.heappush(max_heap, winner)
        
        if max_heap:
            return max_heap[0] * -1
        else:
            return 0
