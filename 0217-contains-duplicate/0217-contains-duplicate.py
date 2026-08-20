class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #brute force
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False
        se=set()
        for i in range(len(nums)):
            if nums[i] in se:
                return True
            se.add(nums[i])
        return False