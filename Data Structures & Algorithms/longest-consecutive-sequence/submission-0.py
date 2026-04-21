class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        max_sequence = 0
        for n in nums:
            nums_set.add(n)

        for n in nums_set:
            sequence = 1
            while n-sequence in nums_set:
                sequence += 1

            max_sequence = max(max_sequence, sequence)
        
        return max_sequence