class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        max_count = 0
        count = 1
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1

        for i in range(1, len(nums)):
            if (nums[i] == nums[i-1] + 1):
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
            max_count = max(max_count, count)
        
        return max_count