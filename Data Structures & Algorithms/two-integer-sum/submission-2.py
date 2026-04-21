class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = []
        for i, val in enumerate(nums):
            indexed_nums.append([val, i])

        indexed_nums.sort()
        left = 0
        right = len(indexed_nums) - 1
    
        while left < right:        
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else: 
                return [min(indexed_nums[left][1], indexed_nums[right][1]), max(indexed_nums[left][1], indexed_nums[right][1])]
            