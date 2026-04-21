class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        return heapq.nlargest(k, freq_map.keys(), key = freq_map.get)