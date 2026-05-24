class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_mult = [nums[0]] * len(nums)
        suff_mult = [nums[-1]] * len(nums)
        output = [0] * len(nums)
        for i in range(1, len(nums)):
            pref_mult[i] = pref_mult[i - 1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            suff_mult[i] = suff_mult[i+1] * nums[i]
            
        output[0] = suff_mult[1]
        output[-1] = pref_mult[-2]

        print(suff_mult)
        print(pref_mult)
        for i in range(1, len(nums) - 1):
            output[i] = pref_mult[i - 1] * suff_mult[i + 1]
        
        return output