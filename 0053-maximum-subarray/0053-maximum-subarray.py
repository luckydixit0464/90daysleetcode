class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        su=nums[0]
        maxs=nums[0]
        for i in range(1,len(nums)):
            su=max(nums[i],su+nums[i])
            maxs=max(maxs,su)
        return maxs 
