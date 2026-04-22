class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-2, -1 ,-1, 0, 1, 2]
        output = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            L = i + 1         
            R = len(nums) - 1 
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if total == 0:
                    output.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1 
                    R -= 1
                if total < 0:
                    L += 1
                elif total > 0:
                    R -= 1
            
        return output