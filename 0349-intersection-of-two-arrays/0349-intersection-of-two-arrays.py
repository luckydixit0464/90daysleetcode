class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        se1 = set(nums1)
        ans = set()
        for i in range(len(nums2)):
            if nums2[i] in se1:
                ans.add(nums2[i])
        return list(ans)