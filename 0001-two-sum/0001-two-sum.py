class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sen={}
        for i in range(len(nums)):
            if target-nums[i] in sen:
                return [sen[target-nums[i]],i]
            sen[nums[i]]=i


